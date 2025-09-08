import streamlit as st

uploaded_files=st.file_uploader("Upload files here",type="pdf",accept_multiple_files=False)

user_query=st.text_area("Type your prompt here",height=100,placeholder="Ask")

ask_question=st.button("Ask for answer")

if ask_question:

    if uploaded_files:

        st.chat_message("user").write(user_query)
        fixed_response="Hi,this is fixed response"
        st.chat_message("AI Lawyer").write(fixed_response)

    else:
        st.error("Kindly upload a file")    
