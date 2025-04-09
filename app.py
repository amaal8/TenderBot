import streamlit as st
from auth import check_password
from utils import handle_file_upload, answer_query

st.set_page_config(page_title="TenderBot 💼", layout="wide")

if not check_password():
    st.stop()

st.title("🤖 TenderBot - Your Tender Assistant")
st.markdown("""
Upload tender-related documents (Excel, PDF, Word) and ask questions in English or Arabic.
""")

# Session state for chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

uploaded_file = st.file_uploader("📁 Upload a file", type=["pdf", "docx", "xlsx"])
if uploaded_file:
    file_msg = handle_file_upload(uploaded_file)
    st.success(file_msg)

query = st.text_input("💬 Ask something about your tenders:")
if query:
    with st.spinner("Thinking..."):
        response = answer_query(query)
    st.session_state.chat_history.append((query, response))

# Show chat history
if st.session_state.chat_history:
    st.markdown("---")
    st.subheader("📝 Chat History")
    for q, r in reversed(st.session_state.chat_history):
        st.markdown(f"**You:** {q}")
        st.markdown(f"**TenderBot:** {r}")
