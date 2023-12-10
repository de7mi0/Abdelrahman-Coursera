def calculate_total(a, b):  # Parameters: a and b
    total = a + b  # Task: Addition
    return total  # Output: Sum of a and b


result = calculate_total(5, 7)  # Calling the function with inputs 5 and 7
print(result)  # Output: 12

def greet(name):
    print(f"Hello, {name}")

result = greet("Alice")
print(result)

def print_numbers(limit):
    for i in range(1, limit+1):
        print(i)
print_numbers(5)  # Output: 1 2 3 4 5


def greet(name):
    return "Hello, " + name

for _ in range(3):
    print(greet("Alice"))


my_list = []
def add_element(data_structure, element):
    data_structure.append(element)

def remove_element(data_structure, element):
    if element in data_structure:
        data_structure.remove(element)
    else:
        print(f"{element} not found in the list.")

add_element(my_list, 42)
add_element(my_list, 17)
add_element(my_list, 99)

print("Current list:", my_list)

remove_element(my_list, 17)
remove_element(my_list, 55)
print("Updated list:", my_list)