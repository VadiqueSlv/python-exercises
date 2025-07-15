def chunker_list(list_numbers, size):
    return list(list_numbers[i::size] for i in range(size))

list_numbers = list(map(int, input("Enter numbers: ").split()))
size = int(input("Enter size: "))

print(chunker_list(list_numbers, size))