class RedBlackTreeMap:
    class _Node:
        def __init__(self, key, value, color):
            self.key = key
            self.value = value
            self.left = None
            self.right = None
            self.color = color

    def __init__(self):
        self.root = None
        self.size = 0

    def is_red(self, node):
        # Проверяет, является ли узел красным.
        if node is None:
            return False
        return node.color == 'red'

    def rotate_left(self, node):
        # Осуществляет левый поворот вокруг заданного узла.
        right = node.right
        node.right = right.left
        right.left = node
        right.color = node.color
        node.color = 'red'
        return right

    def rotate_right(self, node):
        # Осуществляет правый поворот вокруг заданного узла.
        left = node.left
        node.left = left.right
        left.right = node
        left.color = node.color
        node.color = 'red'
        return left

    def flip_colors(self, node):
        # Меняет цвета узлов.
        node.color = 'red'
        node.left.color = 'black'
        node.right.color = 'black'

    def put(self, key, value):
        # Добавляет новый узел с заданным ключом и значением.
        def _put(node, key, value):
            if node is None:
                self.size += 1
                return self._Node(key, value, 'red')

            if key < node.key:
                node.left = _put(node.left, key, value)
            elif key > node.key:
                node.right = _put(node.right, key, value)
            else:
                node.value = value

            if self.is_red(node.right) and not self.is_red(node.left):
                node = self.rotate_left(node)
            if self.is_red(node.left) and self.is_red(node.left.left):
                node = self.rotate_right(node)
            if self.is_red(node.left) and self.is_red(node.right):
                self.flip_colors(node)

            return node

        self.root = _put(self.root, key, value)
        self.root.color = 'black'

    def get(self, key):
        # Получает значение по заданному ключу.
        node = self.root
        while node is not None:
            if key < node.key:
                node = node.left
            elif key > node.key:
                node = node.right
            else:
                return node.value
        return None

    def __setitem__(self, key, value):
        # Позволяет использовать оператор [] для добавления нового узла с заданным ключом и значением.
        self.put(key, value)

    def __getitem__(self, key):
        # Позволяет использовать оператор [] для получения значения по заданному ключу.
        return self.get(key)

    def __len__(self):
        # Возвращает количество элементов в ассоциативном массиве.
        return self.size

    def __contains__(self, key):
        # Проверяет, содержится ли заданны
        return self.get(key) is not None