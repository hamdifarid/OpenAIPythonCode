import os
import openai #pip install openai

openai.api_key = "YOUR API KEY"
while True:
    x = input("Ask me")
    prompt = x

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
)
    print(response.choices[0].text)
