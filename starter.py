from config import get_api_key
from openai import OpenAI
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from langchain.memory import ConversationBufferMemory

import streamlit as st

# Set the API key for OpenAI
try:
    OpenAI.api_key = get_api_key()
except Exception as e:
    raise Exception(f"Error setting API key for OpenAI: {e}")


# LLMs
llm = OpenAI(temperature=0.9)
chat_model = ChatOpenAI()

############
# Show to the screen
# App Framework
st.title('Boiler Plate:')