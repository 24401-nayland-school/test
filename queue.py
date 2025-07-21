# queue.py

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        """Adds an item to the end of the queue"""
        self.queue.append(item)

    def dequeue(self):
        """Removes and returns an item from the front of the queue"""
        if not self.is_empty():
            return self.queue.pop(0)
        return None  # Queue is empty

    def peek(self):
        """Returns the item at the front of the queue without removing it"""
        if not self.is_empty():
            return self.queue[0]
        return None

    def is_empty(self):
        """Returns True if the queue is empty, otherwise False"""
        return len(self.queue) == 0

    def size(self):
        """Returns the number of items in the queue"""
        return len(self.queue)