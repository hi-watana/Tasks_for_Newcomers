#!/usr/bin/env python
# -*- coding: utf-8 -*-
#import numpy as np
import re
import sys
import ex02

if __name__ == "__main__":
    args = sys.argv
    argc = len(args)
    if argc != 2:
        sys.stderr.write('Usage: python ' + args[0] + ' <subarray>\n')
        sys.exit(1)
    f = open('NT_113952.1.fasta', 'r')
    f.readline()
    chain = f.read()
    chain = chain.replace('\n', '')
    rcomp = ex02.reverseComplement(chain)
    iterator = re.finditer(args[1], chain)
    print('chain:')
    for i in iterator:
        #print(str(i.start()) + ', ', end='')
        print(i.start())
    iterator = re.finditer(args[1], rcomp)
    print('reverse complement:')
    for i in iterator:
        #print(str(i.start()) + ', ', end='')
        print(i.start())
