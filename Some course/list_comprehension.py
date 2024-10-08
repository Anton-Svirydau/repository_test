""""""

'''
squares = []
for x in range(10):
    squares.append(x ** 2)

# squares = [x ** 2 for x in range(10)]

print(squares)
'''

'''
even_squares = []
for x in range(10):
    if x % 2 == 0:
        even_squares.append(x ** 2)

# even_squares = [x ** 2 for x in range(10) if x % 2 == 0]

print(even_squares)
'''

'''
labelled_numbers = []
numbers = [1, 2, 3, 4, 5]

for num in numbers:
    if num % 2 == 0:
        labelled_numbers.append("even")
    else:
        labelled_numbers.append("odd")
        
print(labelled_numbers)
'''


'''
numbers = [1, 2, 3, 4, 5]

labelled_numbers = ["even" if num % 2 == 0 else "odd" for num in numbers]

print(labelled_numbers)
'''

'''
square_dict = {x: x ** 2 for x in range(10)}

print(square_dict)
'''

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

transpose_matrix = []

for i in range(len(matrix)):
    transpose_row = []
    for row in matrix:
        transpose_row.append(row[i])
    transpose_matrix.append(transpose_row)

# transpose_matrix = [[row[i] for row in matrix] for i in range(len(matrix))]

print(transpose_matrix)
