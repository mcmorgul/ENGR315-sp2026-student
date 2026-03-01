import numpy as np

# generate a random array. Max value is 10, length is 5
a = np.random.randint(10, size=5)
print(a)
print()
# generate a random array. Max value is 10, length is 5
b = np.random.randint(10, size=5)
print(b)
print()

# add the two arrays, piece-wise
c = a + b
print(c)
print()

# square each element of the array
squares = a ** 2
print(squares)
print()

# square each element and then add piece-wise
added_squares = a ** 2 + b ** 2
print(added_squares)
print()

# sum the resulting array to a single value
num = sum(added_squares)
print(num)
print()

print(c)
print()
d = c + 5
print(d)
print()

print(c)
print()
d = c / 2
print(d)