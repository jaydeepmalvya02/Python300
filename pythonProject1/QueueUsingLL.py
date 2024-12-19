class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class Queue:
    def __init__(self):
        self.front=None
        self.rear=None
        self.item_count=0


    def isEmpty(self):
        return self.front==None



    def Enqueue(self,item):
        n=Node(item)
        if self.isEmpty():
            self.front=n

        else:
            self.rear.next=n
        self.rear=n
        self.item_count+=1


    def Dequeue(self):
        if self.isEmpty():
            raise IndexError("Queue Underflow")
        elif self.rear==self.front:
            self.front=None
            self.rear=None
        else:
            self.front=self.front.next
        self.item_count-=1

    def Get_front(self):
        return self.front.data

    def Get_rear(self):
        return self.rear.data


    def Size(self):
        return self.item_count



Q=Queue()
Q.Enqueue(10)
Q.Enqueue(30)
Q.Enqueue(40)
Q.Enqueue(50)
Q.Dequeue()
print(Q.Get_front())
print(Q.Get_rear())
print(Q.Size())






