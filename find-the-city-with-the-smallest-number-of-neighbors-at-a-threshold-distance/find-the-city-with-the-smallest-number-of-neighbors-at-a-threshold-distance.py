class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        outv, out = float("inf"), 0
        graph = defaultdict(dict)
        for a, b, w in edges:
            graph[a][b] = w
            graph[b][a] = w
        
        for start in range(n):
            pq = [(0, start)] 	# priority queue: (path_weight, current_node)
            visited = set() 	# set of visited nodes
            
            while pq:
                path_weight, cur = heappop(pq)
                if path_weight > distanceThreshold: break
                if cur in visited: continue
                visited.add(cur)
                if len(visited) > outv: break
                for adj in graph[cur]:
                    if adj not in visited:
                        heappush(pq, (path_weight + graph[cur][adj], adj))
            if len(visited) <= outv: 
                outv = len(visited)
                out = start
        return out