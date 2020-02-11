# Khayyam Triangle

# The French mathematician, Blaise Pascal, who built a mechanical computer in
# the 17th century, studied a pattern of numbers now commonly known in parts of
# the world as Pascal's Triangle (it was also previously studied by many Indian,
# Chinese, and Persian mathematicians, and is known by different names in other
# parts of the world).

# The pattern is shown below:

#                    1
#                   1 1
#                  1 2 1
#                 1 3 3 1
#                1 4 6 4 1
#                   ...

# Each number is the sum of the number above it to the left and the number above
# it to the right (any missing numbers are counted as 0).

# Define a procedure, triangle(n), that takes a number n as its input, and
# returns a list of the first n rows in the triangle. Each element of the
# returned list should be a list of the numbers at the corresponding row in the
# triangle.


# padder(row) takes a row as a list and pads zeros at its beginning and its end.
def row_padder(row):
    return ([0] + row + [0])

# make_next_row(current_row) takes current_row as input and returns a list
# corresponding to the next row w.r.t. the current row.
def make_next_row(current_row):
    next_row = []
    padded_current_row = row_padder(current_row)
    for idx in range(len(padded_current_row)-1):
        next_row.append(padded_current_row[idx] + padded_current_row[idx+1])
    return next_row

# Define a procedure, triangle(n), that takes a number n as its input, and
# returns a list of the first n rows in the triangle.
def triangle(n):
    if n == 0: return []
    triangle_list = []
    n_iterations = n
    current_row = [1]
    for iteration in range(n_iterations):
        triangle_list += [current_row]
        current_row = make_next_row(current_row)
    return triangle_list


####################
#      TESTS       #
####################

print(triangle(0))

print(triangle(1))

print(triangle(2))

print(triangle(3))

print(triangle(6))

