# Smart Website-Aware Chatbot

## Description
An intelligent chatbot that scrapes the content of any website, even dynamic ones, and answers questions based solely on that website content using OpenAI LLMs.

## Setup
1. Install dependencies:
```
pip install -r requirements.txt
python -m playwright install
```

2. Set your OpenAI API Key in `.env`:
```
OPENAI_API_KEY=your_openai_api_key_here
```

3. Run the app:
```
streamlit run app.py
```