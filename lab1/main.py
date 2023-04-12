class PriorityQueue:
    def __init__(self):
        self.container = []

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)

    def add(self, item):
        self.container.append(item)
        index = len(self.container) - 1
        while index > 0:
            parent = (index - 1) // 2
            if self.container[index] > self.container[parent]:
                self.container[index], self.container[parent] = \
                    self.container[parent], self.container[index]
                index = parent
            else:
                break

    def delete(self):
        if self.is_empty():
            return None
        if len(self.container) == 1:
            return self.container.pop()

        max_item = self.container[0]
        self.container[0] = self.container.pop()
        index = 0
        while True:
            left_child = 2 * index + 1
            right_child = 2 * index + 2
            largest = index
            if left_child < len(self.container) and \
               self.container[left_child] > self.container[largest]:
                largest = left_child
            if right_child < len(self.container) and \
               self.container[right_child] > self.container[largest]:
                largest = right_child
            if largest == index:
                break
            self.container[index], self.container[largest] = \
                self.container[largest], self.container[index]
            index = largest
        return max_item

    def max(self):
        if self.is_empty():
            return None
        return self.container[0]
