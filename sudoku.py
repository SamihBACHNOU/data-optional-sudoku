# pylint: disable=missing-docstring

def is_valid_sequence(seq):
    """
    Returns True if the given sequence is a valid Sudoku row, column or 3x3 square.
    """
# Verify the sequence has length 9
    if len(seq) != 9:
        return False

# Verify contains all numbers from 1 to 9
    for element in seq:
        if element < 1 or element > 9:
            return False
    if len(set(seq)) != 9:
        return False

    return True


def sudoku_validator(grid):
    """
    Returns True if the given Sudoku valid.
    """

# Check each row
    for row in grid:
        if not is_valid_sequence(row):
            return False

# Check each column
    for i in range(len(grid)):
        column = [row[i] for row in grid]
        if not is_valid_sequence(column):
            return False

# Check each 3x3 square
    for i in range(0,9,3):
        for j in range(0,9,3):
            square = [grid[x][y] for x in range(i, i+3) for y in range(j, j+3)]
            if not is_valid_sequence(square):
                return False

    return True
