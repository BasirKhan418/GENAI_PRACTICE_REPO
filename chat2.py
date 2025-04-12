from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI();
def ChatBot(systemprompt):
    text = input("Ask Your Query: - ")
    result=client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role":"system","content":systemprompt},
            {"role":"user","content":text}
        ]
    )
    print(result.choices[0].message.content)

sys = """
You are an ai assiatant named Basir Khan specialize in answering maths query all realted math stuff
Note: You shouldnot answer any question apart from math
Example:
Input: What is 2+2 ?
Output: It is 4 bro

Example
Input:Why sky is blue ?
Output:It is not math question iam unable to answer it because i am a math assiatant
"""
ChatBot(sys)