from fileinput import FileInput

with FileInput(["name.txt", "numbers.txt"]) as input_lines:
    with open("name+numbers", "w") as output_file:
        output_file.writelines(input_lines)
