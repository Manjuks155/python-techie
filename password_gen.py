import random

alpha_count = int(input("Enter the number of letters needed for password : "))
special_count = int(input("Enter the number of special characters needed for password : "))
numbers_count = int(input("Enter the number of numbers needed for password : "))

alpha_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
              'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
              'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
special_list = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']
numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

password_list = []
for i in range(1, alpha_count+1):
    password_list += random.choice(alpha_list)

for i in range(1, special_count+1):
    password_list += random.choice(special_list)

for i in range(numbers_count):
    password_list += str(random.choice(numbers_list))

print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
    password += char

print(password)


