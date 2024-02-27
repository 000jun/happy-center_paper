import streamlit as st
import datetime
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname('STREAMLIT_PROJECT')))) # 상위 폴더 모듈(read_number) 불러오기 위해 경로 설정
from read_number import *
import pandas as pd

from attached_file import write_attach

# 전역변수 설정
value_dict = {}
# 변수 선언
year_list = [str(year)+'년' for year in range(2024, 2026)] # 년도 리스트
month_list = [str(month)+'월' for month in range(1, 13)] # 월 리스트

# 레이아웃 설정
st.set_page_config(page_title='품의서 작성 프로그램', layout='wide')
st.title('품의서 작성 프로그램')
st.subheader('정보 입력')

date_col = st.columns(6)
with date_col[0]:
    # 소속 입력 (중등교육과, 김해교육협력지원센터)
    department = st.selectbox('소속을 선택하세요', ('중등교육과', '김해교육협력지원센터'))
with date_col[1]:
    # 지급 여비 년, 월 입력
    year_data = st.selectbox('고지년도를 입력해 주세요', (year_list))
with date_col[2]:
    # 고지월 입력
    month_data = st.selectbox('고지월을 입력해 주세요', (month_list))

title_body = year_data + ' ' + month_data + ' ' + department + ' ' + '인터넷 전화 요금'
st.write(title_body)

# 금액
cost_value = st.number_input('금액 입력', min_value=0)
if cost_value:
    cost_value_kor = st.write(f'금 :orange[{readnumber(cost_value)}]원') # int to kor
str_cost = str(format(cost_value, ','))
total_cost = f'금{str_cost}원' + f'(금{readnumber(cost_value)}원)'
value_dict['금액'] = total_cost

# 거래처
vendor = st.selectbox('거래처를 선택하세요', ('SKT', 'KT', 'LGU+'))

# 예산
budget_value = st.text_input('예산 과목 입력', 'test_value')
value_dict['예산'] = budget_value

# 붙임파일 작성
attached_file = '붙임  일반지출품의서 1부.  끝.'

# print test FIXME:
testing_button = st.button('품의서 출력')
if testing_button: # 테스트 버튼 클릭시 작동 로직

    # 입력값 데이터프레임 반환 : value -> dataframe
    df = pd.DataFrame(value_dict, index=[0])
    # df.to_excel('df.xlsx')

    # 본문 생성
    result_paper = title_body + +'\n\n' # 제목
    result_paper += f'{items_value}를 다음과 같이 구입하고자 합니다.\n' # 본문
    for i in range(len(df.columns)):
        line = (str(i+1) + '. ' + str(df.columns[i]) + ': '+ str(df[df.columns[i]].values[0]) +'\n')
        result_paper += line

    result_paper += '\n' + attached_file # 붙임파일 추가

    # 본문 출력
    st.subheader('품의서 출력 결과')
    st.text_area(
        '품의서 출력 결과',
        result_paper,
        height=400
    )