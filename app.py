import streamlit as st
import pandas as pd
from agent import create_agent, ask_agent

st.set_page_config(
    page_title="DataChat",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 DataChat")
st.caption("อัพโหลด CSV แล้วคุยกับข้อมูลของคุณได้เลย")

with st.sidebar:
    st.header("📁 อัพโหลดข้อมูล")
    uploaded_file = st.file_uploader("เลือกไฟล์ CSV", type=["csv"])

    if uploaded_file:
        st.success("✅ โหลดข้อมูลสำเร็จ")

    st.divider()
    st.caption("สร้างโดย Papimon Kongnark")
    st.caption("Powered by Groq + LangChain")

if uploaded_file is None:
    st.info("👈 เริ่มต้นด้วยการอัพโหลด CSV ในแถบด้านซ้าย")

    st.subheader("💡 ตัวอย่างคำถามที่ถามได้")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("- สินค้าไหนขายดีที่สุด?")
        st.markdown("- ยอดขายเฉลี่ยต่อเดือนเท่าไหร่?")
        st.markdown("- มีข้อมูลกี่แถว กี่คอลัมน์?")
    with col2:
        st.markdown("- คอลัมน์ไหนมีค่าว่างบ้าง?")
        st.markdown("- แสดง top 5 ที่มียอดสูงสุด")
        st.markdown("- สรุปข้อมูลทั้งหมดให้หน่อย")

else:
    for enc in ["utf-8", "latin-1", "cp874", "cp1252"]:
        try:
            uploaded_file.seek(0)
            df = pd.read_csv(uploaded_file, encoding=enc)
            break
        except (UnicodeDecodeError, Exception):
            continue
    else:
        st.error("ไม่สามารถอ่านไฟล์ได้ กรุณาบันทึกไฟล์ใหม่เป็น UTF-8")
        st.stop()

    if "agent" not in st.session_state or st.session_state.get("file_name") != uploaded_file.name:
        with st.spinner("🔄 กำลังโหลด AI Agent..."):
            st.session_state.agent = create_agent(df)
            st.session_state.file_name = uploaded_file.name
            st.session_state.messages = []

    with st.expander("📊 ดูตัวอย่างข้อมูล", expanded=True):
        col1, col2, col3 = st.columns(3)
        col1.metric("แถวทั้งหมด", f"{df.shape[0]:,}")
        col2.metric("คอลัมน์", df.shape[1])
        col3.metric("ข้อมูลที่หายไป", df.isnull().sum().sum())
        st.dataframe(df.head(), use_container_width=True)

    st.divider()

    st.subheader("💬 ถามคำถาม")

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("ถามเกี่ยวกับข้อมูลของคุณ..."):
        with st.chat_message("user"):
            st.markdown(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})

        with st.chat_message("assistant"):
            with st.spinner("🤔 กำลังวิเคราะห์..."):
                response = ask_agent(st.session_state.agent, prompt)
                st.markdown(response)
                st.session_state.messages.append({"role": "assistant", "content": response})
