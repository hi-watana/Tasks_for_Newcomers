#!/usr/bin/env python
if __name__ == "__main__":
    f = open('NT_113952.1.fasta', 'r')
    f.readline()
    chain = f.read()
    print('A: ' + str(chain.count('A')))
    print('T: ' + str(chain.count('T')))
    print('G: ' + str(chain.count('G')))
    print('C: ' + str(chain.count('C')))
