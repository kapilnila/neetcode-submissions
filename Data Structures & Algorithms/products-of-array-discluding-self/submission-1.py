class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nxt = [1] * n

        prod = 1
        for i in range(n - 1, -1, -1):
            nxt[i] = prod
            prod *= nums[i]

        res = []
        prefix = 1
        for i in range(n):
            res.append(prefix * nxt[i])
            prefix *= nums[i]
            
        return res
