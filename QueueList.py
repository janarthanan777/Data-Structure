class Queue:
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.list = self.maxsize * [None]
        self.start = -1
        self.top = -1
    def __str__(self):
        values = [str(x) for x in self.list[ self.maxsize: : -1]]
        return ' | '.join(values)
    def empty(self):
        if self.start == -1:
            return True
        else:
            return False
    def full(self):
        if self.start == 0 and self.top == self.maxsize -1:
            return True
        elif self.top + 1 == self.start:
            return True
        else:
            return False
    def enqueue(self, value):
        if self.full():
            print('It is full bhai, kya bharega aur')
        elif self.top + 1 == self.maxsize:
            self.top = 0
        elif self.top == -1 and self.start == -1:
            self.start =0
            self.top = 0
        else:
            self.top += 1
        self.list[self.top] = value
    def dequeue(self):
        if self.empty():
            print('Khaali hai bhai')
        elif self.start + 1 == self.maxsize:
            print(self.list[self.start])
            self.start = 0
        elif self.start == 0 and self.top == 0:
            self.start = -1
            self.top = -1
        else:
            self.start += 1
            print(self.list[self.start -1])
    def peek(self):
        if self.empty():
            print('Ena da ulla onnume illa')
        else:
            print(self.list[self.start])
    def delete(self):
        self.start = -1
        self.top = -1
        self.list = [None] * self.maxsize
q = Queue(5)
q.enqueue(44)
q.enqueue(43)
q.enqueue(42)
q.enqueue(41)
q.enqueue(40)

print(q)