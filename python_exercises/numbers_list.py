import random

numbers = [random.randint(1, 100) for _ in range(5)]
print(numbers)

def add_to_list(num):
    numbers.append(num)

num = int(input("Enter number "))
add_to_list(num)

print(numbers)