from dfa import *

if __name__ == '__main__':
    g = Grammar()
    g.create('product.txt')
    d = DFA(g)
    close = d.closure(Product("S'", '.S'))
    for i in close:
        print(i)
    print()
    d.dfa()

