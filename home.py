# st.write("""
# **INDUSTRY**
# <br>
# Software Application
# """, unsafe_allow_html=True)

import streamlit as st

st.set_page_config(
    page_title='품의서 자동 생성 프로그램'
)
st.title('품의서 자동 생성 프로그램')
st.markdown("""---""")
st.subheader("사용법 안내")
st.write("""
:point_left: :blue[사이드바]에서 작성할 품의의 :blue[템플릿]을 클릭하세요.
<br>
템플릿 별로 요청하는 :orange[정보]를 :orange[입력]한 후 :orange[작성 버튼]을 누르면 품의서 :orange[제목]과 :orange[내용]을 :orange[출력]합니다
""", unsafe_allow_html=True)
st.markdown("######")
st.markdown("######")
st.subheader('버전 및 업데이트')
st.write("""
V1.0.0.-alpha1 (2024-02-25) : 알파버전 테스팅
""", unsafe_allow_html=True)
st.markdown("######")
st.markdown("######")
st.subheader("개발자")
st.write("""
최영준, 이욱상
""")
st.markdown("######")
st.markdown("######")
st.subheader("문의")
st.write("""
템플릿 추가 등에 관한 문의
<br>
:e-mail: zerojun@korea.kr
""", unsafe_allow_html=True)