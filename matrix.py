# -*- coding: utf-8 -*-

class Matrix():
    def __init__(self, m = []):
        self.m = m

    def __str__(self):
        if self.m:
            s = ''
            for i in self.m:
                s += '| '
                for j in i:
                    s += str(j) + ' '
                s += '|\n'  
            return s
        else:
            return 'Empty matrix'
        
    def null(self, r, c):
        '''
        Generates a null-matrix of size R x C.
        '''
    
        if r < 0 or c < 0 or not type(r) == int or not type(c) == int:
            raise ValueError('Rows and cols must be positive integers.')
        
        self.m = [[0 for i in range(c)] for j in range(r)]
        
    def unit(self, n):
        '''
        Generates a square unit-matrix of size N x N.
        '''
        
        self.null(n, n)
        for i in range(n):
            self.m[i][i] = 1
    


if __name__=='__main__':
    import unittest
    
    class MatrixTestCase(unittest.TestCase):
    
        def test_print_matrix(self):
            m = Matrix([[1,2], [3,4]])
            self.assertEqual(m.__str__(), '| 1 2 |\n| 3 4 |\n')
    
        def test_create_null_matrix(self):
            m = Matrix()
            m.null(2, 3)
            self.assertEqual(m.m, [[0, 0, 0],[0, 0, 0]])
            
        def test_create_unit_matrix(self):
            m = Matrix()
            m.unit(3)
            self.assertEqual(m.m, [[1, 0, 0], [0, 1, 0], [0, 0, 1]])
        
    unittest.main()
