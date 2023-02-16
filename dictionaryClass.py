thisDict = {
    "brand":"ford",
    "model":"Mustang",
    "year": 1964,
    # "year": 8970 # if there is 2 duplicate items, it'll read the latest item.
}
# # print all items in Dictionary
# print(thisDict)

# # print specific items in dictionary
# print(thisDict["model"])

# # to get item in dictionary
# print(thisDict.get("brand"))

# # to add item in dictionary
# thisDict["color"] = "red"
# print(thisDict)

# # to remove item in dictionary use "var.pop"
# thisDict.pop("model")
# print(thisDict)

# # to delete item in dictionary
# del thisDict["brand"]

# remove last item in dictionary
thisDict.popitem()
print(thisDict)











