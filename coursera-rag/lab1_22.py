from common import generate_with_single_input


house_data = [
    {
        "address": "123 Maple Street",
        "city": "Springfield",
        "state": "IL",
        "zip": "62701",
        "bedrooms": 3,
        "bathrooms": 2,
        "square_feet": 1500,
        "price": 230000,
        "year_built": 1998
    },
    {
        "address": "456 Elm Avenue",
        "city": "Shelbyville",
        "state": "TN",
        "zip": "37160",
        "bedrooms": 4,
        "bathrooms": 3,
        "square_feet": 2500,
        "price": 320000,
        "year_built": 2005
    }
]

# First, let's create a layout for the houses

def house_info_layout(houses):
    layout = ''
    # Iterate over the houses
    for house in houses:
        # For each house, append the information to the string using f-strings
        # The following way using brackets is a good way to make the code readable as in each line you can start a new f-string that will appended to the previous one
        layout += (f"House located at {house['address']}, {house['city']}, {house['state']} {house['zip']} with "
            f"{house['bedrooms']} bedrooms, {house['bathrooms']} bathrooms, "
            f"{house['square_feet']} sq ft area, priced at ${house['price']}, "
            f"built in {house['year_built']}.\n") # Don't forget the new line character at the end!
    return layout

# Check the layout
print(house_info_layout(house_data))

def generate_prompt(query, houses):
    # The code made above is modular enough to accept any list of houses, so you could also choose a subset of the dataset.
    # This might be useful in a more complex context where you want to give only some information to the LLM and not the entire data
    houses_layout = house_info_layout(houses)
    # Create a hard-coded prompt. You can use three double quotes (") in this cases, so you don't need to worry too much about using single or double quotes and breaking the code
    PROMPT = f"""
Use the following houses information to answer users queries.
{houses_layout}
Query: {query}    
             """
    return PROMPT

print(generate_prompt("What is the most expensive house?", houses = house_data))

query = "What is the most expensive house? And the bigger one?"

print('Query without house')
# Asking without the augmented prompt, let's pass the role as user
query_without_house_info = generate_with_single_input(prompt = query, role = 'user')
print(query_without_house_info['content'])

print('Query with house')
# With house info, given the prompt structure, let's pass the role as assistant
enhanced_query = generate_prompt(query, houses = house_data)
query_with_house_info = generate_with_single_input(prompt = enhanced_query, role = 'assistant')
print(query_with_house_info['content'])