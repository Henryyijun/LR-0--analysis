from dfa import *

if __name__ == '__main__':
    g = Grammar()
    g.create('product.txt')
    lr = LR(g)
    root = lr.lr_parsing('aacbb#')
    tree = Tree(g)
    tree.print_tree(root)


