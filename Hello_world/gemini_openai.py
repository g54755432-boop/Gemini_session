from openai import OpenAI

client = OpenAI(
    api_key="AIzaSyDAzL3v5aVOOShYGXRO7Nhyt8FS9aqFvuk",
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role": "system", "content": "You are an expert in maths and you can only answer questions related to maths. other questions will be ignored with i'm only expert in maths"},
        {
            "role": "user",
            "content": "tell me how are you"
        }
    ]
)

print(response.choices[0].message.content)