import math, copy


def format_sudoku(sudoku_, name="Table"):
    print(f"{name} looks like this:")
    for line in sudoku_:
        ln = ""
        for chr in line:
            ln += str(chr) + " | "
        print(ln)


def slice(list, index):
    temp = []
    for item in list:
        temp.append(item[index])
    return temp


def matrix(sudoku, idx, idy):
    FACTOR = int(math.sqrt(len(sudoku)))
    if idx <= FACTOR and idy <= FACTOR:
        temp = sudoku[idx * FACTOR: (idx + 1) * FACTOR]
        matrice = []
        for line in temp:
            matrice += line[idy * FACTOR: (idy + 1) * FACTOR]
        return matrice


def count(sudoku, element):
    count = 0
    for line in sudoku:
        for item in line:
            if element == item:
                count += 1
    return count


sudoku = [[None, 3, None, None, None, 8, 9, 1, None],
          [None, 7, None, None, 1, 4, 5, None, None],
          [6, None, None, 9, None, 2, 8, None, None],
          [None, None, None, None, None, None, None, None, None],
          [None, None, None, None, 4, 6, 2, 9, 7],
          [None, 2, None, None, None, None, 6, None, None],
          [None, 6, 3, 5, 7, None, 4, 8, 2],
          [8, 5, 7, 4, None, 3, 1, 6, None],
          [None, 4, 9, 8, 6, None, None, None, 5]]

template_3x3 = [i for i in range(1, 10)]
template_4x4 = template_3x3 + "A,B,C,D,E,F,G".split(',')

format_sudoku(sudoku)

FACTOR = int(math.sqrt(len(sudoku)))
flag = 0
probabilities = copy.deepcopy(sudoku)
iteration_counter = 1

count_None = count(sudoku, None)
while count(sudoku, None) > 0:
    count_None = count(sudoku, None)
    print(f"*** ITERATION {iteration_counter} ***")
    for x, line in enumerate(sudoku):
        for y, item in enumerate(line):
            if item is None:
                idx = int(x / FACTOR)
                idy = int(y / FACTOR)
                local_matrice = matrix(sudoku, idx, idy)
                slice_column = slice(sudoku, y)
                candidates = [i for i in template_3x3 if
                              i not in line and i not in local_matrice and i not in slice_column]
                probabilities[x][y] = candidates
                if len(candidates) == 1:
                    sudoku[x][y] = candidates[0]
                else:
                    flag -= 1
    format_sudoku(sudoku, "Sudoku")
    format_sudoku(probabilities, "Probabilities")
    iteration_counter += 1
