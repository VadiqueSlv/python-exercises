def sum_to_n():
    n = int(input("Enter number "))
    total = 0
    for i in range(1, n + 1):
        total += i
    print(total)

sum_to_n()
