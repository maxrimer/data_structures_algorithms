# Creating a tree using lists

class TreeNode:
    def __init__(self, data, children=[]):
        self.data = data
        self.children = children

    def __str__(self, level=0):
        ret = ' ' * level + str(self.data) + '\n'
        for child in self.children:
            ret += child.__str__(level+1)
        return ret

    def add_child(self, treenode):
        self.children.append(treenode)


tree = TreeNode('Drinks', [])
cold = TreeNode('Cold', [])
hot = TreeNode('Hot', [])
tree.add_child(cold)
tree.add_child(hot)
fanta = TreeNode('Fanta', [])
cola = TreeNode('Coca Cola', [])
tea = TreeNode('Tea', [])
coffee = TreeNode('Coffee', [])
cold.add_child(fanta)
cold.add_child(cola)
hot.add_child(tea)
hot.add_child(coffee)
print(tree)