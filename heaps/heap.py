class Heap:

    def __init__(self, l):
        self.tree = l
        self.heapify()

    def swap(self, idx1, idx2):
        value1 = self.tree[idx1]
        self.tree[idx1] = self.tree[idx2]
        self.tree[idx2] = value1

    # O(n)
    def heapify(self):
        starting_index = ((len(self.tree) - 1) // 2) - 1
        
        for i in range(starting_index, -1, -1):
            self.shift_down(i)

    # O(log(n))
    def shift_up(self, current_idx):
        if current_idx == 0:
            return
        
        parent_idx = (current_idx // 2) - 1

        if self.tree[current_idx] >= self.tree[parent_idx]:
            self.swap(current_idx, parent_idx)
            self.shift_up(parent_idx)

    # O(log(n))
    def shift_down(self, current_idx):
        left_idx = 2 * current_idx + 1
        right_idx = 2 * current_idx + 2

        largest_idx = current_idx
        if left_idx < len(self.tree) and self.tree[left_idx] >= self.tree[largest_idx]:
            largest_idx = left_idx
        
        if right_idx < len(self.tree) and self.tree[right_idx] >= self.tree[largest_idx]:
            largest_idx = right_idx
        
        if largest_idx != current_idx:
            self.swap(current_idx, largest_idx)
            self.shift_down(largest_idx)

    # O(log(n))
    def insert(self, value):
        self.tree.append(value)
        self.shift_up(len(self.tree) - 1)

    # O(log(n))
    def pop(self) -> int:
        if len(self.tree) == 0:
            raise IndexError("The heap is empty")
        
        value = self.tree[0]
        
        self.tree[0] = self.tree[-1]
        del self.tree[-1]
        self.shift_down(0)
        
        return value

    def __iter__(self):
        return iter(self.tree)
    
    def __len__(self):
        return len(self.tree)
