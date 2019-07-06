class Quadruple:
    '''
    四元式数据结构
    '''
    def __init__(self, op, arg1, arg2, result):
        self.op = op
        self.arg1 = arg1
        self.arg2 = arg2
        self.result = result

    def __str__(self):
        return '(' + str(self.op) + ',' + str(self.arg1) + ',' + str(self.arg2) + ',' + str(self.result) + ')'


