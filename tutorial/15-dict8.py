thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
# 1. for ... in ... ---> loop (key)
for key in thisdict:
  print(f'Key: {key}')
  
  thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
# Loop (key)
for key in thisdict:
  print(f'Key: {key} - Value: {thisdict[key]}')
  
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
# 2. Only loop values of dictionary
for value in thisdict.values():
  print(f'Value (thisdict.values(): {value}')
  
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
# 3. Only loop keys of dictionary
for key in thisdict.keys():
  print(f'Key: (thisdict.keys(): {(key)}')

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
# 4. Loop (key, value)
for key, value in thisdict.items():
  print(key, value)