class Matrix:

    matrix_count = 0

    def __init__(self, matrix_lst, matrix_lst2=None):
        Matrix.matrix_count += 1
        self.matrix_lst = matrix_lst
        self.matrix_lst2 = matrix_lst2

    def __str__(self):
        if self.matrix_lst2 is None:
            for i in self.matrix_lst:
                print(" ".join(map(str, i)))
        else:
            for i in self.matrix_lst:
                print(" ".join(map(str, i)))
            for j in self.matrix_lst2:
                print(" ".join(map(str, j)))

    def __add__(self, other):
        result = [[self.matrix_lst[i][j] + other[i][j] for j in range(len(self.matrix_lst[0]))] for i in
                  range(len(self.matrix_lst))]
        for i in result:
            print(" ".join(map(str, i)))

    def sum_matrix(self):
        if self.matrix_lst2:
            result = [[self.matrix_lst[i][j] + self.matrix_lst2[i][j] for j in range(len(self.matrix_lst[0]))] for i in
                      range(len(self.matrix_lst))]
            for i in result:
                print(" ".join(map(str, i)))
        else:
            print('Матрицы сложить нельзя.')
