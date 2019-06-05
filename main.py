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
    d.show_i()
    d.show_status()
    '''
    close = d.closure(Product("S'", '.S'))
    for i in close:
        print(i)
    print()
    go = d.goto(close, 'a')
    for i in go:
        print(i, len(i.right))
    a, b = set(), set()
    p1 = Product('S', 'A')
    p2 = Product('S', 'B')
    a.add(p1)
    a.add(p2)
    b.add(p1)
    b.add(p2)
    u = a - b
    for i in u:
        print(i)
    '''

