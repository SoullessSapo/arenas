
class Heap:
    #config : True // Max_Heap
    #config : False // Min_heap
    def __init__(self, data = [], config = True):
        self.data = []
        self.config = config
        self.build(data[:])
    def left(self, index):
        return 2*index +1
    def right(self, index):
        return 2 * (index + 1)
    def parent(self, index):
        return (index-1) // 2
    def height(self):
        return math.ceil(math.log(len(self.data), 2))
    def __len__(self):
        return len(self.data)
    def insert(self, new):
        self.data.append(new)
        self.build()
    def update(self, old, new):
        self.delete(old)
        self.insert(new)
    def delete(self, to_delete):
        if len(self) == 0:
            raise Exception("El montón está vacio")
        if to_delete not in self.data:
            raise Exception("El elemento no está en el montón")
        self.data.remove(to_delete)
        self.build()
    def build(self, data = []):
        if data and len(data) > 0 and isinstance(data, list):
            self.data = data
        for index in range(len(self)//2, -1, -1):
            self.heapify(index)
    def heapify(self, index):
        if self.config:
            self.max_heapify(index)
        else:
            self.min_heapify(index)
    def max_heapify(self, index):
        left_index, right_index, largest_index = self.left(index), self.right(index), index
        if left_index < len(self) and self.data[largest_index] < self.data[left_index]:
            largest_index = left_index
        if right_index < len(self) and self.data[largest_index] < self.data[right_index]:
            largest_index = right_index
        if largest_index != index:
            self.data[largest_index], self.data[index] = self.data[index], self.data[largest_index]
            self.max_heapify(largest_index)

    def peek(self):
        return self.data[0]
    def rightymaxi(self):
        return self.data[len(self)-1]

    def min_heapify(self, index):
        left_index, right_index, minimal_index = self.left(index), self.right(index), index
        if left_index < len(self) and self.data[minimal_index] > self.data[left_index]:
            minimal_index = left_index
        if right_index < len(self) and self.data[minimal_index] > self.data[right_index]:
            minimal_index = right_index
        if minimal_index != index:
            self.data[minimal_index], self.data[index] = self.data[index], self.data[minimal_index]
            self.min_heapify(minimal_index)
    def saca_maximo(self):
        self.max_heapify(0)
        return self.data[0]

    def heapsort(self):
        n = len(self)
        for i in range(n - 1, 0, -1):
            self.data[i], self.data[0] = self.data[0], self.data[i]
            n -= 1
            if self.config:
                self.max_heapify(0)
            else:
                self.min_heapify(0)

    def __str__(self):
        return str(self.data)


class PriorityQueue:
    def __init__(self, data=[], config=True):
        self.data = Heap(data, config)

    def __str__(self):
        return str(self.data)

    def __len__(self):
        return len(self.data)

    def enqueue(self, new):
        self.data.insert(new)

    def dequeue(self):
        if len(self) == 0:
            raise Exception("Underflow")
        to_dequeue = self.data.peek()
        self.data.delete(to_dequeue)
        return to_dequeue





def main():
    lis = "a"
    r = []
    while lis:
        lis = input("?")
        if lis.isdigit():
            r.append(int(lis))
        else:
            print(Heap.saca_maximo(Heap(lis)))

main()