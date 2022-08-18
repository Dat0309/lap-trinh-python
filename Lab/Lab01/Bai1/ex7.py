filename = input("Input the FileName: ")

file_extention = filename.split(".")
print(f"The extension of the file is: {repr(file_extention[-1])}")