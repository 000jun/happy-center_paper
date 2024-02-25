"""
수도요금 품의서 작성 프로그램
"""

import streamlit as st
import datetime
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname('STREAMLIT_PROJECT')))) # 상위 폴더 모듈(read_number) 불러오기 위해 경로 설정
from read_number import *

# 변수 선언
years = [year for year in range(2020, 2026)] # 년도 리스트
months = [month for month in range(1, 13)] # 월 리스트
targets = ['YEAR', 'MONTH', 'COST', 'KOREAN_WON', 'START', 'END', 'BUDGET'] # 품의서 txt 변환 타겟 문자 리스트

# 레이아웃 설정
st.set_page_config(page_title='수도요금 품의서 작성 프로그램', layout='wide')

# 타이틀
st.title('수도요금 납부 품의서 작성 프로그램')

# Subheader 적용
st.subheader('고지서 정보 입력')

# 고지년월 입력
year_data = st.selectbox(
    '고지년도를 입력해 주세요',
    (years)
)

# 고지월 입력
month_data = st.selectbox(
    '고지월을 입력해 주세요',
    (months)
)

# 고지서 금액 입력
paper_cost = st.number_input(
    '수도요금을 입력해 주세요',
    min_value=0, max_value=100000000, value=0,
)
if paper_cost:
    st.write(f'금 :orange[{readnumber(paper_cost)}]원')

# 고지서 금액 한글 변환
kor_cost = readnumber(paper_cost)
paper_cost = format(paper_cost, ',') # 에러 발생해서 int -> 한글변환 -> str(,) 변환

# 산정 시작일
start_date = st.date_input(
    '산정 시작일을 입력해 주세요',
    datetime.datetime.today()
)

# 산정 종료일
end_date = st.date_input(
    '산정 종료일을 입력해 주세요',
    datetime.datetime.today()
)

# 예산과목
budget_item = '특색교육과정운영>행복마을학교운영>'

# input_value리스트
input_list = [year_data, month_data, paper_cost, kor_cost, start_date, end_date, budget_item]

# 품의서 생성 버튼
button = st.button('품의서 생성')
if button:
    st.subheader('품의서 출력 결과')
    
    f = open('template_water.txt', 'r', encoding='utf-8')
    
    data = f.read()

    for i in range(len(targets)):
        data = data.replace(targets[i], str(input_list[i]))

    st.text_area(
        '품의서 출력 결과',
        data,
        height=400
    )

