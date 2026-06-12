from together import Together
import os
from dotenv import load_dotenv
import os
from typing import List, Dict

load_dotenv()

model = os.getenv('TOGETHER_API_MODEL')
max_tokens = os.getenv('TOGETHER_MAX_TOKENS')

# response = client.chat.completions.create(
#     model=model,
#     messages=[
#       {
#         "role": "user",
#         "content": "What is the smallest planet in Solar system?"
#       }
#     ]
# )
# print(response.choices[0].message.content)


def generate_with_single_input(prompt: str,
                               role: str = 'user',
                               top_p: float = None,
                               temperature: float = None,
                              **kwargs):

    payload = {
        "model": model,
        "messages": [{'role': role, 'content': prompt}],
        "max_tokens": max_tokens,
        "reasoning": {"enabled": False},
        **kwargs
    }

    # Only add temperature and top_p if they're not None
    if top_p is not None:
        payload["top_p"] = top_p
    if temperature is not None:
        payload["temperature"] = temperature

    client = Together() # auth defaults to os.environ.get("TOGETHER_API_KEY")

    json_dict = client.chat.completions.create(**payload).model_dump()
#    json_dict['choices'][-1]['message']['role'] = json_dict['choices'][-1]['message']['role'].lower()

    try:
        output_dict = {'role': json_dict['choices'][-1]['message']['role'], 'content': json_dict['choices'][-1]['message']['content']}
    except Exception as e:
        raise Exception(f"Failed to get correct output dict. Please try again. Error: {e}")
    return output_dict

def generate_with_multiple_input(messages: List[Dict],
                               top_p: float = None,
                               temperature: float = None,
                                **kwargs):

    payload = {
        "model": model,
        "messages": messages,
        "max_tokens": max_tokens,
        "reasoning": {"enabled": False},
        **kwargs
    }

    # Remove None parameters for Together API
    if top_p is not None:
        payload["top_p"] = top_p        
    if temperature is not None:
        payload["temperature"] = temperature

    client = Together() # auth defaults to os.environ.get("TOGETHER_API_KEY")
    json_dict = client.chat.completions.create(**payload).model_dump()
    json_dict['choices'][-1]['message']['role'] = json_dict['choices'][-1]['message']['role'].lower()

    try:
        output_dict = {'role': json_dict['choices'][-1]['message']['role'], 'content': json_dict['choices'][-1]['message']['content']}
    except Exception as e:
        raise Exception(f"Failed to get correct output dict. Please try again. Error: {e}")
    return output_dict
