
import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()

# Retrieve the OpenAI API key from environment variables
def get_OpenAI():
    openAI_api_key = os.getenv("OPENAI_API_KEY")
    if not openAI_api_key:
        raise EnvironmentError("No OpenAI API key found. "
                               "Please check your .env file.")
    return openAI_api_key

# Retrieve the NewsApi.org API key from environment variables
def get_NewsAPIKey():
    news_api_key = os.getenv("NEWS_API_KEY")
    if not news_api_key:
        raise EnvironmentError("No NEWS_API_KEY found. "
                               "Please check your .env file.")
    return news_api_key

# Retrieve the OpenWeather API key from environment variables
def get_OpenWeatherAPIKey():
    openWeather_api_key = os.getenv("OPENWEATHERMAP_API_KEY")
    if not openWeather_api_key:
        raise EnvironmentError("No OpenWeather_API_KEY found. "
                               "Please check your .env file.")
    return openWeather_api_key


