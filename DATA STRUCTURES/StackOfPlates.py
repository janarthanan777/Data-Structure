class StackOfPlates:
    def __init__(self, x):
        self.elements = x
        self.stack = []

    def push(self, value):
        if self.stack == []:
            self.stack.append([value])
        elif len(self.stack[-1]) == self.elements:
            self.stack.append([value])
        else:
            self.stack[-1].append(value)
    def pop(self):
        if self.stack == []:
            print('Ulla onnume illa da')
        popped_data = self.stack[-1][-1]
        if len(self.stack[-1]) == 1:
            del self.stack[-1]
        else:
            del self.stack[-1][-1]
        print(popped_data)
SOP = StackOfPlates(4)
SOP.push(10)
SOP.push(3)
SOP.push(2)
SOP.push(11)
SOP.pop()
SOP.pop()
