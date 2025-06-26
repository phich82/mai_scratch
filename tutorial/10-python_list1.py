thislist = ["apple", "banana", "cherry",None]

print(thislist)
print('===> 1. Get value of 4th element/item')
print(thislist[3])
print('===> End')

thislist = ["apple", "banana", "cherry"]

print(thislist)
print('===> 2. Get value of the last element/item')
print(thislist[-1])
print('===> End')

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# thelist[x:y]: x: index, y: nth element/item
# thelist[:y]: x: index=0, y: nth element/item -> thelist[0:y]
# thelist[x:]: x: index, y: last element/item
print(thislist[2:5])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# thelist[-x:-y]: y: index (start from last element: right -> left), x: nth element (start from last element: right -> left)
print(thislist[-4:-1]) # <=> thislist[1:4] start from right to left

thislist = ["apple", "banana", "cherry"]
hasExistInList = "apple" in thislist # bool
hasNotExistInList = "mango" not in thislist # bool
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
if hasExistInList:
    print("Yes, 'apple' is in the fruits list")
if hasNotExistInList:
    print("No,the mango is not in the fruit list")
