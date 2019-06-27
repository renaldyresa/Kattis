class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    hls = ""
    def PrintTree(self):
        Node.hls += "l" if self.left else "n"
        Node.hls += "r" if self.right else "n"
        if self.left:
            self.left.PrintTree()
        if self.right:
            self.right.PrintTree()

byk, byk_node = map(int,input().split())
data = set()
for i in range(byk):
    nd = [int(x) for x in input().split()]
    root = Node(nd[0])
    for j in range(1,len(nd)):
        root.insert(nd[j])
    root.PrintTree()
    data.add(Node.hls)
    Node.hls = ""
print(len(data))
