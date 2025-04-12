from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

text = "basir is a good developer . He thinks that do you ?"

result  = client.embeddings.create(
    input=text,
    model="text-embedding-3-small"
)

print("Vecto embeddings are:- ",result.data[0].embedding)