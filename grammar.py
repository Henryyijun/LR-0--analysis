
class Product:
    def __init__(self, l, r):
        self.left = l
        self.right = r

    def __str__(self):
        return self.left + '->' + self.right

    def __cmp__(self, other):
        return self.left == other.left and self.right == other.right

    def __hash__(self):
        return hash(id(self.left) + id(self.right))

    def __eq__(self, other):
        return self.left == other.left and self.right == other.right


class Grammar:
    def __init__(self):
        self.Vt = set()
        self.Vn = set()
        self.P = []
        self.start = None

    def create(self, file_name):
        flag = False
        with open(file_name) as f:
            for line in f:
                l = line.strip('\n')
                for char in line:
                    if str.isupper(char) and not flag:
                        self.start = char
                        flag = True
                        break
                    else:
                        continue

                position = l.find('->')
                p = Product(l[:position], l[position + 2:])
                self.P.append(p)

                for i in range(len(l)):
                    if (i == position) or (i == (position + 1)):
                        continue
                    elif str.isupper(l[i]):
                        self.Vn.add(l[i])
                    else:
                        self.Vt.add(l[i])

    def type(self,  symbol):
        if symbol in self.Vn:
            return 'Vn'
        elif symbol in self.Vt:
            return 'Vt'
