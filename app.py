import streamlit as st
import time

st.set_page_config(page_title="TenderBot", layout="wide")

st.title("🤖 TenderBot")
st.write("مرحبًا بك في TenderBot، الشات بوت الذكي للمناقصات!")

# واجهة إدخال
user_input = st.text_input("💬 اكتب استفسارك عن المناقصة:")

if user_input:
    with st.spinner("جاري المعالجة..."):
        time.sleep(2)  # محاكاة لعملية الذكاء الاصطناعي
        st.success(f"✅ هذا الرد التجريبي على: {user_input}")

# نضيف عنصر تفاعلي يبقي الصفحة حية
st.button("إعادة تعيين")
