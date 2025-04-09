import streamlit as st

def check_password():
    def password_entered():
        if st.session_state["password"] == "1234":
            st.session_state["password_correct"] = True
            del st.session_state["password"]
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        st.text_input("Enter access code:", type="password", on_change=password_entered, key="password")
        return False
    elif not st.session_state["password_correct"]:
        st.text_input("Enter access code:", type="password", on_change=password_entered, key="password")
        st.error("Wrong access code.")
        return False
    else:
        return True
