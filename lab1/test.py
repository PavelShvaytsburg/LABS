from main import PriorityQueue
# Создание объекта priority_queue
pq = PriorityQueue()

# Проверка на пустоту
print(pq.is_empty())

# Добавление элементов в priority_queue
pq.add(5)
pq.add(10)
pq.add(3)

# Получение максимального элемента
print(pq.max())  # 10

# Удаление максимального элемента
pq.delete()
print(pq.max())  # 5

# Получение размера очереди
print(pq.size())

# Проверка на пустоту
print(pq.is_empty())
