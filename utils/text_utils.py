from langchain.text_splitter import CharacterTextSplitter

def chunk_text(text):
    splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=700,
        chunk_overlap=100,
        length_function=len
    )
    return splitter.split_text(text)