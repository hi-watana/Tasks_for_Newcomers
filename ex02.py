# -*- coding: utf-8 -*-
def reverseComplement(s):
    s = s.replace('A', 't')
    s = s.replace('T', 'A')
    s = s.replace('t', 'T')
    s = s.replace('G', 'c')
    s = s.replace('C', 'G')
    s = s.replace('c', 'C')
    return s[::-1]

