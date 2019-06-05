from grammar import *


class Transition:
    def __init__(self, sn, s, x, en, e):
        '''

        :param sn: 开始状态编号
        :param s: 开始状态集合
        :param x: 输入的字符
        :param en: 转变后的状态编号
        :param e: 转变后的状态集合
        '''
        self.start_num = sn
        self.start = set()
        self.start |= s
        self.x = x
        self.end = set()
        self.end_num = en
        self.end |= e

    def __str__(self):
        return '初始状态：编号为{a}, {b}'.format(a=self.start_num, b=[str(i) for i in self.start]) + '输入字符:' + self.x + ' 转变后的状态:编号为{a}, {b}'.format(a=self.end_num, b=[str(i) for i in self.end])


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
        self.p = g.P
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
                        if c == item.left and item not in close:
                            close.append(item)
        return close

    def goto(self, i, x):
        '''
        :param i: is a set of items
        :param x: is a grammar symbol
        :return:a new set of items, 在状态i下输入符号x转变成新的状态集合
        '''
        new_i = set()
        for item in i:
            position = item.right.find('.')
            if position == len(item.right) - 1:
                continue
            elif 0 <= position < len(item.right) - 1 and item.right[position + 1] == x:
                temp = item.right[:position] + item.right[position + 1] + '.' + item.right[position + 2:]
                p = Product(item.left, temp)
                new_i.add(p)
                close = self.closure(p)
                close = set(close)
                new_i = new_i | close
        return new_i

    @staticmethod
    def is_in_i(items, i):
        '''
        检查当前状态集合是否已经存在
        :param items: 项目集合，
        :param i:
        :return: 存在返回true，否则返回 false
        '''
        for item in i:
            if len(item) == len(items):
                u = items - item
                if len(u) == 0:
                    return True
        return False

    def dfa(self):
        '''
        构造活前缀DFA
        :return:  活前缀DFA
        '''
        close = self.closure(Product("S'", '.S'))
        symbols = self.grammar.Vn | self.grammar.Vt
        symbols.remove("S'")
        symbols = list(symbols)
        symbols.sort()
        print(symbols)
        self.i.append(set(close))
        for items in self.i:
            for x in symbols:
                temp = self.goto(items, x)
                if len(temp) > 0:
                    if not self.is_in_i(temp, self.i):  # 不存在添加
                        self.i.append(temp)
                        sn = self.i.index(items)
                        en = self.i.index(temp)
                        t = Transition(sn, items, x, en, temp)
                        self.status.append(t)
                    else:
                        sn = self.i.index(items)
                        en = self.i.index(temp)
                        t = Transition(sn, items, x, en, temp)
                        self.status.append(t)

    def action(self, i, a):
        '''
        :param i: 状态i
        :param a: 输入字符
        :return: 返回移进 或者是 规约
        '''

    def action_table(self):
        '''
        构造LR(0) 分析表的aciton表
        :return: action 表
        采取的存储形式: index 为状态号 [{a:s1},... {#:acc}] 这种存储形式
        [[{a:s1},... {#:acc}],
        [{a:s1},... {#:acc}],
        [{a:s1},... {#:acc}]]
        '''
        terminal = list(self.grammar.Vt)
        terminal.append('#')
        print()
        terminal.sort()
        print(terminal)
        table = [[] for row in range(len(self.i))]  # 二维列表 存储action
        for item in self.status:
            sn = item.start_num
            en = item.end_num
            x = item.x
            if x in self.grammar.Vt:
                table[sn].append({x: 's' + str(en)})

        for item in self.i:
            for i in item:
                if i.right.find('.') == len(i.right) - 1 and (i.left != "S'" and i.right != 'S.'):
                    p = Product(i.left, i.right.strip('.'))
                    j = self.p.index(p)
                    for s in terminal:
                        table[self.i.index(item)].append({s: 'r' + str(j)})
                elif i.right.find('.') == len(i.right) - 1 and (i.left == "S'" and i.right == 'S.'):
                    table[self.i.index(item)].append({'#': 'acc'})
        count = 0
        for i in table:
            print(count, i)
            count += 1
        return table

    def goto_table(self):
        non_terminal = list(self.grammar.Vn)
        non_terminal.remove("S'")
        print()
        non_terminal.sort()
        print(non_terminal)
        table = [[] for row in range(len(self.i))]
        for item in self.status:
            sn = item.start_num
            en = item.end_num
            x = item.x
            if x in self.grammar.Vn:
                table[sn].append({x : en})
        count = 0
        for i in table:
            print(count, i)
            count += 1
        return table

    def show_i(self):
        for items in self.i:
            for item in items:
                print(item, end=' ')
            print()

    def show_status(self):
        for i in self.status:
            print(i)
            print()



