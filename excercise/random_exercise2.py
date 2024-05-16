import random

# Pay bill randomly
# Manju, Nischala, Darshan, Arun

# Method-1
names = input("Enter the name with comma separated : ")
names_list = names.split(", ")
names_list_len = len(names_list)
rand_num = random.randint(0, names_list_len - 1)
name_selected = names_list[rand_num]

print(f"{name_selected} will pay the bill")


names =  input("Enter the names with comma separated : ")
names_list = names.split(", ")
person_selected = random.choice(names_list)
print(f"{person_selected} will pay the bill")



