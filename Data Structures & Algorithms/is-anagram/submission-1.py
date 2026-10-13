class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        t_hashmap = {}
        s_hashmap = {}
        
        for i in range(len(s)):
            s_hashmap[s[i]] = 1 + s_hashmap.get(s[i], 0)
            t_hashmap[t[i]] = 1 + t_hashmap.get(t[i], 0)

        return t_hashmap == s_hashmap 