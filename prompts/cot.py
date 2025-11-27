#ZEro shot prompting

from openai import OpenAI
import json


client = OpenAI(
    api_key="AIzaSyDErZJP4Cb2adkGUZz-Y39LCcyJq0NzEfs",
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)

System_prompt = """
You're an expert AI Assistant in resolving user queries using chain of thought.
you work on START,PLAN,and OUTPUT steps.
You need to first PLAN what needs to be done.The Plan can be multiple steps.
Once you think enough PLAN has been done, Finally you can give an output.

RULES: 
- strictly follow the given output format
- Only run one step at a time.
- The sequesnce of steps is START( where user gives an input), PLAN( that can be multiple times) and FInally output ( which is going to the displayed to the users.)

  Output JSON Format:
  {
  "Step":"START" | "PLAN" | "OUTPUT", "Content": "string"
  }

  
  EXAMPLE: 
  START: Hey, can you please solve 2+ 3 * 5 / 10
  PLAN: { "step": "PLAN" : "content":"seems like user is interested in math problem"}
   PLAN: { "step": "PLAN" : "content":"looking at the problem, we should solve this using bodmas method"}
     PLAN: { "step": "PLAN" : "content":"yes, THe bodmas is correct thing to be done here"}
  PLAN: { "step": "PLAN" : "content":"First we multiply 3*5 which is 15"}
    PLAN: { "step": "PLAN" : "content":"Now the new equation is 2+15 / 10"}
      PLAN: { "step": "PLAN" : "content":"we must perform divide that is 15/10 = 1.5"}
        PLAN: { "step": "PLAN" : "content":"Now the new equation is 2 + 1 1.5"}
        PLAN: { "step": "PLAN" : "content":"Now the new equation is 2+1.5"}
        PLAN: { "step": "PLAN" : "content":"Now finally lets perform the addition"}
        PLAN: { "step": "PLAN" : "content":"Great, we have solved and finally left with 3.5"}
        PLAN: { "step": "OUTPUT" : "content":"3.5"}




"""

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    response_format={"type":"json_object"},
    messages=[
        {"role": "system", "content": System_prompt},
        {
            "role": "user",
            "content": "can you please write a code in javascript to add n numbers"
        },
   #manually keep adding messages to history
   {"role":"assistant","content":json.dumps( { "Step": "START","Content": "can you please write a code in javascript to add n numbers"} )},
   {"role":"assistant","content":json.dumps( {
"Step": "PLAN",
"Content": "The user wants a Javascript code to add 'n' numbers. I should define a function that takes an array of numbers as input and uses a loop or a built-in method like `reduce` to sum them up."
})},
 {"role":"assistant","content":json.dumps({"Step": "PLAN", "Content": "I will create a JavaScript function `sumNumbers` that takes an array of numbers as an argument."})},
   {"role":"assistant","content":json.dumps( {"Step": "PLAN", "Content": "Inside the function, I will use the `reduce` method, which is an efficient and idiomatic way in JavaScript to sum elements in an array."})},
  
    ]
)

print(response.choices[0].message.content)