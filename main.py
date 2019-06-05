from dfa import *

if __name__ == '__main__':
    g = Grammar()
    g.create('product.txt')

    lr = LR(g)
    lr.lr_parsing('acb#')
    '''
    close = d.closure(Product("S'", '.S'))
    for i in close:
        print(i)
    print()
    d.dfa()
    d.show_i()
    d.show_status()
    d.action_table()
    d.goto_table()
    '''

