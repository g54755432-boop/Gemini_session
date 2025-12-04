from openai import OpenAI
from dotenv import load_dotenv
import requests

load_dotenv()

client = OpenAI(
    api_key="AIzaSyDErZJP4Cb2adkGUZz-Y39LCcyJq0NzEfs",
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)


def get_weather(city: str):
    url = f"https://wttr.in/{city.lower()}?format=%C+%t"
    response = requests.get(url)

    if response.status_code == 200:
        return f"The weather in {city} is {response.text}"

    return "Something went wrong"


def Main():
    user_query = input("> ")
    response = client.chat.completions.create(
        model="gemini-2.5-flash",
        messages=[
            {"role": "user", "content": user_query}
        ]
    )
    print(f"output: {response.choices[0].message.content}")


# Main()
print(get_weather("goa"))
