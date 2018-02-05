#!/usr/bin/env python
from functools import reduce
from operator import add
from concurrent import futures

def vector_sum(ll):
    return reduce(lambda l1, l2: map(add, l1, l2), ll)

if __name__ == "__main__":
    unit_matrix = {"A": [1, 0, 0, 0],\
                   "T": [0, 1, 0, 0],\
                   "G": [0, 0, 1, 0],\
                   "C": [0, 0, 0, 1]}
    with open("NT_113952.1.fasta", "r") as f, futures.ThreadPoolExecutor(max_workers=1) as executor:
        f.__next__()
        count_list = vector_sum(map(lambda s: vector_sum(executor.map(lambda c: unit_matrix[c], s.rstrip("\n"))), f))
        for i in count_list:
            print(i)

