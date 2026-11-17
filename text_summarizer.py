from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
import streamlit as st

load_dotenv()

llm= ChatGroq(model ="openai/gpt-oss-20b")

prompt = ChatPromptTemplate.from_template(
    "Summarize the following text in simple words using 5 to 6 bullet points:\n\n {text}"
    )

chain = prompt | llm

st.title("Text Summarizer")
st.write("Enter a paragraph to generate a short summary.")


text = st.text_area("Enter your text here: ")

if st.button ("Summarize"):
    if text.strip():
        with st.spinner("Generating summary..."):
            response = chain.invoke({"text": text})
        st.subheader("Summary:")
        st.write(response.content)

    else:
        st.warning("Please enter some text to summarize.")
