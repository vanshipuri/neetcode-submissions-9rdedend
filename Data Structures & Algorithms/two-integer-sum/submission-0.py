class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        hashmaps={}
        for i in range(0,n):
            remaining=target-nums[i]
            if remaining in hashmaps:
                return [hashmaps[remaining],i]
            hashmaps[nums[i]]=i



        