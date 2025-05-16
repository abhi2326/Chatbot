import streamlit as st
from scraper.dynamic_scraper import scrape_dynamic
from utils.text_utils import chunk_text
from llm_integration.rag_pipeline import get_chatbot
import datetime

st.set_page_config(page_title="Smart Web Chatbot", layout="wide")
st.title("🌐 Smart Website Chatbot")

if "qa_bot" not in st.session_state:
    st.session_state.qa_bot = None
if "messages" not in st.session_state:
    st.session_state.messages = []

url = st.text_input("🔗 Enter the website URL:")

if st.button("Scrape and Analyze Website"):
    try:
        with st.spinner("⏳ Scraping and processing website..."):
            raw_text = scrape_dynamic(url)
            if not raw_text.strip():
                st.error("No content found. Please check the URL or try another site.")
            else:
                chunks = chunk_text(raw_text)
                qa_bot = get_chatbot(chunks)
                st.session_state.qa_bot = qa_bot
                st.success("✅ Website content loaded and ready for questions!")
    except Exception as e:
        st.error(f"❌ Error: {str(e)}")

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if st.session_state.qa_bot:
    user_input = st.chat_input("Ask anything about the website:")
    if user_input:
        with st.chat_message("user"):
            st.markdown(user_input)
        st.session_state.messages.append({"role": "user", "content": user_input})

        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = st.session_state.qa_bot.run(user_input)
                st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})

if st.session_state.messages:
    chat_log = "\n\n".join(
        f"{'User' if msg['role'] == 'user' else 'Assistant'}: {msg['content']}"
        for msg in st.session_state.messages
    )
    st.download_button(
        label="💾 Download Chat History",
        data=chat_log,
        file_name=f"chat_history_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
        mime="text/plain"
    )