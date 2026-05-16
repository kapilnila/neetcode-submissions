class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grps={}
        for i in strs:
            key="".join(sorted(i))

            if key not in grps:
                grps[key]=[]
            grps[key].append(i)
        return list(grps.values())
        
        