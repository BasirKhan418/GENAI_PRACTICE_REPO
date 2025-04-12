from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

client = OpenAI()

result  = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
            "role": "user",
            "content": "Hello, how are you?"
        }
    ]
)

print(result.choices[0].message.content)