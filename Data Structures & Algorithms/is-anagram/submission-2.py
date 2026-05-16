from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        res1={}
        res2={}
        res1=Counter(s)
        res2=Counter(t)
        
        return res1==res2
        