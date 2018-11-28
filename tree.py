class node:
    def __init__(self, value=None):
        self.data = value
        self.left = None
        self.right = None


class tree:
    def __init__(self, rootvalue):
        node = Node(rootvalue)
        self.root = node


'''set current = root
    while(both child not empty)
    current + current left'''

'''parse tree'''
