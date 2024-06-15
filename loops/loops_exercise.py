heights = input("Enter the person's heights with spaces : \n")
heights_list = heights.split(" ")
heights_list_new = list()
length = 0
sum = 0

for height in heights_list:
    heights_list_new.append(int(height))
    length += 1

print(type(heights_list_new))
print(heights_list_new)
print("Length : " + str(length))

for i in range(length):
    sum += heights_list_new[i]

print(sum)
avg = sum / length
print("avg : " + str((avg)))
