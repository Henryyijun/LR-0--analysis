from grammar import *


class DFA:
    def __init__(self, g):
        '''
        引入新的开始符号S'
        :param g: Grammar
        '''
        self.i = []  # 保存活前缀DFA状态

        self.grammar = Grammar()
        self.grammar.start = "S'"
        self.grammar.Vn = g.Vn
        self.grammar.Vn.add("S'")
        self.grammar.Vt = g.Vt
        self.grammar.P.append(Product("S'", '.S'))
        for i in range(len(g.P)):
            r = '.' + g.P[i].right
            self.grammar.P.append(Product(g.P[i].left, r))

    def closure(self, p):
        '''
        求每一条产生式的闭包
        :param p: Product
        :return:
        '''
        close = []
        close.append(p)
        for i in close:
            position = i.right.find('.')
            if 0 <= position < len(i.right) - 1:
                if i.right[position + 1] in self.grammar.Vn:
                    c = i.right[position + 1]
                    for item in self.grammar.P:
                        if c == item.left:
                            close.append(item)
        return close

    def dfa(self):
        close = self.closure(Product("S'", '.S'))
        self.i.append(close)




