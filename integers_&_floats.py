
# Arithmetic Operators:
# Addition:        3 + 2  ---a
# Subtraction:     3 - 2  ---b
# Multiplication:  3 * 2  ---c
# Division:        3 / 2  ---d
#Floor Division:   3 // 2  ---e
#Exponent:         3 ** 2  ---f
#Modulus:          3 % 2  ---g


a = 3 + 2
print(a)

b = 3 - 2
print(b)

c = 3 * 2
print(c)

d = 3 / 2
print(d)

e = 3 // 2
print(e)

f = 1.7 ** 2
print(f)

g = 3 % 2
print(g)


x = (3 * 2 + 1)  
print(x)

y = (3* (2 +1))   # Follows BODMAS
print(y)


num = 1
num = num +1 
print (num)     # Incrementing a variable

nu = 2
nu += 1     # Shorthand for increment
print(nu)

nu1 = 3
nu1 *= 50
print(nu1)


nu2 = 2
nu2 /= 4
print(nu2)

print(type(nu2))

print(type(f))

pi = 22 / 7
print(round(pi))

print(round(pi,10))

xy = -73
print(abs(xy))




# Boolean logic


# Typecasting

num_1 = '100'  # string datatype

num_2 = "200"  # string datatype

print(num_1 + num_2)  # answer should be 300 but it consider it as STRING and CONCATENATE

num_1 = int(num_1)  # Typecasted as int

num_2 = int(num_2)  # Typecasting

print(num_1 + num_2)
