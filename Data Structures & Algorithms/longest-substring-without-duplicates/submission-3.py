class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        record=set()
        res=[]
        max_val=0
        for i in s:
            if i not in record:
                res.append(i)
                record.add(i)
            else:
                while res[0]!=i:
                    k=res.pop(0)
                    record.remove(k)
                res.pop(0)
                res.append(i)
            max_val=max(max_val,len(res))
        return max_val



