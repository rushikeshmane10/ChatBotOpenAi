from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Set your Groq API key
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"

# Define your prompt
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please respond to the user queries"),
        ("user", "Question: {question}")
    ]
)

# Streamlit UI
st.title('Test Project With GROQ API')
input_text = st.text_input("Search the topic you want")

# Groq LLM
# Replace the old model name with a supported one
llm = ChatGroq(
    model="llama-3.1-8b-instant",  # use a currently supported model
    temperature=0
)


# Output parser and chain
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

# Invoke the chain if user inputs a question
if input_text:
    st.write(chain.invoke({'question': input_text}))
