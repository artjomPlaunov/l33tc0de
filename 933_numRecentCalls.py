from collections import deque

class RecentCounter:

    def __init__(self):
        self.dq = deque([])

    def ping(self, t: int) -> int:
        lo = t-3000
        self.dq.append(t)
        while self.dq[0] < lo :
            self.dq.popleft()
        return len(self.dq)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
