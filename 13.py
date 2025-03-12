import json

# Read the JSON file
with open('C:\Users\sanja\Downloads\test.json') as file:
    data = json.load(file)

# Extract keys and values
keys = data.keys()
values = data.values()

# Print keys and values
print("Keys:")
for key in keys:
    print(key)

print("Values:")
for value in values:
    print(value)
