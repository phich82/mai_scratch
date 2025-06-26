thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue", {"a": 1}],
  "name": {"Snowy":"beautiful"}
}
print(thisdict)
print(type(thisdict["brand"]))
print(type(thisdict["colors"]))
print(thisdict["colors"][1])
print(type(thisdict["colors"][3]))
print(thisdict["colors"][3])
print(thisdict["colors"][3]["a"])
print(type(thisdict["year"]))
print(type(thisdict["electric"]))
print(type(thisdict["name"]))
print(thisdict["name"]["Snowy"])

