import streamlit as st


def main():
    st.set_page_config(
        page_title="Hello",
        page_icon="👋",
    )
    st.write("# Bomidi")

    st.sidebar.success("Select a demo above.")
