"""
협의회비 품의서 작성 프로그램
"""

import streamlit as st
import datetime
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname('STREAMLIT_PROJECT')))) # 상위 폴더 모듈(read_number) 불러오기 위해 경로 설정
from read_number import *
import pandas as pd

# 전역변수 설정
value_dict = {}

# 레이아웃 설정
st.set_page_config(page_title='협의회비 품의서 작성 프로그램', layout='wide') #탭 이름
st.title('협의회비 품의서 작성 프로그램') # 타이틀
st.subheader('정보 입력')

# 품의명 입력
title = st.text_input('품의명 입력')

# 체크박스
checks = st.columns(10, gap='small')
with checks[0]:
    paper = st.checkbox('관련', True) # 관련문서 체크
with checks[1]:
    cost = st.checkbox('금액', True)
with checks[2]:
    date = st.checkbox('일시', True)
with checks[3]:
    place = st.checkbox('장소', False)
with checks[4]:
    topic = st.checkbox('안건', False)
with checks[5]:
    people = st.checkbox('참석자', False)
with checks[6]:
    detail = st.checkbox('예산과목', True)

# 관련문서
if paper == True:
    paper_col = st.columns(2)
    with paper_col[0]:
        paper_haed = st.text_input('관련문서 부서', '중등교육과')
    with paper_col[1]:
        paper_tail = st.text_input('문서번호', placeholder='1234호')
    link_paper = paper_haed + '-' + paper_tail # 관련문서 value
    value_dict['관련'] = link_paper

# 금액
if cost == True:
    cost_value = st.number_input('금액 입력', min_value=0)
    if cost_value:
        cost_value_kor = st.write(f'금 :orange[{readnumber(cost_value)}]원') # int to kor
    str_cost = str(format(cost_value, ','))
    total_cost = f'금{str_cost}원' + f'(금{readnumber(cost_value)}원)'
    value_dict['금액'] = total_cost

# 일시
if date == True:
    date_value = st.date_input('날짜 입력',datetime.datetime.today())
    date_value = date_value.strftime('%Y-%m-%d')
    value_dict['일시'] = date_value

# 장소
if place == True:
    place_value = st.text_input('장소 입력')
    value_dict['장소'] = place_value

# 안건
if topic == True:
    topic_value = st.text_input('안건 입력')
    value_dict['안건'] = topic_value

if people == True:
    # 지급대상
    people_value = st.text_input('세부 지급대상 입력',
                                 placeholder='업무담당자 5명, 관계자 5명, (총 10명)'
                                 )
    value_dict['지급대상'] = people_value
    # people_col = st.columns(10)
    # with people_col[0]:
    #     people = st.text_input('지급대상 입력', placeholder='ex) 업무담당자')
    # with people_col[1]:
    #     people_num = st.number_input('지급 대상 총 인원수', min_value=0, value=1)
    # if people_num > 1:
    #     people_data = people + ' 외 ' + str(people_num-1) + '명'
    #     st.write(people + ':orange[ 외 ' + str(people_num-1) + '명]')
    # else:
    #     people_data = people
    #     st.write(people_data)

# 품의명 입력
value_dict['예산과목'] = '특색교육과정운영 >'

# print test FIXME:
testing_button = st.button('테스트')
if testing_button: # 테스트 버튼 클릭시 작동 로직
    
    # 입력값 데이터프레임 반환 : value -> dataframe
    df = pd.DataFrame(value_dict, index=[0])
    # df.to_excel('df.xlsx')

    # 본문 생성
    result_paper = title +'\n\n' # 제목
    result_paper += f'협의회비를 다음과 같이 지출하고자 합니다.\n' # 본문
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