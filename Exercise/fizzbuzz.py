num = int(input('Enter the number:'))
if num % 2 == 0:
    print(f"{num} is even")
else:
    print(f"{num} is odd")

# 3 - fizz
# 5 - buzz
# 3 & 5 - fizzbuzz

for i in range(16):
    if i % 3 == 0 and i % 5 == 0:
        print("fizzbuzz")
    elif i % 3 == 0:
        print("fizz")
    elif i % 5 == 0:
        print('buzz')
    else:
        print(i)
