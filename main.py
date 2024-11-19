import streamlit as st

app_title = "자동 강의 PPT 생성기"

usage = """
1. 강의 주제와 대상 특성을 입력합니다.
2. 생성 버튼을 눌러 프로세스를 시작합니다.
3. 생성된 피피티를 결과 페이지에서 다운로드 받습니다.
"""

def main():
    st.title(app_title)
    st.markdown(usage)

if __name__ == "__main__":
    main()
