def more_than():
    num = int(input("Enter number "))
    if num >= 100:
        return "Too much"
    else:
        return num * num

print(more_than())