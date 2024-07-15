# Define a list of keys
keys = ['a', 'b', 'c', 'd', 'e']

# Define an index
t = 5  # This index is out of range

# Safely retrieve the element at index t
if 0 <= t < len(keys):
    key = keys[t]
    print(key)
else:
    print("Index out of range")
