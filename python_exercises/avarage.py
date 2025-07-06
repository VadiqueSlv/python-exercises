n = int(input("How much elements? "))
numbers = []

for i in range(n):
    num = int(input(f"Enter element {i + 1}: "))
    numbers.append(num)

def is_prime(n):
    average = sum(numbers) / len(numbers)
    print(average)