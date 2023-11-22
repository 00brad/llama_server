from openai import OpenAI

client = OpenAI(
    api_key="none",
    base_url="http://localhost"
)

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content":
            '''
            Name 3 excellent science fiction movies.
            '''
         }
    ]
)

print(completion)
