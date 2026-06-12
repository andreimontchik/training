print("Lists")

# Example of a list
l1 = ['RAG', 'is', 'awesome']
print(f"Original list: {l1}")

# Adding an item
l1.append('!')
print(f"List after adding '!': {l1}")

# Removing an item
l1.remove('awesome')
print(f"List after removing 'awesome': {l1}")

# .remove and .append change the list and have no return
result = l1.append("this is a test")
print(result)


print("Lists Comprehensions")
# An example of list comprehension to create a list of squares
squares = [x**2 for x in range(10)]
print(f"Squares of numbers from 0 to 9: {squares} (with list comprehension)")


# The same example using for loop
squares_for_loop = []
for x in range(10):
    squares_for_loop.append(x**2)
print(f"Squares of numbers from 0 to 9: {squares_for_loop} (without list comprehension)")

# Conditional list comprehension
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(f"Squares of even numbers from 0 to 9: {even_squares} (with list comprehension)")

# Without list comprehension
even_squares_for_loop = []
for x in range(10):
    if x % 2 == 0:
        even_squares_for_loop.append(x**2)
print(f"Squares of even numbers from 0 to 9: {even_squares_for_loop} (without list comprehension)")

print("Dictionaries")
# Example of a dictionary
person = {
    'name': 'Alice',
    'age': 25,
    'city': 'New York'
}
print(f"Person dictionary: {person}")

# Accessing a value
print(f"Name: {person['name']}")

# Adding a new key-value pair
person['email'] = 'alice@example.com'
print(f"Updated person dictionary: {person}")

for key, value in person.items():
    print(f"Key: {key}\tValue: {value}")

for val in person:
    print(val)

print("f-strings")
# Basic f-string example
name = "John"
age = 30
greeting = f"Hello, {name}. You are {age} years old."
print(greeting)

# A list of dictionaries - this structure will come up a lot in this course!
people = [
    {
        "name": "Alice Johnson",
        "age": 28,
        "email": "alice.johnson@example.com",
        "location": "New York, NY"
    },
    {
        "name": "Michael Smith",
        "age": 34,
        "email": "michael.smith@example.com",
        "location": "Los Angeles, CA"
    },
    {
        "name": "Emily Davis",
        "age": 22,
        "email": "emily.davis@example.com",
        "location": "Austin, TX"
    },
    {
        "name": "John Brown",
        "age": 45,
        "email": "john.brown@example.com",
        "location": "Chicago, IL"
    },
    {
        "name": "Sarah Wilson",
        "age": 31,
        "email": "sarah.wilson@example.com",
        "location": "Seattle, WA"
    }
]

# First, create an empty list to store the sentences:
t = []
# Iterate over the list of dictionary
for person_info_dict in people:
    # person_info_dict is a dict and you can access its values using the keys
    layout_string = f"Name: {person_info_dict['name']}, Age: {person_info_dict['age']}, E-mail: {person_info_dict['email']}, Location: {person_info_dict['location']}"
    # Append the string with the desired information into the list
    t.append(layout_string) # Add a new line character at the end
# Create the result layout by using the .join method
# The .join function concatenates every string in the list 't', separated by the specified delimiter. Here, each element of 't' is joined using the newline character '\n'.print(formatted_string)
formatted_string = "\n".join(t) 
print(formatted_string)

# Another way of creating strings that depend on parameters is the following:
template = "Name: {name}, Age: {age}, E-mail: {email}, Location: {location}"
t = []
for person_info_dict in people:
    # person_info_dict is a dict and you can access its values using the keys
    # Append the string with a new information using the .format method
    layout_string = template.format(name = person_info_dict['name'], 
                         age = person_info_dict['age'], 
                         email = person_info_dict['email'], 
                         location = person_info_dict['location'])
    t.append(layout_string)
formatted_string = "\n".join(t)
print(formatted_string)