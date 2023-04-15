class HashMap:
    def __init__(self, capacity=10, load_factor=0.75):
        # конструктор класса, создает пустую хеш-таблицу с заданным начальным размером capacity и коэффициентом загруженности load_factor
        self.capacity = capacity
        self.load_factor = load_factor
        self.size = 0
        self.buckets = [[] for _ in range(capacity)]

    def __setitem__(self, key, value):
        # добавляет пару ключ-значение в хеш-таблицу. Если ключ уже присутствует в хеш-таблице, то его значение заменяется на новое.
        index = hash(key) % self.capacity
        for kvp in self.buckets[index]:
            if kvp[0] == key:
                # если ключ уже есть в списке, заменяем значение
                kvp[1] = value
                return
        # если ключа нет в списке, добавляем его
        self.buckets[index].append([key, value])
        self.size += 1
        if self.size > self.capacity * self.load_factor:
            # если коэффициент загруженности больше заданного, перехешируем все элементы
            self.rehash()

    def __getitem__(self, key):
        # получает значение по ключу из хеш-таблицы. Если ключ не найден в хеш-таблице, то возбуждается исключение KeyError
        index = hash(key) % self.capacity
        for kvp in self.buckets[index]:
            if kvp[0] == key:
                return kvp[1]
        raise KeyError(key)

    def __delitem__(self, key):
        # удаляет элемент из хеш-таблицы по ключу. Если ключ не найден в хеш-таблице, то возбуждается исключение KeyError
        index = hash(key) % self.capacity
        for i, kvp in enumerate(self.buckets[index]):
            if kvp[0] == key:
                del self.buckets[index][i]
                self.size -= 1
                return
        raise KeyError(key)

    def __len__(self):
        # возвращает количество элементов в хеш-таблице
        return self.size

    def __load_factor__(self):
        # возвращает текущий коэффициент загруженности хеш-таблицы
        print(self.size, self.capacity)
        return self.size / self.capacity

    def rehash(self):
        # перехеширует все элементы, увеличивая размер хеш-таблицы вдвое
        new_capacity = self.capacity * 2
        new_buckets = [[] for _ in range(new_capacity)]
        for bucket in self.buckets:
            for kvp in bucket:
                index = hash(kvp[0]) % new_capacity
                new_buckets[index].append(kvp)
        self.capacity = new_capacity
        self.buckets = new_buckets