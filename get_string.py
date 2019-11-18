def get_string(file_name):
    result = None
    try:
        with open(file_name, "rt") as f:
            result = f.read()
    except FileNotFoundError as e:
        print("FileNotFoundError: ", e)
    return result