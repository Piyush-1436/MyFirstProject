d = {}   # This is an empty dictionary
info = {
    "name": "Piyush",
    "age" : 19,
    "city": "kalyan",
}
print(info , type(info))
print(info["name"])
print(info["age"]) 
print(info["Piyush1"])      # Returns an error since Piyush1 is not in the dictionary
print(info.get("Piyush1"))  # Prints NONE if the key is not in the dictionary
