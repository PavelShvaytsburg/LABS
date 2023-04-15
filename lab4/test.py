from main import HashMap

hm = HashMap()
hm.__setitem__('a', 10)
hm.__setitem__('b', 34)
hm.__setitem__('c', 8)

print(hm.__getitem__('b'))
print(hm.__len__())

print(hm.__load_factor__())