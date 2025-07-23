def sum_to_n(n):   
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

n = int(input("Enter number "))
print(sum_to_n(n))