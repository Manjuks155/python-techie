name = "krishna"
age = 30
height = 1.7

# TypeError: can only concatenate str (not "int") to str
# print("My name is : " + name + ", age is : " + age + " and height is : " + height)

# type cast
print("My name is : " + name + ", age is : " + str(age) + " and height is : " + str(height) + " meters")

# concatenation using comma
print("My name is :", name, ",age is :", str(age), "and height is :", str(height), " meters")

# f-string example
print(f"My name is : {name}, age is : {age} and height is : {height} meters")
