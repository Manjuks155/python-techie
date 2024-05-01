# check if the given number is even or odd

# if-else
num = int(input("Enter the number : "))
if num % 2 == 0:
    print(f"{num} is even number")
else:
    print(f"{num} is odd number")

# Nested if-else
height = int(input("Enter the height : "))
if height >= 3:
    print("You can ride")
    age = int(input("Enter your age : "))
    bill = 0
    if age <= 12:
        bill = 150
    elif age <= 18:
        bill = 200
    else:
        bill = 250

    want_photo = input("Do you want to take photos (Y/N) : ")
    if want_photo == 'Y' or want_photo == 'y':
        bill += 50

    print(f"your bill is {bill} rupees")

else:
    print("You can not ride")

print("Thank you for visiting!")
