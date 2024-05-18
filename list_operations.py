# list is mutable
list_example = [2, 5, 10, 9, 8, 3, 0, 1, 7, 2, 12]
empty_list = []
empty_list = list()
print("type of a empty list : " + str(type(empty_list)))

print(f"count is : {list_example.count(200)}")
print("Manju".count('a'))

# num_list
num_list = [2, 5, 10, 9, 8, 3, 0, 1, 7, 2, 12]
print(num_list)

# name_list
name_list = ['Java', 'Python', 'JavaScript', 'Angular', 'AWS', 'Lambda']
print(name_list)

# mix_dataType_list
mix_datatype_list = [1, "Java", 10.12, 'AWS', True, 2 + 3j]
print(mix_datatype_list)

d = 'g'
print(type(d))

z = 4 + 5j
print(type(z))

# accessing
print(num_list[1])
# IndexError: list index out of range
# print(num_list[126])

# negative index
print(num_list[-2])
# IndexError: list index out of range
# print(num_list[-20])

# slicing
# list[start:stop:step]
print(num_list[5:7])
print(num_list[0:200])
print(num_list[-4:-2])

# extended slicing
print(num_list[2:7:1])
print(num_list[2:7:2])

# sort
num_list.sort()
print(num_list)

# sort on mix list
# TypeError: '<' not supported between instances of 'str' and 'int'
# mix_datatype_list.sort()
# print(mix_datatype_list)

# sorted returns a new list and original list will be unaltered
name = sorted(name_list, reverse=True)
print("list sort using sorted() method : " + str(name))

# sort() return type - None
return_type = num_list.sort()
print(return_type)

# reverse
num_list.reverse()
# num_list.sort()
print(num_list)

# append at end
num_list.append("Manju")
print(num_list)

print("Appending a list to list")
name1_list = ["scalar", "javabrains", "decode", "codechef"]
print("Before append on name list : " + str(name_list))
name_list.append(name1_list)
print("After append on name list : " + str(name_list))
name_list.extend(name1_list)
print("After the extend on name list : " + str(name_list))

# append at specific index - insert
num_list.insert(2, 200)
print(num_list)

# extend() -
num_list.extend("Car")
num_list.extend(["Java", 'Python', 'AWS'])
print(num_list)

# update - at specific index
num_list[0] = "Zero"
print(num_list)

# remove - Remove the element from list
num_list.remove(10)
print(num_list)

num_list.remove("Zero")
print(num_list)

if num_list.count("Nothing") != 0:
    num_list.remove("Nothing")
print(num_list)

val = num_list.remove(0)
print("return val of remove : " + str(val))
print(num_list)

# pop,
val = num_list.pop()
print(val)
print(num_list)

# pop and return the element
# pop based on index
zero_index_rem = num_list.pop(0)
print("Value removed at zero index : " + str(zero_index_rem))
print(num_list)
