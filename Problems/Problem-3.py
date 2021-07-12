# This problem was asked by Google.

# Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

# For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __repr__(self):
        return str(self.data)

# The following test should pass:

node = Node(val='root', left=Node(val='left', left=Node('left.left')), right=Node('right'))

string = []

def serialize(string, node):
    if not root:
        return None
    
    serialized_tree_map = dict()
    serialized_left = serialize(root.left)
    serialized_right = serialize(root.right)

    serialized_tree_map['data'] = root.data
    

def deserialize(string):
    for item in string:
        if item = "left"


    print(node)


print("serialize:")
string = serialize(string, node)
print(string)

print("deserialize:")
tree = deserialize(string)
print(tree)

print("assert:")
assert deserialize(serialize(string, node)).left.left.val == 'left.left'