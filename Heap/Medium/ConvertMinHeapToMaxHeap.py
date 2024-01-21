def min_heap_to_max_heap(heap):
    n = len(heap)

    def heapify(index):
        largest = index
        left_child = 2 * index + 1
        right_child = 2 * index + 2

        if left_child < n and heap[left_child] > heap[largest]:
            largest = left_child

        if right_child < n and heap[right_child] > heap[largest]:
            largest = right_child

        if largest != index:
            # Swap the values
            heap[index], heap[largest] = heap[largest], heap[index]
            heapify(largest)

    # Start from the last non-leaf node and perform heapify
    for i in range(n // 2 - 1, -1, -1):
        heapify(i)

# Example usage:
min_heap = [3, 5, 9, 6, 8, 20, 10, 12, 18, 9]
print("Min Heap:", min_heap)

min_heap_to_max_heap(min_heap)
print("Max Heap:", min_heap)
