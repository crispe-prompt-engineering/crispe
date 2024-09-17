import utils
import os, re, random
from openai import AzureOpenAI
from collections import Counter

all_responses = []
def ccp_chatgpt_interaction(prompt_path, max_iterations=10):
    client = AzureOpenAI(
        api_key="<OPENAI KEY>",
        api_version="<OPENAI VERSION>",
        azure_endpoint="<OPENAI ENDPOINT>"
    )
    messages = []
    for _ in range(max_iterations):
        user_prompt = utils.read_code(prompt_path)
        messages = [{'role': 'user', 'content': user_prompt}]
        response = client.chat.completions.create(
            model="gpt-4",
            messages=messages,
            temperature=0.7,
        )
        assistant_response = response.choices[0].message.content
        messages.append({'role': 'assistant', 'content': assistant_response})
    return assistant_response

