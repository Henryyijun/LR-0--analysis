from lr import *
from slr import *

if __name__ == '__main__':
    g = Grammar()
    g.create('product.txt')
    '''
    p = lr.g.P
    
    tree = Tree(g)
    tree.print_tree(root)
    lr = LR(g)
    dfa = lr.dfa
    dfa.show_i()
    dfa.show_status()
    root = lr.lr_parsing('acb#')
    tree = Tree(g)
    tree.print_tree(root)
    '''
    lr = SLR(g)
    dfa = lr.dfa
    dfa.show_i()
    dfa.show_status()
    root = lr.slr_parsing('aacbb#')
    tree = Tree(g)
    print('语法树为:', end=' ')
    tree.print_tree(root)
