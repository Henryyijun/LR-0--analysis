from syntax_tree import *
from grammar import *
from dfa import *

if __name__ == '__main__':
    g = Grammar()
    g.create('product.txt')
    d = DFA(g)
    for i in d.grammar.P:
        print(i)
    print()
    close = d.closure(Product("S'", '.B'))
    for i in close:
        print(i)
