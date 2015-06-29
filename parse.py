# -* - coding: utf-8 -*-

import re

class Parser():
    def __init__(self, text):
        self.text = text
        self.equation_rgx = re.compile(
            '[+-]?([0-9]+([,.][0-9]+)?)?x[0-9]+([+-]([0-9]+([,.][0-9]+)?)?x[0-9]+)*=([+-])?([0-9]+([,.][0-9]+)?)'
        )
        self.term_rgx = re.compile(
            '([+-])?([0-9]+(?:[,.][0-9]+)?)?x([0-9]+)'
        )
        
    def parse(self):
        '''
        Parses a given text from TextEdit widget
        and return a list of lists containing factors
        of a given system of linear equations.
        '''
    
        text = self.text
        
        # preprocess
        r = {
            ' ': '',
            ',': '.',
            '*': '',
        }
        for i in r.keys():
            text = text.replace(i, r[i])
        
        if '.' in text:
            _type = float
        else:
            _type = int
        
        m = []
        xmax = 1
        for e in self.equation_rgx.finditer(text):       
            r = []
            for t in self.term_rgx.finditer(e.group()):
                term = t.groups()
                if int(term[2]) > xmax:
                    xmax = int(term[2])
                r.append( term )
            m.append(r)
        
        matr = [[0 for i in range(xmax)] for j in range( len(m) )]
        r = 0
        for i in m:
            for j in i:
                _sign = -1 if j[0] == '-' else 1
                a = 1 if j[1] == None else j[1]
                # next row do work if there are several terms of the same var xn
                # they will be summed up
                matr[r][ int(j[2])-1 ] += _sign * _type(a)
            r += 1

        return matr
        
if __name__ == '__main__':
    import unittest
    
    class ParserTestCase(unittest.TestCase):
    
        def test_parse_method(self):
            input1 = '''+2.8x1 + x2 - 2x3 = 3
                       +6,1x1 + 9.8x2-7.0x3=5'''
            input2 = '''+2x1 + x2 - 2x3 = 3
                       +6x1 + 9x2-7x3=5'''
            
            for i in [input1, input2]:
                self.assertEqual(Parser(i).parse(), False)
            
    unittest.main()