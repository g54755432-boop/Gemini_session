from google import genai

client = genai.Client(
    api_key="AIzaSyDAzL3v5aVOOShYGXRO7Nhyt8FS9aqFvuk"
)

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Explain how AI works in a few words",
)

print(response.text)