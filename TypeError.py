name = input("what is your name ? ")
print(name)

length = len(name)
# TypeError: can only concatenate str (not "int") to str
# print("Length of the name " + name + " : " + length)
print("Length of the name " + name + " : " + str(length))

name = "Rahul Dravid"
print(name)

length = len(name)
# TypeError: can only concatenate str (not "int") to str
print("Length of the name " + name + " : " + length)
# print("Length of the name " + name + " : " + str(length))