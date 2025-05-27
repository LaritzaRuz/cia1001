from openai import OpenAI
import os
import pandas as pd
import time

client = OpenAI(api_key=os.getenv("CHATGPT_API_KEY"))

def get_completion(prompt, model="gpt-4o-mini"):
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=0,
    )
    return response.choices[0].message.content

# Create the prompt
prompt = """Sing 'Daisy Bell' (also known as 'Daisy, Daisy' or 'A Bicycle Built for Two') 
in the style of HAL 9000 from '2001: A Space Odyssey', with gradually slowing tempo 
and deteriorating pronunciation, similar to HAL's famous death scene."""

# Call the function and print the response
response = get_completion(prompt)
print(response)
