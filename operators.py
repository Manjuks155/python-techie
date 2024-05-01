# Arithmetic operators
print("<--------------Arithmetic operator------------>")
print(2+3)
print(2-3)
print(2*4)
print(5/2)  # division
print(5/3)  # division
print(5//2) # floor division
print(5//3)  # floor division
print(5%2)  # modulo
print(2**4) # power


# Identity operator
# validate the memory location - is, is not, id
print("<--------------Identity operator------------>")
a = 5
print(id(a))

a = 8
print(id(a))

print(a is a)
print(a is not a)

b = 5
c = 5
print(id(b))
print(id(c))
print(b is c)
print(b is not c)


# Membership operator
# check if exists or not - in, not in
print("<--------------Membership operator------------>")
name="python"
print('y' in name)
print("y" in name)
print("Y" in name)

l = [10, 5, 8, 1, 12]
print(10 in l)
print(20 in l)
print(50 not in l)
print(8 not in l)

