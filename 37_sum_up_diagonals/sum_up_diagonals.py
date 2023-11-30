def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """
    #had to refer to solution---> studied solution for understanding
    total = 0
    #range(len(matrix)) produces the numbers (0,1,2) for m2
    for i in range(len(matrix)):
        total += matrix[i][i]
            #in m2 this produces +[0],[0] + [1][1] + [2][2]
        total += matrix[i][-1 - i]
            #in m2 this produces +[0],[-1] + [1][-2] + [2][-3]

    return total