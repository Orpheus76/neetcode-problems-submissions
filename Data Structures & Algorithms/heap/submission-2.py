class MinHeap:
    def __init__(self):
        self.heap = [0]

    def push(self, val: int) -> None:
        self.heap.append(val)
        i = len(self.heap) - 1
        while i > 1:
            parent = i // 2
            if self.heap[i] < self.heap[parent]:
                self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
                i = parent
            else:
                break

    def pop(self) -> int:
        if len(self.heap) <= 1:
            return -1
        if len(self.heap) == 2:
            return self.heap.pop()

        res = self.heap[1]
        self.heap[1] = self.heap.pop()
        self._bubble_down(1)  # Utilisation de la méthode commune
        return res  # Ne pas oublier de retourner la valeur !

    def top(self) -> int:
        return self.heap[1] if len(self.heap) > 1 else -1

    def heapify(self, nums: List[int]) -> None:
        self.heap = [0] + nums
        # On part du dernier parent et on remonte (-1) jusqu'à 1
        for i in range((len(self.heap) - 1) // 2, 0, -1):
            self._bubble_down(i)

    def _bubble_down(self, i: int) -> None:
        """Méthode auxiliaire pour faire descendre un élément"""
        while 2 * i < len(self.heap):
            left = 2 * i
            right = 2 * i + 1
            smallest = left

            if right < len(self.heap) and self.heap[right] < self.heap[left]:
                smallest = right

            if self.heap[i] > self.heap[smallest]:
                self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
                i = smallest
            else:
                break
