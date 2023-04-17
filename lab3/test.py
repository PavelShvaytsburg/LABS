# Импортируем класс Node из модуля btree_map
from main import BTree

tree = BTree()
tree.insert(1, 'a')
tree.insert(2, 'b')
tree.insert(3, 'c')
tree.update(2, 'd')
print(tree.search(1)) # Вывод: a
print(tree.search(2)) # Вывод: d
print(tree.search(3)) # Вывод: c