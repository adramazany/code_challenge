class Node:
    def __init__(self, parent):
        self.parent = parent
        self.data = None
        self.left = None
        self.right = None

def create_perfect_binary_tree_postorder(parent,h,i):
    node =Node(parent)
    if h>1:
        node.left, l = create_perfect_binary_tree_postorder(node,h-1,i)
        node.right, r = create_perfect_binary_tree_postorder(node,h-1,l)
        node.data=r
        i=r
    else:
        node.data=i
    return node,i+1

def traverse_postorder(node):
    if node.left:
        traverse_postorder(node.left)
    if node.right:
        traverse_postorder(node.right)
    print("%s,"%node.data)

root,last = create_perfect_binary_tree_postorder(None,4,1)
print(last)
traverse_postorder(root)
