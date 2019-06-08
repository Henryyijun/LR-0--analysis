from lr import *
from slr import *

if __name__ == '__main__':
    g = Grammar()
    g.create('product.txt')
    '''
    lr = LR(g)
    root = lr.lr_parsing('aacbb#')
    tree = Tree(g)
    tree.print_tree(root)
    
    '''
    slr = SLR(g)
    first = slr.get_first('S')
    follow = slr.get_follow('S')
    print(first)
    print(follow)
