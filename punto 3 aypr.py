class MinHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def left_child(self, i):
        return 2 * i + 1

    def right_child(self, i):
        return 2 * i + 2

    def heapify_up(self, i):
        while i > 0 and self.heap[i] < self.heap[self.parent(i)]:
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)

    def heapify_down(self, i):
        n = len(self.heap)
        smallest = i
        left = self.left_child(i)
        right = self.right_child(i)

        if left < n and self.heap[left] < self.heap[smallest]:
            smallest = left

        if right < n and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self.heapify_down(smallest)

    def heap_minimum(self):
        if len(self.heap) > 0:
            return self.heap[0]
        else:
            return None

    def heap_extract_min(self):
        if len(self.heap) == 0:
            return None

        minimum = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.heapify_down(0)
        return minimum

    def heap_decrease_key(self, i, new_value):
        if i >= len(self.heap):
            return

        if new_value > self.heap[i]:
            return

        self.heap[i] = new_value
        self.heapify_up(i)

    def min_heap_insert(self, value):
        self.heap.append(float('inf'))
        self.heap_decrease_key(len(self.heap) - 1, value)

    def is_max_heap(root):
        if root is None:
            return True

        queue = [root]

        while queue:
            node = queue.pop(0)
            if node.left:
                if node.left.value > node.value:
                    return False
                queue.append(node.left)
            if node.right:
                if node.right.value > node.value:
                    return False
                queue.append(node.right)




