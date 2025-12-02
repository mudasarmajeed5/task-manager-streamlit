"""
Custom Data Structures for Task Manager
Implements PriorityQueue and Stack using lists from scratch
"""

class PriorityQueue:
    """
    Min-heap based Priority Queue implementation
    Lower priority number = higher priority (1 is highest, 5 is lowest)
    """
    def __init__(self):
        self.heap = []
    
    def insert(self, task):
        """Insert a task into the priority queue"""
        self.heap.append(task)
        self._heapify_up(len(self.heap) - 1)
    
    def extract_min(self):
        """Remove and return the task with highest priority (lowest number)"""
        if not self.heap:
            return None
        
        if len(self.heap) == 1:
            return self.heap.pop()
        
        # Store the minimum element
        min_task = self.heap[0]
        
        # Move last element to root and heapify down
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        
        return min_task
    
    def peek(self):
        """Return the task with highest priority without removing it"""
        if not self.heap:
            return None
        return self.heap[0]
    
    def is_empty(self):
        """Check if the priority queue is empty"""
        return len(self.heap) == 0
    
    def size(self):
        """Return the number of tasks in the queue"""
        return len(self.heap)
    
    def get_all_tasks(self):
        """Return all tasks in the queue (not in order)"""
        return self.heap.copy()
    
    def _heapify_up(self, index):
        """Move element up to maintain heap property"""
        parent_index = (index - 1) // 2
        
        if index > 0 and self.heap[index]['priority'] < self.heap[parent_index]['priority']:
            # Swap with parent
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            self._heapify_up(parent_index)
    
    def _heapify_down(self, index):
        """Move element down to maintain heap property"""
        smallest = index
        left_child = 2 * index + 1
        right_child = 2 * index + 2
        
        # Compare with left child
        if left_child < len(self.heap) and self.heap[left_child]['priority'] < self.heap[smallest]['priority']:
            smallest = left_child
        
        # Compare with right child
        if right_child < len(self.heap) and self.heap[right_child]['priority'] < self.heap[smallest]['priority']:
            smallest = right_child
        
        # If smallest is not the current index, swap and continue heapifying
        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._heapify_down(smallest)


class Stack:
    """
    Stack implementation using list
    LIFO (Last In First Out) structure
    """
    def __init__(self):
        self.items = []
    
    def push(self, task):
        """Add a task to the top of the stack"""
        self.items.append(task)
    
    def pop(self):
        """Remove and return the task from the top of the stack"""
        if not self.is_empty():
            return self.items.pop()
        return None
    
    def peek(self):
        """Return the task at the top without removing it"""
        if not self.is_empty():
            return self.items[-1]
        return None
    
    def is_empty(self):
        """Check if the stack is empty"""
        return len(self.items) == 0
    
    def size(self):
        """Return the number of tasks in the stack"""
        return len(self.items)
    
    def get_all_tasks(self):
        """Return all tasks in the stack (in order)"""
        return self.items.copy()
