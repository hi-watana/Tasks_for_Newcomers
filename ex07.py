#!/usr/bin/env python
# -*- coding: utf-8 -*-
#import numpy as np
import re
import sys
import math

def getRadiusOfGyration(filename, chain):
    f = open(filename, 'r')
    string = f.read()

    xyzTable = map(lambda l: l[2:5], \
                    filter(lambda x: x[0] == chain, \
                            map(lambda s2: s2.split()[4:9], \
                                 filter(lambda s1: re.search('\sCA\s', s1) != None, \
                                            string.split('\n')))))

    center = map(lambda x: x/len(xyzTable), \
                    reduce(lambda l1, l2: map(lambda s1, s2: float(s1)+float(s2), l1, l2), \
                            xyzTable))

    return sum(map(lambda r: math.sqrt(r[0]*r[0]+r[1]*r[1]+r[2]*r[2]), \
                    map(lambda l: map(lambda x1, x2: float(x1)-x2, l, center), \
                                        xyzTable))) / len(xyzTable)

if __name__ == "__main__":
    args = sys.argv
    argc = len(args)
    if argc != 3:
        sys.stderr.write('Usage: python ' + args[0] + ' <PDB file> <chain name>\n')
        sys.exit(1)

    filename = args[1]
    chain    = args[2]
    print(getRadiusOfGyration(filename, chain))
