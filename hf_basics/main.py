from transformers import pipeline

pipe = pipeline("image-text-to-text", model="google/gemma-3-4b-it")


input = input("Please enter your query \n")

messages = [
    {
        "role": "user",
        "content": [
            {"type": "image", "url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR1MOJMolRlLkyKGx6MhrPfAD-EhxtOsIEMgQ&s"},
            {"type": "text", "text": input}
        ]
    },
]
result = pipe(messages)
print(result[0]["generated_text"][1]["content"])
