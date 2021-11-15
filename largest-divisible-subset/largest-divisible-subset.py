class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort() #O(nlogn)
        
        # create a graph O(n^2)
        # graph a -> B where (b in B) if (b % a == 0)
        graph = defaultdict(list)
        for a, b in combinations(nums, 2):
            if b % a == 0: graph[a].append(b)
        
        # find longest path O(|E|) where E is the set of graph edges
        out = []
        for i, start in enumerate(nums[::-1]):
            best = []
            for adj in graph[start]:
                if len(graph[adj]) > len(best):
                    best = graph[adj]
            graph[start] = [start] + best
            if len(graph[start]) > len(out): out = graph[start]
        return out