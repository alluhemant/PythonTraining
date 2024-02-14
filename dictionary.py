dictionary = {"name": "hemant", "Company": "Genzeon"}

Keys = dictionary.keys()
Values = dictionary.values()
print(dictionary.get(input("Enter the key")))


def find(k):
    for i in range(len(dictionary)):
        if k in dictionary:
            return f"The value for key is:", dictionary.get(k)
        i += 1
    else:
        return "Key", k, "not found in dictionary"


result = find(str(input("Enter the key: ")))
print(result)
