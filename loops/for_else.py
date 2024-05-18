numbers = [20, 345, 6, 7, 4, -8]
num_list = list()
for num in numbers:
    num_list.append(num)

print("list to tuple: " + str(type(tuple(num_list))))
print("list to tuple: " + str(tuple(num_list)))
