class Queue:
    def __init__(self):
        self.items=[]
        # self.front=None
        # self.rear=None
    def IsEmpty(self):
        return self.items[0]==0

    def Enqueue(self,data):
        self.items.append(data)

    def Dequeue(self):
        self.items.pop(0)

    def Get_front(self):
        return self.items[0]

    def Get_rear(self):
        return self.items[-1]

q=Queue()
q.Enqueue(10)
q.Enqueue(20)
q.Enqueue(30)
q.Enqueue(40)
print(q.Get_front())
print(q.Get_rear())
q.Dequeue()
print(q.Get_front())
