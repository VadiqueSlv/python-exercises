def average(numbers):
    average = sum(numbers) / len(numbers)
    return average

n = int(input("How many elements? "))
numbers = []

for i in range(n):
    num = float(input(f"Enter element {i + 1} "))
    numbers.append(num)

average(numbers)