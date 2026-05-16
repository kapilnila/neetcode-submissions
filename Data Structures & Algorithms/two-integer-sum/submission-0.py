class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res={}

        for i in range(len(nums)):
            if target-nums[i] in res:
                k= target-nums[i]
                return [res[k],i]
            else:
                res[nums[i]]=i
        