class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        tickets = [(t, False) for t in tickets]
        tickets[k] = (tickets[k][0], True)
        q = deque(tickets)
        time = 0
        while q:
            time += 1
            a, p = q.popleft()
            a -= 1
            if a == 0 and p: return time
            if a: q.append((a, p))
        