"""
자원봉사자 품의서 작성 프로그램
"""

import streamlit as st
import datetime
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname('STREAMLIT_PROJECT')))) # 상위 폴더 모듈(read_number) 불러오기 위해 경로 설정
from read_number import *
import pandas as pd

# 변수 선언
year_list = [str(year)+'년' for year in range(2024, 2026)] # 년도 리스트
month_list = [str(month)+'월' for month in range(1, 13)] # 월 리스트
# 전역변수 설정
value_dict = {}

# 레이아웃 설정
st.set_page_config(page_title='품의서 작성 프로그램', layout='wide')
st.title('자원봉사자 품의서 작성 프로그램')
st.subheader('정보 입력')

# 자원봉사자 활동 센터 선택
# category = st.multiselect('활동센터 선택', ['김해', '무계', '장유'])

# 지급 년 입력
year_data = st.selectbox('고지년도를 입력해 주세요', (year_list))

# 지급 월 입력
month_data = st.selectbox('고지월을 입력해 주세요', (month_list))

# 총 지급 금액
cost_value = st.number_input('금액 입력', min_value=0)
if cost_value:
    cost_value_kor = st.write(f'금 :orange[{readnumber(cost_value)}]원') # int to kor
str_cost = str(format(cost_value, ','))
total_cost = f'금{str_cost}원' + f'(금{readnumber(cost_value)}원)'

# 내역
content = st.text_input('내역 입력', value='붙임파일 참조')

# 지급대상
people_col = st.columns(8)
with people_col[0]:
    people = st.text_input('지급대상 대표자명 입력', placeholder='ex)홍길동')
with people_col[1]:
    people_num = st.number_input('지급 대상 총 인원수', min_value=0, value=1)
if people_num > 1:
    people_data = people + ' 외 ' + str(people_num-1) + '명'
    st.write(people + ':orange[ 외 ' + str(people_num-1) + '명]')
else:
    people_data = people
    st.write(people_data)

# 품의명 입력
title = '{} {} 김해교육협력지원센터 자원봉사자 활동비 지급'.format(year_data, month_data)
value_dict['금액'] = total_cost
value_dict['내역'] = content
value_dict['지급대상'] = people_data
value_dict['예산과목'] = '특색교육과정운영 >'

# print test FIXME:
testing_button = st.button('테스트')
if testing_button: # 테스트 버튼 클릭시 작동 로직

    # 입력값 데이터프레임 반환 : value -> dataframe
    df = pd.DataFrame(value_dict, index=[0])
    # df.to_excel('df.xlsx')

    # 본문 생성
    result_paper = title +'\n\n' # 제목
    result_paper += '{} {} 김해교육협력지원센터 자원봉사자 활동비를 다음과 같이 지급하고자 합니다.\n'.format(year_data, month_data)
    for i in range(len(df.columns)):
        line = (str(i+1) + '. ' + str(df.columns[i]) + ': '+ str(df[df.columns[i]].values[0]) +'\n')
        result_paper += line

    # 본문 출력
    st.subheader('품의서 출력 결과')
    st.text_area(
        '품의서 출력 결과',
        result_paper,
        height=400
    )