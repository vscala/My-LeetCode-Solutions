class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        graph = defaultdict(dict)
        for a, b, w in times:
            graph[a][b] = w
        
        out = 0             # max time
        start = k			# Starting node
        pq = [(0, start)] 	# priority queue: (path_weight, current_node)
        visited = set() 	# set of visited nodes

        while pq:
            path_weight, cur = heappop(pq)
            if cur in visited: continue
            visited.add(cur)
            out = max(out, path_weight)
            for adj in graph[cur]:
                if adj not in visited:
                    heappush(pq, (path_weight + graph[cur][adj], adj))
        if len(visited) != n: return -1
        return out