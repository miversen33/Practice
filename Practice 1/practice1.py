def parse(matrix, key):
    found = False

    # Picking through the rows of the matrix. We are comparing the key to the created string of each row.
    for row in matrix:
        parsedRow = ''.join(row)
        if parsedRow.__contains__(key):
            found = True
            break

    # Picking through the columns of the matrix. We are comparing the key to the created string of each column.
    for col in range(0, matrix.__len__()):
        parsedCol = ''.join([column[col] for column in matrix])
        if parsedCol.__contains__(key):
            found = True
            break

    return found