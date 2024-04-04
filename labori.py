try:
    # Code that may raise a FileNotFoundError
except FileNotFoundError as ex:
    # Code to handle the FileNotFoundError
    print(f"The file could not be found: {ex}")
