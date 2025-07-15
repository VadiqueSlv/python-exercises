import json

def invert_dict(d):
    return {value: key for key, value in d.items()}

raw_data = input('Enter dictionary JSON (example {"a":1, "b":2}): ')
data = json.loads(raw_data)

inverted = invert_dict(data)
print(inverted){"a":1, "b":2}