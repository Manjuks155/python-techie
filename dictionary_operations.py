# Key - value pair
# Keys should be immutable

dict1 = {'name': 'Manju',
         'age': 29,
         'Programming': 'java'
         }
print(dict1)

for x in dict1:
    print(x)
    print(dict1[x])
    print("--------------------")

print("name is " + dict1["name"])
print("age is " + str(dict1['age']))
dict1['age'] = 30
print("age is " + str(dict1['age']))
print("Programming is " + dict1["Programming"])

dict1['age'] = 30
