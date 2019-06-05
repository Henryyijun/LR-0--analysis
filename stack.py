class Stack:
    def __init__(self):
        self.__list = list()
        self.index = 0

    def __str__(self):
        return '[{}]'.format(str(i) for i in self.__list)

    def __next__(self):
        if self.index < len(self.__list):
            self.index += 1
            return self.__list[self.index]

    def __iter__(self):
        if self.index < len(self.__list):
            self.index += 1
            return iter(self.__list)

    def push(self, o):
        self.__list.append(o)

    def pop(self):
        return self.__list.pop(-1)

    def top(self):
        return self.__list[len(self.__list) - 1]

    def size(self):
        return len(self.__list)

