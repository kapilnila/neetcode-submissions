class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res={}
        ans=[]
        for i in nums:
            if i not in res:
                res[i]= 1
            else:
                res[i] += 1
        for x in res:
            p=res[x]
            ans.append([p,x])
        ans.sort(reverse=True)

        final=[]
        for i in range(k):
            final.append(ans[i][1])
        return final
