thisset = {"apple", "banana", "cherry"}
print(thisset)

thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)

thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset)

thisset = {"apple", "banana", "cherry", False, True, 0}

print(thisset)

thisset = {"apple", "banana", "cherry"}

print(len(thisset))

myset = {"apple", "banana", "cherry"}

print(type(myset))


thisset = set(("apple", "banana", "cherry", "cherry"))
print(thisset)
thisset = set(["apple", "banana", "cherry", "apple"])
print(thisset)
# Note: the set list is unordered, so the result will display the items in a random order.