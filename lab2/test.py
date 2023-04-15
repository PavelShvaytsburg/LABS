from main import RedBlackTreeMap
rbt = RedBlackTreeMap()
rbt.put('a', 1)
rbt.put('b', 2)
rbt.put('c', 3)


print(rbt.get('a'))
print(rbt.get('c'))

rbt.put('c', 5)
print(rbt.get('c'))