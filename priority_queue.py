class Task:
    def __init__(self, task_id, priority, arrival_time, deadline):
        """
        Initialize a new task with its ID, priority, arrival time, and deadline.

        Args:
        - task_id (str): A unique identifier for the task.
        - priority (int): The priority of the task, where a higher number means higher priority.
        - arrival_time (float): The time when the task arrived in the system.
        - deadline (float): The deadline by which the task should be completed.
        """
        self.task_id = task_id
        self.priority = priority
        self.arrival_time = arrival_time
        self.deadline = deadline

    def __lt__(self, other):
        """
        Overriding the less-than operator to compare two tasks.
        This is used by the heap to maintain the order of elements.
        For a max-heap, we return True if self has a higher priority than other.
        
        Args:
        - other (Task): The other task to compare against.

        Returns:
        - bool: True if self has higher priority, False otherwise.
        """
        return self.priority > other.priority

    def __repr__(self):
        """
        Provides a string representation of the task for easier debugging and logging.
        
        Returns:
        - str: A string describing the task.
        """
        return f"Task(ID: {self.task_id}, Priority: {self.priority}, Arrival: {self.arrival_time}, Deadline: {self.deadline})"


class MaxHeap:
    def __init__(self):
        """
        Initialize an empty max-heap using a list.
        """
        self.heap = []

    def insert(self, task):
        """
        Insert a new task into the heap while maintaining the max-heap property.

        Args:
        - task (Task): The task to insert into the heap.

        Time Complexity:
        - O(log n) due to the up-heap operation to maintain the heap property.
        """
        # Add the new task to the end of the heap
        self.heap.append(task)
        # Restore the heap property by moving the task up
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, index):
        """
        Helper method to move the element at the given index up to its correct position in the heap.

        Args:
        - index (int): The index of the element to move up in the heap.
        
        Time Complexity:
        - O(log n) in the worst case, where n is the number of elements in the heap.
        """
        # Move up the tree until the heap property is restored
        while index > 0:
            # Calculate the parent index
            parent_index = (index - 1) // 2
            # If the current node is greater than its parent, swap them
            if self.heap[index] > self.heap[parent_index]:
                self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
                # Move up to the parent's index
                index = parent_index
            else:
                # If the heap property is satisfied, break the loop
                break

    def extract_max(self):
        """
        Remove and return the task with the highest priority (max element) from the heap.
        Maintains the max-heap property after removal.

        Returns:
        - Task: The task with the highest priority, or None if the heap is empty.

        Time Complexity:
        - O(log n) due to the down-heap operation to maintain the heap property.
        """
        if self.is_empty():
            return None
        
        # Swap the root (max element) with the last element in the heap
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        # Remove the last element (the max element)
        max_task = self.heap.pop()
        # Restore the heap property by moving the new root down
        self._heapify_down(0)
        return max_task

    def _heapify_down(self, index):
        """
        Helper method to move the element at the given index down to its correct position in the heap.

        Args:
        - index (int): The index of the element to move down in the heap.
        
        Time Complexity:
        - O(log n) in the worst case, where n is the number of elements in the heap.
        """
        # Continue moving down the tree until the heap property is restored
        while index < len(self.heap):
            largest = index
            left_child = 2 * index + 1  # Left child index
            right_child = 2 * index + 2  # Right child index

            # Check if the left child exists and is greater than the current largest
            if left_child < len(self.heap) and self.heap[left_child] > self.heap[largest]:
                largest = left_child
            # Check if the right child exists and is greater than the current largest
            if right_child < len(self.heap) and self.heap[right_child] > self.heap[largest]:
                largest = right_child

            # If the largest element is not the current element, swap and continue
            if largest != index:
                self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
                # Move to the next index (where the largest was)
                index = largest
            else:
                # If the heap property is satisfied, break the loop
                break

    def increase_key(self, task, new_priority):
        """
        Increase the priority of a given task and adjust its position in the heap.

        Args:
        - task (Task): The task to increase the priority of.
        - new_priority (int): The new priority value for the task.

        Time Complexity:
        - O(log n) due to the up-heap operation to restore the heap property.
        """
        try:
            # Find the index of the task
            index = self.heap.index(task)
            # Ensure the new priority is actually higher
            if new_priority > self.heap[index].priority:
                # Update the priority
                self.heap[index].priority = new_priority
                # Restore the heap property by moving the task up
                self._heapify_up(index)
        except ValueError:
            # Task not found in the heap
            pass

    def decrease_key(self, task, new_priority):
        """
        Decrease the priority of a given task and adjust its position in the heap.

        Args:
        - task (Task): The task to decrease the priority of.
        - new_priority (int): The new priority value for the task.

        Time Complexity:
        - O(log n) due to the down-heap operation to restore the heap property.
        """
        try:
            # Find the index of the task
            index = self.heap.index(task)
            # Ensure the new priority is actually lower
            if new_priority < self.heap[index].priority:
                # Update the priority
                self.heap[index].priority = new_priority
                # Restore the heap property by moving the task down
                self._heapify_down(index)
        except ValueError:
            # Task not found in the heap
            pass

    def is_empty(self):
        """
        Check if the heap is empty.

        Returns:
        - bool: True if the heap is empty, False otherwise.

        Time Complexity:
        - O(1) as it involves checking the length of the list.
        """
        return len(self.heap) == 0

