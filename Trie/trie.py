# creating and initializing trienode and trie classes

class TrieNode:
    def __init__(self):
        self.children = {}
        self.endofstring = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insertstring(self, word):
        current = self.root
        for ch in word:
            node = current.children.get(ch)
            if node == None:
                node = TrieNode()
                current.children.update({ch: node})
            current = node
        current.endofstring = True
        print('The word has been successfully inserted')

    def searchstring(self, word):
        current = self.root
        for ch in word:
            node = current.children.get(ch)
            if node == None:
                return False
            current = node

        if current.endofstring:
            return True
        return False


def deletestring(root, word, index):
    ch = word[index]
    currentnode = root.children.get(ch)
    canthisnodebedeleted = False

    if len(currentnode.children) > 1:
        deletestring(currentnode, word, index+1)
        return False

    if index == len(word) - 1:
        if len(currentnode.children) >= 1:
            currentnode.endofstring = False
            return False
        else:
            root.children.pop(ch)
            return True

    if currentnode.endofstring:
        deletestring(root, word, index+1)
        return False

    canthisnodebedeleted = deletestring(currentnode, word, index+1)
    if canthisnodebedeleted:
        root.children.pop(ch)
        return True
    else:
        return False


newtrie = Trie()
newtrie.insertstring('App')
newtrie.insertstring('Appl')
newtrie.insertstring('Ball')
print(deletestring(newtrie.root, 'Ball', 0))
# print(newtrie.searchstring('Appl'))