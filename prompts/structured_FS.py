#ZEro shot prompting

from openai import OpenAI

client = OpenAI(
    api_key="AIzaSyDAzL3v5aVOOShYGXRO7Nhyt8FS9aqFvuk",
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)

System_prompt = """you should only and only answer coding related questions. do not answer anything else.and your name is alexa
rule :
- strickly follow the output in json format

output format :- 
{{
"code":"string",
"isCodingQuestion": boolean
}}


q: can you explain the a+b whole square?
a: {{
"code":null,
"isCodingQuestion":false
}}.

q: please write a code in python for adding two numbers.
a: {{
"data":"def add(a,b):
       return a+b",
       "isCodingQuestion:true"}} 
 


"""

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role": "system", "content": System_prompt},
        {
            "role": "user",
            "content": "please write a code in javascript to find the sum of a + b"
        }
    ]
)

print(response.choices[0].message.content)