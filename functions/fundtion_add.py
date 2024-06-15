def add(a, b):
    c = a + b
    print(f"sum is {c}")


add(12, 15)
add(12, 10)

add_lists = []
add_lists.append([10, 12])
add_lists.append([11, 13])
add_lists.append([12, 14])
add_lists.append([13, 15])

print("for loop")
for add_list in add_lists:
    add(add_list[0], add_list[1])

print("while loop")
i = 0
while i < len(add_lists):
    add(add_lists[i][0], add_lists[i][1])
    i += 1

