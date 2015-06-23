# -*- coding: utf-8 -*-

class Matrix():
    def __init__(self, m = None):
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

if __name__=='__main__':
    pass
