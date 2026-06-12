from common import generate_with_multiple_input, generate_with_single_input

print('Testing generate_with_single_input')
output = generate_with_single_input(
    prompt="What is the capital of France?"
)

print("Role:", output['role'])
print("Content:", output['content'])

messages = [
    {'role': 'user', 'content': 'Hello, who won the FIFA world cup in 2018?'},
    {'role': 'assistant', 'content': 'France won the 2018 FIFA World Cup.'},
    {'role': 'user', 'content': 'Who was the captain?'}
]

print('Testing generate with multiple inputs')
output = generate_with_multiple_input(
    messages=messages,
    max_tokens=100
)

print("Role:", output['role'])
print("Content:", output['content'])