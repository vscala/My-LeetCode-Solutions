class AllOne:

    def __init__(self):
        self.count = defaultdict(int)
        self.minHeap, self.maxHeap = [], []
        

    def inc(self, key: str) -> None:
        self.count[key] += 1
        heappush(self.maxHeap, (-self.count[key], key))
        heappush(self.minHeap, (self.count[key], key))

    def dec(self, key: str) -> None:
        self.count[key] -= 1
        if self.count[key]:
            heappush(self.maxHeap, (-self.count[key], key))
            heappush(self.minHeap, (self.count[key], key))
        

    def getMaxKey(self) -> str:
        while self.maxHeap:
            curCount, key = heappop(self.maxHeap)
            if curCount == -self.count[key]:
                heappush(self.maxHeap, (curCount, key))
                return key
        return ""
        

    def getMinKey(self) -> str:
        while self.minHeap:
            curCount, key = heappop(self.minHeap)
            if curCount == self.count[key]:
                heappush(self.minHeap, (curCount, key))
                return key
        return ""
        


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()