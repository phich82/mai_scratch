thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(f'thisdict: {thisdict}')
# 1. Delete a item (key, value)
thisdict.pop("model")
print(f'thisdict after deleting `model` key from thisdict via pop(): {thisdict}')

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(f'thisdict: {thisdict}')
# 2. Delete the last item
thisdict.popitem()
print(f'thisdict after deleting last item from thisdict via popitem() {thisdict}')

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(f'thisdict: {thisdict}')
# Delete key a item (model)
del thisdict["model"]
print(f'thisdict after deleting `model` key from thisdict via del thisdict[key]: {thisdict}')

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
# Clear all the item in dictionary
thisdict.clear()
print(f'thisdict after deleting all item from thisdict via clear(): {thisdict}')