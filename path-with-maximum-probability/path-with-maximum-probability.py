class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph = defaultdict(dict)
        for i in range(len(edges)):
            a, b, w = *edges[i], succProb[i]
            graph[a][b] = w
            graph[b][a] = w

        pq = [(-1, start)]
        visited = set()
        while pq:
            path_weight, cur = heappop(pq)
            if cur in visited: continue
            visited.add(cur)
            if cur == end: return -path_weight
            for adj in graph[cur]:
                if adj not in visited:
                    heappush(pq, (path_weight * graph[cur][adj], adj))
        return 0