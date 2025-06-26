# 1. String Type
x = "3"
print('===> 1. String Type')
print(x)
print(type(x))

# 2. Set Type
x = frozenset({"apple", "banana", "cherry"})
print('===> 2. Set Type (frozenset)')
print(x)
# x.union({"apple2", "banana2", "cherry2"})
# print(x)
print(type(x))
# Total of elements in set
print(len(x))
# Print first element in set
my_set = {3, 1, 4, 1, 5, 9, 2}
first_element = next(iter(my_set))
print(first_element)
# Print last element in set


x = {"apple", "banana", "cherry"}
print('===> 2. Set Type (set)')
print(x)
x.add('mango')
x.add('mango')
print(x)
print(type(x))

# 3. None Type
x = None
print('===> 3. None Type')
print(x)
print(type(x))

# 4. Numberic Types (int, float, complex)
# 4.1 int type
x = 20
print('===> 4. Numberic Type (int)')
print(x)
print(type(x))
# 4.2 float type
x = 20.5
print('===> 4. Numberic Type')
print(x)
print(type(x))
# 4.3 complex type (a + bj: a real part, b: imagination part, j: imagination unit, square root of -1)
x = 1j # a=0, b=1
x = -1 + 1j
x = 2.6 + 1.8j
print('===> 4. Numberic Type')
print(x)
print(type(x))

# 5. Boolean Type
x = True
print('===> Boolean Type')
print(x)
print(type(x))

# 6. Sequence Type
x = ["apple","banana","cherry"]
print('===> Sequence Type')
print(x)
print(type(x))

x = ("apple","banana","cherry")
print(x)
print(type(x))

x = range(6)
print(x)
print(type(x))

# 7. Mapping Type
x = {"name":"John","age":36}
print('===> Mapping Type')
print(x)
print(type(x))
