"""
물품 품의서 작성 프로그램
"""

import streamlit as st
import datetime
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname('STREAMLIT_PROJECT')))) # 상위 폴더 모듈(read_number) 불러오기 위해 경로 설정
from read_number import *
import pandas as pd

st.subheader('붙임파일')
attached_file_list = []

attached_col = st.columns(5)
with attached_col[0]:
    attached_file_num = st.number_input('붙임 파일 개수', min_value=1)

for i in range(attached_file_num):
    if i == 0:
        st.text_input(f'붙임 파일{i+1} 이름 입력(기본값)', value='지출품의서 1부.')
        attached_file_list.append('지출품의서 1부.')
    else:
        i = st.text_input(f'붙임 파일{i+1} 이름 입력', placeholder='ex) 영수증 1부.')
        attached_file_list.append(i)

st.write('붙임파일 미리보기')
st.write(attached_file_list)

# 붙임파일 리스트 작성
result_paper = '' # -> 최종 결과

# 붙임파일 최종 작성 알고리즘
# 1. 붙임파일이 1개일 때
if len(attached_file_list) == 1:
    result_paper += (f'붙임 {attached_file_list[0]}' + '  끝.') # 붙임 추가 -> 끝. 추가
# 2. 붙임파일이 2개 이상일 때
else:
    for num in range(len(attached_file_list)):
        if num == 0:
            result_paper += (f'붙임 {num+1}. {attached_file_list[num]}' + '\n') # 첫 번호 -> 붙임 추가
        elif num == len(attached_file_list)-1:
            result_paper += (f'{num+1}. {attached_file_list[num]}' + '  끝.') # 마지막 번호 -> 끝. 추가
        else:
            result_paper += (f'{num+1}. {attached_file_list[num]}' + '\n')

result = st.button('붙임파일 리스트 작성')
if result:
    st.text_area('품의서',
                result_paper,
                height=200
                )