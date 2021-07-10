class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = 0
        self.rear = 0

    # 큐에 추가
    def enQueue(self, num):
        if self.queue[self.rear] is None:
            print("추가", num)
            self.queue[self.rear] = num
            self.rear = (self.rear + 1) % self.size
            return True
        else:
            print("큐가 가득 찼습니다.")
            return False

    # 큐에서 제거
    def deQueue(self):
        if self.queue[self.front] is None:
            print("큐가 비었습니다.")
            return False
        else:
            print("제거", self.queue[self.front])
            self.queue[self.front] = None
            self.front = (self.front + 1) % self.size
            return True

    # 가장 마지막
    def Rear(self):
        return self.queue[self.rear - 1]

    # 원형 큐가 꽉차있나?
    def isFull(self):
        # front와 rear가 같고, front값이 None이 아니면 꽉차있음
        return self.front == self.rear and self.queue[self.front] is not None

    # 원형 큐가 비어있나?
    def isEmpty(self):
        # front와 rear가 같고, front값이 None이면 비어있음
        return self.front == self.rear and self.queue[self.front] is None

    # 맨 앞
    def Front(self):
        return self.queue[self.front]

    def printQueue(self):
        f = self.front
        print("========printQueue========")
        # do while문 구현
        while True:
            print(self.queue[f])
            f = (f + 1) % self.size
            if f == self.rear or self.isEmpty():
                break
        print("==========================")


if __name__ == "__main__":
    cq = CircularQueue(5)
    cq.enQueue(10)
    cq.enQueue(20)
    cq.enQueue(30)
    cq.enQueue(40)
    cq.printQueue()
    print(cq.Rear())
    print(cq.isFull())
    cq.deQueue()
    cq.deQueue()
    cq.enQueue(50)
    cq.enQueue(60)
    cq.printQueue()
    print(cq.Rear())
    print(cq.Front())
    cq.enQueue(70)
    cq.enQueue(80)
    cq.printQueue()
    cq.deQueue()
    cq.deQueue()
    cq.deQueue()
    cq.deQueue()
    cq.deQueue()
    cq.deQueue()
    cq.printQueue()
