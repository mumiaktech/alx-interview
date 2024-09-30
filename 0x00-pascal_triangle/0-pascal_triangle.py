#!/usr/bin/python3
def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = []

    for row in range(n):
        # Start each row with 1
        new_row = [1] * (row + 1)

        # Calculate the values for the inner elements of the row
        for j in range(1, row):
            new_row[j] = triangle[row - 1][j - 1] + triangle[row - 1][j]

        triangle.append(new_row)

    return triangle

