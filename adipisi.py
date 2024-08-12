def create_list(values, n):
    return [value for value in values if value <= n]

# Sample run
input_list = [10, 20, 30, 40, 50]
result = create_list(input_list, 25)
print(result)
