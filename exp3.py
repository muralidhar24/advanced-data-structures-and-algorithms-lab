class Heap:
    def __init__(self, is_min_heap=True):
        self.heap = []
        self.is_min_heap = is_min_heap 
    def _compare(self, parent, child):
        """Compare function to handle Min-Heap or Max-Heap logic."""
        if self.is_min_heap:
            return parent > child 
        else:
            return parent < child 

    def _heapify_up(self, index):
        """Restore heap property moving upwards."""
        parent_index = (index - 1) // 2
        if index > 0 and self._compare(self.heap[parent_index], self.heap[index]):
            # Swap if parent violates the heap property
            self.heap[parent_index], self.heap[index] = self.heap[index], self.heap[parent_index]
            self._heapify_up(parent_index)

    def _heapify_down(self, index):
        """Restore heap property moving downwards."""
        left_child = 2 * index + 1
        right_child = 2 * index + 2
        smallest_or_largest = index

        # Compare left child
        if left_child < len(self.heap) and self._compare(self.heap[smallest_or_largest], self.heap[left_child]):
            smallest_or_largest = left_child

        # Compare right child
        if right_child < len(self.heap) and self._compare(self.heap[smallest_or_largest], self.heap[right_child]):
            smallest_or_largest = right_child

        # If heap property is violated, swap and continue heapifying down
        if smallest_or_largest != index:
            self.heap[index], self.heap[smallest_or_largest] = self.heap[smallest_or_largest], self.heap[index]
            self._heapify_down(smallest_or_largest)

    def insert(self, value):
        """Insert a value into the heap."""
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def delete(self, value):
        """Delete an element from the heap."""
        try:
            index = self.heap.index(value)
            # Replace the element to delete with the last element
            self.heap[index] = self.heap[-1]
            self.heap.pop()
            # Restore heap property
            if index < len(self.heap):
                self._heapify_down(index)
                self._heapify_up(index)
        except ValueError:
            print(f"Value {value} not found in the heap.")

    def display(self):
        """Display the heap."""
        print("Heap contents:", self.heap)

# Example Usage
if __name__ == "__main__":
    print("Min-Heap Operations:")
    min_heap = Heap(is_min_heap=True)
    min_heap.insert(10)
    min_heap.insert(20)
    min_heap.insert(5)
    min_heap.insert(15)
    min_heap.display()

    min_heap.delete(10)
    print("After deleting 10:")
    min_heap.display()

    print("\nMax-Heap Operations:")
    max_heap = Heap(is_min_heap=False)
    max_heap.insert(10)
    max_heap.insert(20)
    max_heap.insert(5)
    max_heap.insert(15)
    max_heap.display()

    max_heap.delete(20)
    print("After deleting 20:")
    max_heap.display()