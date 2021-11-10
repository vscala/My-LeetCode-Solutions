class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        known = defaultdict(dict)
        for i in range(len(equations)):
            a, b, v = *equations[i], values[i]
            known[a][b] = v
            known[b][a] = 1/v
        
        # search from a -> b in known
        out = []
        for a, b in queries:
            if b in known[a]: out += [known[a][b]]
            else: 
                for c in known[a]:
                    # navigate from a -> c -> ... -> b
                    visited = set()
                    q = [(c, known[a][c])]
                    while q:
                        cur, val = q.pop(0)
                        if b in known[cur]: 
                            out += [known[cur][b]*val]
                            break
                        if cur in visited: continue
                        visited.add(cur)
                        for d in known[cur]:
                            q += [(d, val*known[cur][d])]
                    else: continue
                    break
                else: out += [-1]
        return out