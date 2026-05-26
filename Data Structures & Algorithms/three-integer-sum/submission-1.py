class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        rec=set()

        for i in range(len(nums)):
            seen=set()

            for j in range(i+1,len(nums)):

                target = - (nums[i]+nums[j])
                if target in seen:
                    triplet = tuple(sorted([nums[i],nums[j],target]))
                    rec.add(triplet)
                seen.add(nums[j])
        return [list(x) for x in rec]