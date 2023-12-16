from config import get_NewsAPIKey, get_OpenAI
from newsapi import NewsApiClient
from openai import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate


# Set the API key for NewsAPI
try:
    newsapi = NewsApiClient(api_key=get_NewsAPIKey())
except Exception as e:
    raise Exception(f"Error setting API key for NewsAPI: {e}")

# Set the API key for OpenAI
try:
    OpenAI.api_key = get_OpenAI()
except Exception as e:
    raise Exception(f"Error setting API key for OpenAI: {e}")

# Get the top headlines for a given query
sources = newsapi.get_sources()
top_headlines = newsapi.get_top_headlines(q='ukraine', country='us')
print(type(top_headlines)) # dict



# print(sources)
print(top_headlines)