#!/usr/bin/env python3
# -*- coding: utf-8 -*-


openai.api_key = os.getenv("CHATGPT_API_KEY")  # Reads the API key from the environment variable

def get_completion(prompt, model="gpt-4o-mini"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,
    )
    return response.choices[0].message["content"]

# Create the prompt
prompt = f"""
sing daisy daisy from 2001 a space oddicy, but slow it down like hal does,
add like a bunch of letters not a -
"""

# Call the function and print the response
response = get_completion(prompt)
print(response)
import openai
import os
import pandas as pd
import time

openai.api_key = os.getenv("CHATGPT_API_KEY")  # Reads the API key from the environment variable

def get_completion(prompt, model="gpt-4o-mini"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,
    )
    return response.choices[0].message["content"]

# Create the prompt
prompt = f"""
sing daisy daisy from 2001 a space oddicy, but slow it down like hal does,
add like a bunch of letters not a -
"""

# Call the function and print the response
response = get_completion(prompt)
print(response)
