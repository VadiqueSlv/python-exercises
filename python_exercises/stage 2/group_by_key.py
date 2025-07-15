import json

def group_by_key(data, key):
    grouped = {}
    for item in data:
        value = item.get(key)
        if value not in grouped:
            grouped[value] = []
        grouped[value].append(item)
    return grouped

raw_data = input("Enter dictionary JSON (example [{'a':1}, {'a':2}]): ")
data = json.loads(raw_data)

key = input("Enter key: ")

print(group_by_key(data, key))