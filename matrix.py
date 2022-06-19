class Integer:
    def __init__(self, val):
        if isinstance(val, int):
            self.value = val
        else:
            raise TypeError('Value mist be integer!')

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self.value)


    def __eq__(self, other):
        if isinstance(other, Integer):
            value = other.value
        elif isinstance(other, int):
            value = other
        elif isinstance(other, Complex):
            if other.i != 0 :
                return False
            value = other.r
        else:
            return NotImplemented
        # Check equivalent
        if self.value == value :
            return True
        else:
            return False

    def __add__(self, other):
        if isinstance(other, Matrix):
            return NotImplemented
        elif isinstance(other, Integer):
            return Integer(self.value + other.value)
        elif isinstance(other, Complex):
            return NotImplemented
        else:
            raise TypeError('Integer cant add to this type.')

    def __mul__(self, other):
        if isinstance(other, Matrix):
            return NotImplemented
        elif isinstance(other, Integer):
            return Integer(self.value * other.value)
        elif isinstance(other, Complex):
            return NotImplemented
        else:
            raise TypeError('Integer cant mult by this type.')

    @staticmethod
    def make_integer_from_string(string):
        return Integer(int(string))
#-------------------------------------------------------------------------


class Complex:
    def __init__(self, real, imaginary):
        self.i = imaginary
        self.r = real

    def __eq__(self, other):
        if isinstance(other, Complex):
            if (self.i == other.i) and (self.r == other.r):
                return True
            else:
                return False
        else:
            return NotImplemented

    def __add__(self, other):
        if isinstance(other, Matrix):
            return NotImplemented
        elif isinstance(other, Integer):
            return Complex(self.r + other.value, self.i)
        elif isinstance(other, Complex):
            return Complex(self.r + other.r, self.i + other.i)
        else:
            raise TypeError('Complex number cant add this type')

    def __sub__(self, other):
        return self + other * Integer(-1)

    def __mul__(self, other):
        if isinstance(other, Matrix):
            return NotImplemented
        elif isinstance(other, Integer):
            return Complex(self.r * other.value, self.i * other.value)
        elif isinstance(other, Complex):
            return Complex(self.r * other.r - self.i * other.i, self.i * other.r + self.r * other.i)
        else:
            raise TypeError('Complex number cant multiply by this type.')

    def __str__(self):
        return str(self.r)+ ('' if self.i < 0 else '+') + str(self.i) + 'i'

    def __repr__(self):
        return str(self.r)+ ('' if self.i < 0 else '+') + str(self.i) + 'i'

#-------------------------------------------------------------------------


class Matrix :
    def __init__(self, row, col, matrix):
        self.row = row
        self.col = col
        if all((isinstance(it, Integer) or isinstance(it, Complex) for it in matrix)):
            self.matrix = []

            for r in range(row) :
                self.matrix.append(matrix[r*col:(r+1) * col])
            else:
                raise TypeError('Value must be an instance of Integer or Complex class')

    @staticmethod
    def make_unit_matrix(n):
        return Matrix(n, n, [Integer(1) if i % (n + 1) == 0 else Integer(0) for i in range(n * n)])

    @staticmethod
    def get_ith_row(matrix, i):
        return matrix.matrix[i]

    @staticmethod
    def get_ith_col(matrix, j):
        return [it[j] for it in matrix.matrix]

    @staticmethod
    def is_zero_matrix(matrix):
        for i in matrix.matrix:
            for j in i:
                if j != 0:
                    return False
        return True

    @staticmethod
    def is_unit_matrix(matrix):
        if matrix.row != matrix.col:
            return False
        return matrix == Matrix.make_unit_matrix(matrix.row)

    @staticmethod
    def is_bottom_triangular_matrix(matrix):
        if matrix.row != matrix.col:
            return False
        for i in range(matrix.row):
            for j in range(i + 1, matrix.col):
                if matrix.matrix[i][j] != 0:
                    return False
        return True

    @staticmethod
    def is_top_triangular_matrix(matrix):
        if matrix.row != matrix.col:
            return False
        for i in range(matrix.row):
            for j in range(i):
                if matrix.matrix[i][j] != 0:
                    return False
        return True

    @classmethod
    def make_matrix_from_string(cls, elements):
        matrix = []
        rows = elements.split(',')
        for row in rows:
            for item in row.split(' '):
                if 'i' in item:
                    matrix.append()


