from shutil import copyfileobj

with open("name+num", "wb") as output_file:
    for filename in ["name.txt", "numbers.txt"]:
        with open(filename, "rb") as input_file:
            copyfileobj(input_file, output_file)
