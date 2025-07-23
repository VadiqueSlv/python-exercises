def more_than(num):
    return "Too much" if num >= 100 else num * num

n = int(input("Enter number "))
print(more_than(n))