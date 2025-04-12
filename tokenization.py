import tiktoken
encoder = tiktoken.encoding_for_model("gpt-4o")

print(encoder.n_vocab)
text = "the text is the cat sat on the mat"
tokens=  encoder.encode(text)
print(tokens)

my_tokens = [3086, 2201, 382, 290, 9059, 10139, 402, 290, 2450]

print(encoder.decode(my_tokens))
