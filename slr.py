from dfa import *
from syntax_tree import *


class SLR:
    def __init__(self, g):
        self.dfa = DFA(g)
        self.g = g
        self.dfa.dfa()
        self.action = self.dfa.action_table()
        self.goto = self.dfa.goto_table()



    def check(self, x):
        for i in self.g.P:
            if i.left == x and i.right == '`':
                return True
        return False

    def get_first(self, x):
        first = set()
        if x in self.g.Vt:
            first.add(x)
            return first

        if self.check(x):
            first.add('`')

        for it in self.g.P:
            if it.left == x:
                i = 0
                for c in it.right:
                    i += 1
                    temp = self.get_first(c)
                    if '`' in temp:
                        first = first | temp
                        if i == len(it.right):
                            first.add('`')
                    else:
                        first = first | temp
                        if '`' in first:
                            first.remove('`')
                        break
                    temp.clear()
        return first

    def get_follow(self, x):
        follow = set()
        if x == self.g.start:
            follow.add('#')
        for p in self.g.P:
            position = p.right.find(x)
            if position != -1 and position != len(p.right) - 1:
                temp = self.get_first(p.right[position + 1])
                if '`' in temp:
                    follow |= temp
                    if '`' in follow:
                        follow.remove('`')

                    temp2 = self.get_follow(p.left)
                    follow |= temp2
                else:
                    follow |= temp

        for p in self.g.P:
            if len(p.right) >= 2 and p.left != x:
                position = p.right.find(x)
                if position != -1 and position == len(p.right) - 1:
                    temp2 = self.get_follow(p.left)
                    follow |= temp2

        return follow

