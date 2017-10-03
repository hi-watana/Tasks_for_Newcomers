#!/usr/bin/env python
# -*- coding: utf-8 -*-
#import numpy as np
import matplotlib.pyplot as plt
if __name__ == "__main__":
    f = open('NT_113952.1.fasta', 'r')
    f.readline()
    chain = f.read()
    chain = chain.replace('\n', '')
    length = len(chain)
    w = 1000
    s = 300
    i = 0
    contentList = []
    for i in range(int((length - w) / s)):
        tmp = chain[s * i:s * i + w]
        contentList.append(float(tmp.count('G') + tmp.count('C')) / w)

    if int((length - w) / s) * s < length:
        contentList.append(float(tmp.count('G') + tmp.count('C')) / w)
    #print len(contentList)
    plt.plot(contentList)
    plt.legend()
    plt.savefig('ex3.png')

    plt.show()
