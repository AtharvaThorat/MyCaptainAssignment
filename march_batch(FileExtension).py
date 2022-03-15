Filename = input("Input the Filename: ")
File_Extension = Filename.split(".")
# [-1] corresponds to the last index, in order to get the extension
print("The extension of the file is: ", (File_Extension[-1]))
