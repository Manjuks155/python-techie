langs = {"Java", 'python', "AWS", "SQL"}
langs.update((1, 2, 3))

for i in langs:
    print(i)

numbers = [5, 4, -2, 8, 10]
squares_numbers = []
squares_numbers = list()
print(type(numbers))
print(type(squares_numbers))
for i in numbers:
    squares_numbers.append(i ** 2)

print(squares_numbers)

numbers_set = {5, 4, -2, 8, 10}
squares_set = set()
print("type of the set : " + str(type(squares_set)))
for num in numbers_set:
    squares_set.add(num ** 2)

print("squares of the set : " + str(squares_set))

