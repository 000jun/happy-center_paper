"""
물품 품의서 작성 프로그램
"""

import streamlit as st
import datetime
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname('STREAMLIT_PROJECT')))) # 상위 폴더 모듈(read_number) 불러오기 위해 경로 설정
from read_number import *
import pandas as pd

# 전역변수 설정
value_dict = {}

# 변수 선언
department_list = ['중등교육과']
year_list = [str(year)+'년' for year in range(2024, 2026)] # 년도 리스트
month_list = [str(month)+'월' for month in range(1, 13)] # 월 리스트
budget_list = [
    '교육연구운영지원',
    '교실수업개선',
    '교원인사관리',
    '교육과정운영지원',
    '독서논술교육운영',
    '문화예술교육활동',
    '공유재산및물품관리',
    '학교폭력예방및교육',
    '학생생활지도지원',
    '학생안전관리',
    '기관기본운영비',
    '진학시험및입학전형관리',
    '현장중심장학지원',
    '진로진학교육운영',
    '학부모및주민참여확대',
    '특색교육과정운영'
]
budget_list.sort()

# 레이아웃 설정
st.set_page_config(page_title='품의서 작성 프로그램', layout='wide')
st.title('일상경비 품의서 작성 프로그램')
st.subheader('정보 입력')

date_col = st.columns(6)
with date_col[0]:
    # 부서 선택
    department = st.selectbox('부서를 입력해 주세요', (department_list))
with date_col[1]:
    # 지급 년 입력
    year_data = st.selectbox('요구년도를 입력해 주세요', (year_list))
with date_col[2]:
    # 지급 월 입력
    month_data = st.selectbox('요구월을 입력해 주세요', (month_list))

# 예산교부 요청내역 선택
select_budget_list = st.multiselect('예산교부 요청내역', budget_list)

# 예산 요청 금액 입력
for i in range(len(select_budget_list)):
    budget_value = st.number_input(f'{select_budget_list[i]} 금액 입력', min_value=0)
    if budget_value:
        preview_value = f':red[{select_budget_list[i]}]' + ' : ' + f':orange[{readnumber(budget_value)}]원'
        budget_value_kor = st.write(preview_value) # int to kor
    str_budget = str(format(budget_value, ','))
    total_budget = budget_value
    value_dict[select_budget_list[i]] = total_budget

total_cost = sum(value_dict.values())

# #테스트 버튼
# test_btn = st.button('테스트')
# if test_btn:
#     st.write(select_budget_list)
#     st.write(total_cost)

# 품의명 입력
base_line = '{} {} {} 일상경비'.format(year_data, month_data, department)
title = base_line + ' 교부 건의'

# print test FIXME:
testing_button = st.button('출력')
if testing_button: # 출력 버튼 클릭시 작동 로직

    # 입력값 데이터프레임 반환 : value -> dataframe
    df = pd.DataFrame(value_dict, index=[0])
    # df.to_excel('df.xlsx')

    # 본문 생성
    result_paper = title +'\n\n' # 제목
    result_paper += f'{base_line} 예산을 다음과 같이 교부 요청합니다.\n' # 본문
    for i in range(len(df.columns)):
        line = (str(i+1) + '. ' + str(df.columns[i]) + ': '+ str(format(df[df.columns[i]].values[0], ',')) + '원' +'\n')
        result_paper += line
    result_paper += '\n'
    result_paper += '붙임  일상경비교부요구지출품의서 1부.  끝.'

    # 본문 출력
    st.subheader('품의서 출력 결과')
    # st.write(result_paper)
    st.text_area(
        '품의서 출력 결과',
        result_paper,
        height=400
    )