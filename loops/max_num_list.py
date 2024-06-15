numbers = input("Enter the numbers with space:\n")
numbers_list = numbers.split()
count = 0

for num in numbers_list:
    count += 1

max = 0
for i in range(0, count):
    val = int(numbers_list[i])
    numbers_list[i] = val
    if val > max:
        max = val

print("Max value is : " + str(max))
print(numbers_list)

# 3 43 65 2 3
