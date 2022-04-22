from logging import exception


class Queue:
    def __init__(self):
        self.q = []
    
    def head(self):
        if not self.isEmpty():
            return self.q[-1]
        else:
            print(f"message in QueueModule: head failed!")

    def enqueue(self, obj):
        self.q.insert(0, obj)

    def dequeue(self):
        if not self.isEmpty():
            obj  = self.q.pop(-1)
            return obj
        else:
            print(f"message in QueueModule: Pop failed!")
            raise IndexError("Queue is Empty")       
                 
    def isEmpty(self):
        return len(self.q) == 0

class QueueEx(Queue):
    def __init__(self, maxSize: int):
        super().__init__()

        if maxSize <= 0:
            raise exception("Size insert a Positive value.")

        self.maxSize = maxSize
        self.size = 0

    def enqueue(self, obj):
        if self.size < self.maxSize:
            super().enqueue(obj)
            self.size += 1
        else:
            print(f"Queue is Full, {obj} was not inserted.")
    
    def dequeue(self):
        return super().dequeue()

    def isEmpty(self):
        return super().isEmpty()