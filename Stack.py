class Stack:
    class Node:
        def __init__(self, val, next=None):
            self.val = val
            self.next = next
        def __str__(self):
            return str(self.val)
        def __repr__(self):
            return str(self)

    def __init__(self):
        self.top = None

    def push(self, val):
        self.top = Stack.Node(val, self.top)

    def pop(self):
        assert self.top, 'Stack is empty'
        val = self.top.val
        self.top = self.top.next
        return val

    def peek(self):
        return self.top.val if self.top else None

    def empty(self):
        return self.top == None

    def __bool__(self):
        return not self.empty()

    def __repr__(self):
        if not self.top:
            return ''
        return '--> ' + ', '.join(str(x) for x in self)

    def __iter__(self):
        n = self.top
        while n:
            yield n.val
            n = n.next

    def remove_all(self, val):
        while self.top and self.top.val == val:
            self.top = self.top.next
        n = self.top
        while n:
            if n.next and n.next.val == val:
                n.next = n.next.next
            else:
                n = n.next

    def roll(self,idx):
        p = self.top
        for i in range(0,idx):
            p = p.next
        self.top.next, self.top, p.next = p.next, self.top.next, self.top
