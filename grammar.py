
class Product:
    def __init__(self, l, r):
        self.left = l
        self.right = r

    def __str__(self):
        if len(self.left) > 0 and len(self.right) > 0:
            return self.left + '->' + self.right
        return ''

    def __hash__(self):
        return hash(hash(hash(self.left)) + hash(hash(self.right)))

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.left == other.left) and (self.right == other.right)
        else:
            return False


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
