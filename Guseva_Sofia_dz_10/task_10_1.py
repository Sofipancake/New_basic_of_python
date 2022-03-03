"""Задание 1
Реализовать класс Matrix (матрица).

Обеспечить перегрузку конструктора класса (метод __init__()), который должен принимать данные
(список списков) для формирования матрицы. В случае если список списков некорректный - возбуждать
исключение ValueError с сообщением fail initialization matrix.

Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
| 31 43 |
| 22 51 |
| 37 86 |

| 3 5 32 |
| 2 4 6 |
| -1 64 -8 |

| 3 5 8 3 |
| 8 3 7 1 |

Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде
(как показано выше).
Далее реализовать перегрузку метода __add__() для сложения двух объектов класса Matrix
(двух матриц). Результатом сложения должна быть новая матрица."""

from typing import List


class Matrix:
    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        fs = len(matrix[0])
        for row in matrix:
            if len(row) != fs:
                raise ValueError('fail initialization matrix')

    def __str__(self):
        return '\n'.join([f'| {" ".join(map(str, row))} |' for row in self.matrix])

    def __add__(self, other):
        summatr = Matrix([
            [self.matrix[i][j] + other.matrix[i][j] for j in range(len(self.matrix[0]))]
            for i in range(len(self.matrix))
        ])
        return summatr


if __name__ == '__main__':
    first_matrix = Matrix([[1, 2], [3, 4], [5, 6]])
    second_matrix = Matrix([[6, 5], [4, 3], [2, 1]])
    print(first_matrix)
    """    
    | 1 2 |
    | 3 4 |
    | 5 6 |
    """
    print(first_matrix + second_matrix)
    """    
    | 7 7 |
    | 7 7 |
    | 7 7 |
    """
    fail_matrix = Matrix([[1, 2], [3 ,4, 7], [5, 6]])
    """
    Traceback (most recent call last):
      ...
    ValueError: fail initialization matrix
    """
