class Node:
    def __init__(self, v, k):
        self.value = v
        self.node_kind = k
        self.children = []

    def __str__(self):
        return self.value + ' ' + self.node_kind + ' '


class Tree:
    def __init__(self, g):
        pass

    def check(self, left, nodes):
        for i in range(len(nodes)):
            if left == nodes[i].value:
                return i
        return -1

    def create(self, g):
        root = Node(g.start, g.type(g.start))
        nodes = []
        nodes.append(root)
        for item in g.P:
            index = self.check(item.left, nodes)
            n = nodes[index]
            if index != -1:
                nodes.pop(index)
                for char in item.right:
                    temp = Node(char, g.type(char))
                    n.children.append(temp)
                    if temp.node_kind == 'Vn':
                        nodes.insert(0, temp)
                for i in nodes:
                    print(i)
        return root

    def create_p(self, g, p):
        root = Node(g.start, g.type(g.start))
        nodes = []
        nodes.append(root)
        for item in p:
            index = self.check(item.left, nodes)
            n = nodes[index]
            if index != -1:
                nodes.pop(index)
                for char in item.right:
                    temp = Node(char, g.type(char))
                    n.children.append(temp)
                    if temp.node_kind == 'Vn':
                        nodes.insert(0, temp)
                for i in nodes:
                    print(i)
        return root

    def print_tree(self, root):
        if root is not None and root.node_kind == 'Vn' and root != '`':
            if len(root.children) > 0:
                print(root.value, '(', end='')
                for n in root.children:
                    self.print_tree(n)
                print(')', end='')
            else:
                print(root.value, end='')
        elif root is not None and root.node_kind == 'Vt' and root.value != '`':
            print(root.value, end='')
