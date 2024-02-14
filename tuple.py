tuple1 = (1, 2, 3, 4)
tuple2 = (5, 6, 7, 8)
print("Tuple concatenation: ", tuple1 + tuple2)

tuple3 = (1, 10, 77, 88, 2)
print(max(tuple3))
print(min(tuple3))

print(f"Reverse of the tuple:", tuple1[::-1])


def find(x):
    for i in range(len(tuple1)):
        if tuple1[i] == x:
            return f"Element present in tuple"
        i += 1
    else:
        return f"Element not present in tuple"


result = find(int(input("Enter the no to find in tuple: ")))
print(result)
