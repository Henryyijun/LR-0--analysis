from dfa import *

if __name__ == '__main__':
    g = Grammar()
    g.create('product.txt')
    d = DFA(g)
    for i in d.grammar.P:
        print(i)
    print()
    d.dfa()
    s = set()
    s.add(Product('S', 'A'))
    s.add(Product('S', 'A'))
    for i in s:
        print(i)
