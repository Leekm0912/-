import collections


class MyStack:
    def __init__(self):
        self.q = collections.deque()

    def push(self, x):
        self.q.append(x)
        # 요소 삽입 후 앞에 있는것들을 모두 뒤로 보냄.
        for _ in range(len(self.q) - 1):
            self.q.append((self.q.popleft()))

    def pop(self):
        # 맨 앞에 있는것이 가장 마지막에 들어온 요소.
        self.q.popleft()

    def top(self):
        return self.q[0]

    def empty(self):
        return len(self.q) == 0
