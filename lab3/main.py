class BTreeNode:
    def __init__(self, leaf=False):
        self.leaf = leaf
        self.keys = []
        self.values = []
        self.children = []

    def split_child(self, i, child):
        new_node = BTreeNode(leaf=child.leaf)
        self.children.insert(i + 1, new_node)
        self.keys.insert(i, child.keys[2])
        self.values.insert(i, child.values[2])
        new_node.keys = child.keys[3:]
        new_node.values = child.values[3:]
        child.keys = child.keys[:2]
        child.values = child.values[:2]
        if not child.leaf:
            new_node.children = child.children[3:]
            child.children = child.children[:3]

    def insert_non_full(self, key, value):
        i = len(self.keys) - 1
        if self.leaf:
            self.keys.append(None)
            self.values.append(None)
            while i >= 0 and key < self.keys[i]:
                self.keys[i + 1] = self.keys[i]
                self.values[i + 1] = self.values[i]
                i -= 1
            self.keys[i + 1] = key
            self.values[i + 1] = value
        else:
            while i >= 0 and key < self.keys[i]:
                i -= 1
            i += 1
            if len(self.children[i].keys) == 4:
                self.split_child(i, self.children[i])
                if key > self.keys[i]:
                    i += 1
            self.children[i].insert_non_full(key, value)

    def search(self, key):
        i = 0
        while i < len(self.keys) and key > self.keys[i]:
            i += 1
        if self.keys[i] == key:
            return self.values[i]
        if self.leaf:
            return None
        return self.children[i].search(key)


class BTree:
    def __init__(self):
        self.root = BTreeNode(leaf=True)

    def insert(self, key, value):
        if len(self.root.keys) == 4:
            new_root = BTreeNode()
            new_root.children.append(self.root)
            new_root.split_child(0, self.root)
            new_root.insert_non_full(key, value)
            self.root = new_root
        else:
            self.root.insert_non_full(key, value)

    def search(self, key):
        return self.root.search(key)

    def update(self, key, value):
        i = 0
        while i < len(self.root.keys) and key > self.root.keys[i]:
            i += 1
        if self.root.keys[i] == key:
            self.root.values[i] = value
        elif not self.root.leaf:
            self.root.children[i].update(key, value)
