greetings = ["hi", 'hello', "welcome"]
names = ['Krishna', "Ram", 'Madhav']

for greeting in greetings:
    for name in names:
        # print(f"{greeting} {name}")
        # print(greeting + " " + name)
        print(greeting, name)
        if greeting == 'hello' and name == 'Ram':
            break
    else:
        print("Inner for else executed")
    if greeting == 'welcome':
        break
else:
    print("outer for else executed")

print("Loop completed")

print("Example for continue")
for i in range(0, 10 + 1, 2):
    if i == 4:
        continue
    print(f"printed {i}")

