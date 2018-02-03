#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import math
import sys
import numpy as np

def isAtomLine(line):
    c = line[15]
    return (line[0:4] == "ATOM" or line[0:6] == "HETATM") \
            and line[13:15] == "CA" \
            and (c == " " or c == "A") \
            and line[21] == chain

def getRadiusOfGyration(filename, chain):
    with open(filename, "r") as f:
        atom_lines = filter(isAtomLine, f)
        xyz_list = [[float(s[30:37].strip()),\
                     float(s[38:45].strip()),\
                     float(s[46:53].strip())] for s in atom_lines]
        gravity = np.array(xyz_list).T.mean(axis=1)
        return np.linalg.norm(xyz_list - gravity,axis=1).mean()

if __name__ == "__main__":
    args = sys.argv
    argc = len(args)
    if argc != 3:
        sys.stderr.write('Usage: python ' + args[0] + ' <PDB file> <chain name>\n')
        sys.exit(1)

    filename = args[1]
    chain    = args[2]
    print(getRadiusOfGyration(filename, chain))
