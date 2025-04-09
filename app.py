import streamlit as st

st.set_page_config(page_title="TenderBot", layout="wide")

st.title("🤖 TenderBot")
st.write("مرحبًا بك في TenderBot، الشات بوت الذكي للمناقصات!")

user_input = st.text_input("اكتب استفسارك عن المناقصة:")

if user_input:
    st.write("🔍 جاري معالجة استفسارك...")
    st.success("✅ تم تحليل استفسارك: " + user_input)

# نضيف سطر يخلي التطبيق "ينتظر" وما يوقف فجأة
st.stop()
