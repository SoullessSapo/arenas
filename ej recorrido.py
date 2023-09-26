class Node:

    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None

def buildTree(inn, pre, inStrt, inEnd):
    global preIndex, mp

    if (inStrt > inEnd):
        return None
    curr = pre[preIndex]
    preIndex += 1
    tNode = Node(curr)
    if (inStrt == inEnd):
        return tNode
    inIndex = mp[curr]

    tNode.left = buildTree(inn, pre, inStrt,
                           inIndex - 1)
    tNode.right = buildTree(inn, pre, inIndex + 1,
                            inEnd)

    return tNode

def buldTreeWrap(inn, pre, lenn):
    global mp

    for i in range(lenn):
        mp[inn[i]] = i

    return buildTree(inn, pre, 0, lenn - 1)

def printInorder(node):
    if (node == None):
        return

    printInorder(node.left)
    print(node.data, end=" ")
    printInorder(node.right)

if __name__ == '__main__':
    mp = {}
    preIndex = 0

    inn = ['D', 'B', 'E', 'A', 'F', 'C']
    pre = ['A', 'B', 'D', 'E', 'C', 'F']
    lenn = len(inn)

    root = buldTreeWrap(inn, pre, lenn)
    print("Inorder del "
          " arbol construido es")

    printInorder(root)