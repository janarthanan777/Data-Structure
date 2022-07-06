class Multistack:
    def __init__(self, elements):
        self.elements = elements
        self.noOfStacks = 3
        self.stack = [[0] * self.elements] * self.noOfStacks
    def full(self, stacknum):
        if self.stack[stacknum][self.elements - 1] != 0:
            return True
        else:
            return False
    def empty(self, stacknum):
        if  self.stack[stacknum][0] == 0:
            return True
        else:
            return False
    def index(self, stacknum):
        

    def push(self, stacknum, value):
        if self.full(stacknum):
            print('It is full')
        else:
            self.stack[stacknum][]

