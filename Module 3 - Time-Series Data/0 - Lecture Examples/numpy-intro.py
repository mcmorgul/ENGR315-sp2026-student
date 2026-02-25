import numpy as np

# make a basic array
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print('The array')
print(arr2d,'\n')

# what's the array shape
shape = arr2d.shape

# what type of data is it holding
type = arr2d.dtype

# access single elements (0,0) and (2,2)
item = arr2d[0, 0]
item2 = arr2d[2, 2]

# get the first row, second row, and right column
first_row = arr2d[0, :]
second_row = arr2d[1, :]
right_column = arr2d[:, 2]

# get the first two rows
first_two = arr2d[:2]
print('first two rows:')
print(first_two,'\n')

# from row 1, grab first two columns
two_columns = arr2d[1, :2]
print('first two columns:')
print(two_columns,'n')

# from all rows, get the first column
first_column = arr2d[:, 0]
print('the first column:')
print(first_column,'\n')

print('The array')
print(arr2d,'\n')
x = arr2d[2:][0]
print('try:')
print('arr2d[1][2]:',arr2d[1][2])
print('arr2d[1,2]:',arr2d[1,2])
print('')

print('arr2d[1][0:2]:',arr2d[1][0:2])
print('arr2d[1][0:3]:',arr2d[1][0:3])
print('arr2d[1,0:3]:',arr2d[1,0:3])
print('')

print('arr2d[1,0:2][0:2]:',arr2d[1,0:2][0:2])
print('arr2d[1,0:2]:',arr2d[1,0:2])
print('arr2d[1,0:2][1]:',arr2d[1,0:2][1])
print('')

print('arr2d[1:3,0:3]:',arr2d[1:3,0:3])
print('arr2d[1:3,0:3][0:2]:',arr2d[1:3,0:3][0:2])
print('arr2d[1:3,0:3][0:2][1]:',arr2d[1:3,0:3][0:2][1])
print('')

print('arr2d[1:3,0:2]:',arr2d[1:3,0:2])
print('arr2d[1:3][0:2]:',arr2d[1:3][0:2])
print('arr2d[1:3][:,0:2]:',arr2d[1:3][:, 0:2])

