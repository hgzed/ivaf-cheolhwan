
import streamlit as st
import datetime

st.set_page_config(page_title="IVAF x 철환 프로토콜", layout="wide")

st.title("🧠 IVAF 철환 Signature Edition")
st.subheader("의식 기반 루틴 트래커")

# 1. Intuition Tracker
st.header("1️⃣ Intuition Tracker: 오늘의 직관")
intuition = st.text_area("오늘 떠오른 상징/키워드/감정은?", placeholder="예: 물결, 투명함, 긴장감")
st.markdown("- 선택한 감정/키워드가 오늘의 방향을 암시합니다.")

# 2. Visualization Generator
st.header("2️⃣ Visualization Generator: 흐름 구조화")
st.markdown("오늘의 키워드를 어떻게 구조화할 수 있을까요?")

col1, col2 = st.columns(2)
with col1:
    core_value = st.text_input("핵심 키워드")
    linked_emotion = st.text_input("연결된 감정")
with col2:
    symbolic_image = st.text_input("떠오른 상징")
    movement = st.selectbox("오늘의 흐름은?", ["수렴", "확산", "정지", "순환"])

if st.button("🌀 시각적 흐름 구조 생성"):
    st.success(f"🧭 {core_value} → ({linked_emotion}) → {symbolic_image} [{movement}]로 연결되는 흐름이 형성되었습니다.")

# 3. Action Planner
st.header("3️⃣ Action Planner: 오늘의 실행")
todo_items = st.text_area("오늘 실천할 항목 (한 줄에 하나씩)", placeholder="예: 원고 쓰기\n루틴 점검\n명상 15분")
timebox = st.slider("예상 실행 시간 (총 분 단위)", 30, 240, 90)
if st.button("✅ 실행 플랜 저장"):
    st.success(f"총 {timebox}분 동안 다음 행동을 실행할 계획입니다:")
    for i, item in enumerate(todo_items.split("\n")):
        st.markdown(f"- {item.strip()}")

# 4. Feedback Log
st.header("4️⃣ Feedback Log: 오늘의 피드백")
exec_score = st.slider("오늘의 실행력 점수는?", 0, 10, 7)
alignment = st.slider("직관과 실행의 정렬도는?", 0, 10, 6)
journal = st.text_area("오늘의 내면 회고", placeholder="오늘 나는 어떤 감정으로 움직였는가?")

if st.button("📘 회고 저장"):
    st.markdown("---")
    st.subheader("🌒 오늘의 회고 요약")
    st.markdown(f"- 실행 점수: {exec_score}/10")
    st.markdown(f"- 정렬도: {alignment}/10")
    st.markdown(f"- 회고 내용: {journal}")
    st.success("회고가 저장되었습니다. 내일 다시 확인하세요.")
