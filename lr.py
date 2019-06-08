from syntax_tree import *
from dfa import *


class LR:
    def __init__(self, g):
        self.dfa = DFA(g)
        self.g = g
        self.dfa.dfa()
        self.action = self.dfa.action_table()
        self.goto = self.dfa.goto_table()

    def lr_parsing(self, string):
        tree = Tree(self.g)
        ps = []
        stack = []
        stack.append(0)
        symbols = []
        symbols.append('#')
        index = 0
        p = Product('', '')
        while True:
            print(stack, symbols, string[index:], p)
            a = string[index]
            s = stack[len(stack) - 1]
            t = self.action[s].get(a, ' ')
            if t != ' ' and t[0] == 's':
                stack.append(int(t[1:]))
                symbols.append(a)
                index += 1
            elif t != ' ' and t[0] == 'r':
                p = self.dfa.p[int(t[1:])]
                length = len(p.right)
                for i in range(length):
                    symbols.pop()
                    stack.pop()
                temp = stack[len(stack) - 1]
                goto = self.goto[temp].get(p.left, ' ')
                ps.append(p)
                if goto != ' ':
                    stack.append(goto)
                    symbols.append(p.left)
            elif t != ' ' and t == 'acc':
                print('分析成功')
                break
            else:
                print('分析失败')
                break
        ps.reverse()
        root = tree.create_p(self.g, ps)
        return root
