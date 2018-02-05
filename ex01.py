#!/usr/bin/env python
if __name__ == "__main__":
    with open('NT_113952.1.fasta', 'r') as f:
        f.__next__()
        chain = f.read()
        print('A: ' + str(chain.count('A')))
        print('T: ' + str(chain.count('T')))
        print('G: ' + str(chain.count('G')))
        print('C: ' + str(chain.count('C')))
