# -* - coding: utf-8 -*-

import re

class Parser():
    def __init__(self, text):
        self.text = text
        self.equation_rgx = re.compile(
            '(?:[+-][0-9,.]*x[0-9]+)+=[0-9,.]+'
        )
        self.term_rgx = re.compile(
            '([+-][0-9,.]*)x[0-9]+'
        )
        
    def parse(self):
        
        # preprocessing
        text = self.text
        text = text.replace(' ', '').replace(',', '.')
        text = text.replace('+x', '+1x').replace('-x', '-1x')
        
        # if there are no float factors 
        # then all is of integer type.
        if '.' in text:
            _type = float
        else:
            _type = int
        
        m = [] #matrix
        for e in self.equation_rgx.finditer(text):       
            r = [] #row of the matrix
            for t in self.term_rgx.finditer(e.group()):
                r.append( _type(t.group(1)) )
            m.append(r)
        
        return m
        
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