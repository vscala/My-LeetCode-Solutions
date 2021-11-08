class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        mods = defaultdict(int)
        for val in arr:
            if mods[(k - val%k)%k]: mods[(k - val%k)%k] -= 1
            else: mods[val%k] += 1
        return all(mods[v] == 0 for v in mods)