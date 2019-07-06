from dfa import *
from syntax_tree import *
from quadruple import *



temp = [0 for i in range(100)] #临时变量编号
quadruples = [] #四元式列表
symbol = {0: '_'} #符号表
symbol_place = 1
temp_place = -1


def gen(op, arg1, arg2, result):
    q = Quadruple(op, symbol[arg1], symbol[arg2], symbol[result])
    quadruples.append(q)
    return len(quadruples)


def new_temp():
    for i in range(100):
        if temp[i] == 0:
            temp[i] = -(i + 1) # < 0 表示临时变量
            return temp[i]


def lookup(name):
    '''
    以Name查符号表，若查到则返回相应登记项的序号(≥1),否则返回0。
    :param name:
    :return:
    '''
    for i, e in enumerate(symbol):
        if e == name:
            return i
    return 0

def enter(name):
    keys = list(symbol.keys())
    keys.sort()  #对编号排序
    num = keys[len(keys) - 1] + 1   #找到最大编号并且加1
    symbol.update({num: name})
    return num


def entry(name):
    i = lookup(name)
    if i != 0:
        return i
    else:
        return enter(name)


class SLR:
    def __init__(self, g):
        self.dfa = DFA(g)
        self.g = g
        self.dfa.dfa()
        self.action = self.dfa.slr_action_table()
        self.goto = self.dfa.goto_table()

    def slr_parsing(self, string):
        global symbol_place
        global temp_place
        tree = Tree(self.g)
        ps = []
        stack = []
        stack.append(0)
        symbols = []
        symbols.append('#')
        index = 0
        p = Product('', '')
        iter = -1
        s = string.strip('#')
        node_num = len(s)
        nodes = []
        for i in range(node_num):
            nodes.append(Node(s[i], 'Vt'))
        while True:
            print(stack, symbols, p)
            a = string[index]
            s = stack[len(stack) - 1]
            t = self.action[s].get(a, ' ')
            if t != ' ' and t[0] == 's':
                stack.append(int(t[1:]))
                symbols.append(a)
                index += 1
                iter += 1

            elif t != ' ' and t[0] == 'r':
                p = self.dfa.p[int(t[1:])]
                pos = int(t[1:])
                leng = len(p.right)
                for i in range(leng):
                    symbols.pop()
                    stack.pop()
                temp = stack[len(stack) - 1]
                goto = self.goto[temp].get(p.left, ' ')
                ps.append(p)
                if goto != ' ':
                    stack.append(goto)
                    symbols.append(p.left)

                iter = iter - len(p.right) + 1
                node = Node(p.left, 'Vn')
                for i in range(len(p.right)):
                    node.children.append(nodes[iter + i])

                for i in range(iter + 1, node_num - len(p.right) + 1):
                    nodes[i] = nodes[i + len(p.right) - 1]

                node_num = node_num - len(p.right) + 1
                nodes[iter] = node
                if pos == 0:
                    quadruples.append(Quadruple(node.children[1].value, node.children[2].place, 0,
                                                node.children[0].place))
                elif pos == 1 or pos == 2 or pos == 4 or pos == 5:
                    node = nodes[iter]
                    t1 = new_temp()
                    t = 't' + str(abs(t1))
                    symbol.update({t1: t})
                    quadruples.append(Quadruple(node.children[1].value, node.children[0].place,
                                                node.children[2].place, t1))
                    nodes[iter].place = t1
                elif pos == 3 or pos == 6 or pos == 8:
                    nodes[iter].place = nodes[iter].children[0].place
                elif pos == 7:
                    nodes[iter].place = nodes[iter].children[1].place
                elif pos >= 9:
                    t = nodes[iter].children[0].value
                    s1 = entry(t)
                    symbol.update({s1: t})
                    nodes[iter].place = s1
            elif t != ' ' and t == 'acc':
                    print('分析成功')
                    break
            else:
                print('分析失败')
                break
        ps.reverse()

        root = tree.create_p(self.g, ps)
        return root



