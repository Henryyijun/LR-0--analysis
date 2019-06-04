from grammar import *


class DFA:
    def __init__(self, g):
        '''
        引入新的开始符号S'
        :param g: Grammar
        S'->.S
        S->.A
        A->.aAb
        S->.B
        B->.aBb
        B->.d
        A->.c

        self.i: 保存活前缀DFA状态, 每个状态是一个基础项目的集合。
        例如：
        i[0] = {A->.aAb,A->.c,S->.B, S'->.S, B->.aBb,B->.d,S->.A}

        self.status: 状态迁移列表， 例如 I0 读取字符a -> I1
        则有 字典d = {(I0, a): I1}
        self.status.append(d)
        self.status = [{(I0, a): I1}]
        '''

        self.i = []
        self.status = []
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
        :return: 闭包
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
        '''
        构造活前缀DFA
        :return:  活前缀DFA
        '''
        close = self.closure(Product("S'", '.S'))
        self.i.append(set(close))
        for item in self.i:
            pass




