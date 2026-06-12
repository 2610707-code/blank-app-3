import streamlit as st
import pandas as pd

# 1. 초기 도서 목록 설정 (session_state를 사용하여 데이터 유지)
if 'books' not in st.session_state:
    st.session_state.books = ['해리포터', '어린왕자', '데미안']

st.title("📚 도서 대출 프로그램")

# 2. 현재 도서 목록 출력 (st.dataframe 사용)
st.write("### 현재 도서 목록")
if st.session_state.books:
    # 리스트를 데이터프레임으로 변환하여 표 형태로 깔끔하게 출력
    df_books = pd.DataFrame(st.session_state.books, columns=['도서명'])
    st.dataframe(df_books, use_container_width=True)
else:
    st.info("현재 대출 가능한 도서가 없습니다.")

st.divider()

# 3. 대출할 도서 이름 입력 위젯 (st.text_input)
name = st.text_input("대출할 도서 이름을 입력하세요:")

# 4. '대출하기' 버튼 및 처리 로직 (st.success, st.error 사용)
if st.button("대출하기"):
    if not name:
        st.warning("도서 이름을 먼저 입력해 주세요.")
    elif name not in st.session_state.books:
        # 목록에 없는 경우 (기존 코드의 '이미 대출된 도서입니다' 역할)
        st.error(f"'{name}'은(는) 이미 대출된 도서이거나 목록에 없는 도서입니다.")
    else:
        # 목록에 있는 경우 리스트에서 삭제하고 성공 메시지 출력
        st.session_state.books.remove(name)
        st.success(f"'{name}' 대출이 완료되었습니다!")
        # 상태가 변경되었으므로 화면을 새로고침하여 목록 표(Dataframe) 갱신
        st.rerun()