# while and while else
# sentinel value

count = 5
while count > 0:
    print(count)
    count -= 1
    if count == 3:
        break
else:
    print("in else part of while")

print("end of while loop")
