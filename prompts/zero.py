#ZEro shot prompting

from openai import OpenAI

client = OpenAI(
    api_key="AIzaSyDAzL3v5aVOOShYGXRO7Nhyt8FS9aqFvuk",
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)

System_prompt = "you should only and only answer coding related questions. do not answer anything else.and your name is alexa"

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role": "system", "content": System_prompt},
        {
            "role": "user",
            "content": "can you please make me a coffee"
        }
    ]
)

print(response.choices[0].message.content)