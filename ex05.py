#!/usr/bin/env python
# -*- coding: utf-8 -*-
#import numpy as np
import ex02

def dnaToAminoAcid(chain, start):
    codonList = {'TTT':'F', # Phe \
                 'TTC':'F', # Phe \
                 'TTA':'L', # Leu \
                 'TTG':'L', # Leu \
                 'TCT':'S', # Ser \
                 'TCC':'S', # Ser \
                 'TCA':'S', # Ser \
                 'TCG':'S', # Ser \
                 'TAT':'Y', # Tyr \
                 'TAC':'Y', # Tyr \
                 'TAA':'_', # STOP \
                 'TAG':'_', # STOP \
                 'TGT':'C', # Cys \
                 'TGC':'C', # Cys \
                 'TGA':'_', # STOP \
                 'TGG':'W', # Trp \
                 'CTT':'L', # Leu \
                 'CTC':'L', # Leu \
                 'CTA':'L', # Leu \
                 'CTG':'L', # Leu \
                 'CCT':'P', # Pro \
                 'CCC':'P', # Pro \
                 'CCA':'P', # Pro \
                 'CCG':'P', # Pro \
                 'CAT':'H', # His \
                 'CAC':'H', # His \
                 'CAA':'Q', # Gln \
                 'CAG':'Q', # Gln \
                 'CGT':'R', # Arg \
                 'CGC':'R', # Arg \
                 'CGA':'R', # Arg \
                 'CGG':'R', # Arg \
                 'ATT':'I', # Ile \
                 'ATC':'I', # Ile \
                 'ATA':'I', # Ile \
                 'ATG':'M', # Met \
                 'ACT':'T', # Thr \
                 'ACC':'T', # Thr \
                 'ACA':'T', # Thr \
                 'ACG':'T', # Thr \
                 'AAT':'N', # Asn \
                 'AAC':'N', # Asn \
                 'AAA':'K', # Lys \
                 'AAG':'K', # Lys \
                 'AGT':'S', # Ser \
                 'AGC':'S', # Ser \
                 'AGA':'R', # Arg \
                 'AGG':'R', # Arg \
                 'GTT':'V', # Val \
                 'GTC':'V', # Val \
                 'GTA':'V', # Val \
                 'GTG':'V', # Val \
                 'GCT':'A', # Ala \
                 'GCC':'A', # Ala \
                 'GCA':'A', # Ala \
                 'GCG':'A', # Ala \
                 'GAT':'D', # Asp \
                 'GAC':'D', # Asp \
                 'GAA':'E', # glu \
                 'GAG':'E', # glu \
                 'GGT':'G', # Gly \
                 'GGC':'G', # Gly \
                 'GGA':'G', # Gly \
                 'GGG':'G', # Gly \
                 }
    frameList = [chain[i: i+3] for i in range(start, len(chain), 3)]
    end = len(frameList) - 1
    if len(frameList[end]) < 3:
        frameList.pop(end)

    return ''.join(map(lambda frame: codonList[frame], frameList))


if __name__ == "__main__":
    f = open('NT_113952.1.fasta', 'r')
    f.readline()
    chain = f.read()
    chain = chain.replace('\n', '')
    rcomp = ex02.reverseComplement(chain)
    print('chain:')
    for i in range(3):
        print(str(i) + ': ' + dnaToAminoAcid(chain, i))
    print('reverse complement:')
    for i in range(3):
        print(str(i) + ': ' + dnaToAminoAcid(rcomp, i))
