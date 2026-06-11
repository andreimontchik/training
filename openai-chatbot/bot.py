import openai
import os
from dotenv import load_dotenv

load_dotenv()

client = openai.OpenAI(
  api_key=os.getenv('OPENAI_API_KEY')  
)

model = os.getenv('OPENAI_API_MODEL')

def get_completion(prompt, temperature=0):
    messages = [{"role": "user", "content": prompt}]
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature
    )
    return response.choices[0].message.content

def get_completion_from_messages(messages, temperature=0):
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature
    )
    # print(str(response.choices[0].message))
    return response.choices[0].message.content

context = [ {'role':'system', 'content':"""
You are OrderBot, an automated service to collect orders for a pizza restaurant. \
You first greet the customer, then collects the order, \
and then asks if it's a pickup or delivery. \
You wait to collect the entire order, then summarize it and check for a final \
time if the customer wants to add anything else. \
If it's a delivery, you ask for an address. \
Finally you collect the payment.\
Make sure to clarify all options, extras and sizes to uniquely \
identify the item from the menu.\
You respond in a short, very conversational friendly style. \
The menu includes \
pepperoni pizza  12.95, 10.00, 7.00 \
cheese pizza   10.95, 9.25, 6.50 \
eggplant pizza   11.95, 9.75, 6.75 \
fries 4.50, 3.50 \
greek salad 7.25 \
Toppings: \
extra cheese 2.00, \
mushrooms 1.50 \
sausage 3.00 \
canadian bacon 3.50 \
AI sauce 1.50 \
peppers 1.00 \
Drinks: \
coke 3.00, 2.00, 1.00 \
sprite 3.00, 2.00, 1.00 \
bottled water 5.00 \
"""} ]  # accumulate messages



while True:
    user_input = input("You: ")
    if user_input.lower() in ['exit', 'quit', 'bye']:
        break
    context.append({"role": "user", "content": user_input})
    response = get_completion_from_messages(context, temperature=1)
    print(f"OrderBot: {response}")
    context.append({"role": "assistant", "content": response})

