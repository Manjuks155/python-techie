val_1=12345
val_2="Python"
val_3=True
# NameError: name 'true' is not defined. Did you mean: 'True'?
# val_3=true

print(type(val_1))
print(type(val_2))
print(type(val_3))

a=1
b=2
check = a<b
print(check)
check = a>b
print(check)

number=input("Enter two digit number : ")
num_one=int(number[0])  # type-casting / type-conversion
num_two=int(number[1])

print(num_one + num_two)

# int to str conversion
num_1=25
print(str(num_1)) # 25

# str to int conversion
str_1="055"
print(int(str_1)) # 55

# ValueError: invalid literal for int() with base 10: 'Python'
# str_2="Python"
# print(int(str_2))
