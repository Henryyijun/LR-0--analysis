from dfa import *

if __name__ == '__main__':
    g = Grammar()
    g.create('product.txt')
    d = DFA(g)
    for i in d.grammar.P:
        print(i)
    print()
    d.dfa()

