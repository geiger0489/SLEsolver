# -*- coding: utf-8 -*-

from copy import deepcopy

class Matrix():
    def __init__(self, m = []):
        self.set(m)
        
    def __eq__(self, other):
        if type(other) == Matrix:
            return self.m == other.m
        elif type(other) == list:
            return self.m == other
        else:
            raise TypeError('Unsupported operand "==" for Matrix and %s' % other.__class__.__name__)

    def __str__(self):
        if not self.m:
            return 'Empty matrix'
            
        r, c = self.dimensions()
        if r == c == 1:
            return str(self.m[0][0])
        if r > 50 or c > 50:
            return 'Matrix of %s x %s elements' % (r, c)
        
        max = 1
        for i in self.m:
            for j in i:
                l = len( str(j) )
                max = l if l > max else max
        max = str(max + 1)
        s = ''
        row = '|' + ('%' + max + 's') * len(self.m[0]) + ' |\n'
        for i in self.m:
            s += row % tuple(i)  
        return s
 
    def __add__(self, other):
        '''
        Sums two equal matrices. A + B = C.
        '''
        
        if not other.dimensions() == self.dimensions():
            raise Exception('Matrix dimensions must be equal.')
        
        result = Matrix( deepcopy(self.m) )
        for i in range( len(result.m) ):
            for j in range( len(result.m[i]) ):
                result.m[i][j] += other.m[i][j]
        
        return result
        
    def __sub__(self, other):
        '''
        Subtracts two equal matrices. A - B = C.
        '''
        
        other = Matrix( deepcopy(other.m) )
        other.invert()
        return self.__add__(other)
    
    def set(self, m):
        if not type(m) == list:
            raise TypeError('Input parameter must be of type "list".')
        
        self.m = m
    
    def is_empty(self):
        if self.m:
            return False
        else:
            return True
        
    def fill(self, r, c, n):
        '''
        Generates a matrix of size R x C with all elements equal to n.
        '''
    
        if r < 0 or c < 0 or not type(r) == type(c) == int:
            raise ValueError('Rows and cols must be positive integers.')
        
        self.m = [[n for i in range(c)] for j in range(r)]
        return self

    def null(self, r, c):
        '''
        Generates a null-matrix of size R x C.
        '''
        
        return self.fill(r, c, 0)
        
    def ones(self, r, c):
        '''
        Generates a all-ones matrix of size R x C.
        '''
        
        return self.fill(r, c, 1)
        
    def unity(self, n):
        '''
        Generates a square unity matrix of size N x N.
        '''
        
        self.null(n, n)
        for i in range(n):
            self.m[i][i] = 1
        return self
            
    def invert(self):
        '''
        Inverts the matrix (aij = -aij)
        '''
        
        for i in range( len(self.m) ):
            for j in range( len(self.m[i]) ):
                self.m[i][j] *= -1
        return self
        
    def flip_rows(self, m, n):
        '''
        Flips m-th and n-th rows.
        '''
        
        if not type(m) == type(n) == int:
            raise TypeError('Row indices must be integer.')
        
        buff = self.m[m]
        self.m[m] = self.m[n]
        self.m[n] = buff
        return self

    def flip_cols(self, m, n):
        '''
        Flips m-th and n-th cols.
        '''
        
        if not type(m) == type(n) == int:
            raise TypeError('Column indices must be integer.')
        
        for i in self.m:
            buff = i[m]
            i[m] = i[n]
            i[n] = buff
        return self
        
    def dimensions(self):
        '''
        Returns matrix dimensions as a tuple (rows, cols).
        '''
        
        if not self.m:
            raise Exception('Trying to get dimensions of empty matrix')
        return (len(self.m), len(self.m[0]))
        
    def is_square(self):
        '''
        Returns True if the matrix is square
        and returns False if it's not.
        '''
        
        return len(self.m) == len(self.m[0])
        
    def append_right(self, m):
        '''
        Appends a given matrix to the right of the existing one.
        Matrices must have equal heights.
        '''
        
        if not type(m) == Matrix:
            raise TypeError('Trying to append non-matrix to Matrix object')
            
        rm, cm = m.dimensions()
        r, c = self.dimensions()
        
        if not rm == r:
            raise ValueError('Matrices have different height.')
        
        for i in range(r):
            self.m[i].extend(m.m[i])
        return self

    def append_left(self, m):
        '''
        Appends a given matrix to the left of the existing one.
        Matrices must have equal heights.
        '''
        
        if not type(m) == Matrix:
            raise TypeError('Trying to append non-matrix to Matrix object')
            
        rm, cm = m.dimensions()
        r, c = self.dimensions()
        
        if not rm == r:
            raise ValueError('Matrices have different height.')
        
        for i in range(r):
            self.m[i] = m.m[i] + self.m[i]
        return self
        
    def transpose(self):
        '''
        Transposes a given matrix. a[i][j] --> a[j][i] 
        '''
        
        def transpose_square(r, c):
            for i in range(r):
                for j in range(i, c):
                    if i == j:
                        continue
                    b = self.m[i][j]
                    self.m[i][j] = self.m[j][i]
                    self.m[j][i] = b
        
        r, c = self.dimensions()
        if r == c: # if the matrix is square
            transpose_square(r, c)
            
        elif r < c: # if the matrix is horizontal
            transpose_square(r, r)
            for i in range(c - r):
                row = []
                for j in range(r):
                    row.append(self.m[j][r])
                    del self.m[j][r]
                self.m.append(row)
                
        else: # if the matrix is vertical
            transpose_square(c, c)
            for i in range(r - c):
                for j in range(c):
                    self.m[j].append(self.m[c][j])
                del self.m[c]
    
    def to_upper_triangular(self):
        '''
        Transforms the matrix to upper triangular matrix.
        1 2 3           1 2 3
        4 5 6  goes to  0 5 6
        7 8 9           0 0 9
        '''
        '''
        r, c = self.dimensions()
        for j in range(c):
            for i in range(j + 1, r):
                self.m[i][j] - self.m[i - 1][j] * self.m[i][j] / self.m[i - 1][j]
        '''
                
                      
if __name__=='__main__':
    import unittest
    
    class MatrixTestCase(unittest.TestCase):
    
        def test_print_matrix(self):
            m = Matrix([[1, 2, 3], [4, 5, 6]])
            self.assertEqual(m.__str__(), '| 1 2 3 |\n| 4 5 6 |\n')

        def test_fill_matrix_with_n(self):
            m = Matrix()
            m.fill(2, 3, 5)
            self.assertEqual(m, [[5, 5, 5],[5, 5, 5]])
            
        def test_create_null_matrix(self):
            m = Matrix()
            m.null(2, 3)
            self.assertEqual(m, [[0, 0, 0],[0, 0, 0]])
            
        def test_create_ones_matrix(self):
            m = Matrix()
            m.ones(2, 3)
            self.assertEqual(m, [[1, 1, 1],[1, 1, 1]])
            
        def test_create_unity_matrix(self):
            m = Matrix()
            m.unity(3)
            self.assertEqual(m, [[1, 0, 0], [0, 1, 0], [0, 0, 1]])
            
        def test_invert_matrix(self):
            m = Matrix()
            m.unity(3)
            m.invert()
            self.assertEqual(m, [[-1, 0, 0], [0, -1, 0], [0, 0, -1]])

        def test_flip_cols(self):
            m = Matrix([[1,2],[3,4]])
            self.assertEqual(m.flip_cols(0, 1), [[2,1], [4,3]])
            
        def test_flip_rows(self):
            m = Matrix([[1,2],[3,4]])
            self.assertEqual(m.flip_rows(0, 1), [[3,4], [1,2]])
            
        def test_get_matrix_dimensions(self):
            m = Matrix([[-1, 0, 0], [0, 0, -1]])
            self.assertEqual(m.dimensions(), (2, 3))

        def test_sum_two_matrices(self):
            m1 = Matrix([[1, 1], [1, 1]])
            m2 = Matrix([[1, 1], [1, 1]])
            m3 = m1 + m2
            self.assertEqual(m3, [[2, 2], [2, 2]])
        
        def test_subtract_two_matrices(self):
            m1 = Matrix([[1, 1], [1, 1]])
            m2 = Matrix([[1, 1], [1, 1]])
            m3 = m1 - m2
            self.assertEqual(m3, [[0, 0], [0, 0]])
            
        def test_matrix_is_square(self):
            m1 = Matrix([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
            m2 = Matrix([[1, 1, 1], [1, 1, 1]])
            self.assertTrue(m1.is_square())
            self.assertFalse(m2.is_square())
        
        def test_transpose_matrix(self):
            m = Matrix([[1, 2, 3], [1, 2, 3], [1, 2, 3]]) #square
            m.transpose()
            self.assertEqual(m, [[1, 1, 1], [2, 2, 2], [3, 3, 3]])
            
            m = Matrix([[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]]) # cols > rows
            m.transpose()
            self.assertEqual(m, [[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4], [5, 5, 5]])
            
            m = Matrix([[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4], [5, 5, 5]]) # cols < rows
            m.transpose()
            self.assertEqual(m, [[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]])

        def test_append_right(self):
            m1 = Matrix([[1, 2, 3], [1, 2, 3], [1, 2, 3]])
            m2 = Matrix([[4], [4], [4]])
            self.assertTrue(m1.append_right(m2) == [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]])

        def test_append_left(self):
            m1 = Matrix([[1, 2, 3], [1, 2, 3], [1, 2, 3]])
            m2 = Matrix([[4], [4], [4]])
            self.assertTrue(m1.append_left(m2) == [[4, 1, 2, 3], [4, 1, 2, 3], [4, 1, 2, 3]])
           
    unittest.main()
