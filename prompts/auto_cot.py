# ZEro shot prompting

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
 PLAN: { "step":"START": "content": "Hey, can you please solve 2+ 3 * 5 / 10"}
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

message_history = [
    {"role": "system", "content": System_prompt},
]

user_query = input(" tell me your query \n")

print("\n\n\n\n\n")


message_history.append({"role": "user", "content": user_query})


while True:
    response = client.chat.completions.create(
        model="gemini-2.5-flash",
        response_format={"type": "json_object"},
        messages=message_history
    )
    raw_result = (response.choices[0].message.content)
    message_history.append({"role": "assistant", "content": raw_result})
    parsed_result = json.loads(raw_result)

    if parsed_result.get("Step") == "START":
        print("STARTING LLM", parsed_result.get("Content"))
        continue

    if parsed_result.get("Step") == "PLAN":
        print("THINKING", parsed_result.get("Content"))
        continue

    if parsed_result.get("Step") == "OUTPUT":
        print("OUTPUT", parsed_result.get("Content"))
        break
