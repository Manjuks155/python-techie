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
# print("Length of the name " + name + " : " + length)
print("Length of the name " + name + " : " + str(length))

animal = "lion"
print(len(animal))
print(len("ab"))
print(len(""))

# TypeError: len() takes exactly one argument (0 given)
# print(len())

print("End")

# TypeError: can only concatenate str (not "int") to str
# name="Python"
# print("The length of name " + name + " is " + len(name))


amount=input("what is the value of dollar in rupee : ")
currency='rupees'
print(amount + " " + currency)