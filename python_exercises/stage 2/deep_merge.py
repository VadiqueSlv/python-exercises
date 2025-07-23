def deep_merge(dict1, dict2):
    result = dict1.copy()

    for key, value in dict2.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = deep_merge(result[key], value)
        else:
            result[key] = value

    return result

a = {
    "user": {
        "name": "A",
        "info": {
            "age": 1
        }
    }
}

b = {
    "user": {
        "info": {
            "age": 2,
        }
    },
}

merged = deep_merge(a, b)
print(merged)