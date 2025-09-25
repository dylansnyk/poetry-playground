from openai import OpenAI

client = OpenAI()

def get_completion(message):
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": message}
        ]
    )

    return response.choices[0].message.content
