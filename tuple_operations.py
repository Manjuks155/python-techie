# tuple is immutable in nature
num_tuple = (20, 5, -8, 3, 18, 25)
name_tuple = ("Java", "Python", "AWS")
mixed_tuple = (2, 6, 4, -7, 'Manju', 10.5, True)
tuple1 = (10)  # <class 'int'>     # Invalid tuple
tuple2 = (20,)  # valid tuple
tuple3 = ()  # Empty tuple   # valid

empty_tuple = ()
empty_tuple = tuple()
print("type of empty tuple : " + str(type(empty_tuple)))

print(type(num_tuple))
print(type(name_tuple))
print(type(mixed_tuple))
print(type(tuple1))
print(type(tuple2))
print(type(tuple3))

# list to tuple
list_ex = [10, -5, 2, 7, 8, True, 'Python']
print(list_ex)
tuple_ex = tuple(list_ex)
print("list to tuple : ")
print(tuple_ex)

list_t = list(tuple_ex)
print("tuple to list : ")
print(list_t)
