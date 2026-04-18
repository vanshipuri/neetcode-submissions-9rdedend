class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        hash_maps={}
        for i in range(0,n):
            remaining=target-nums[i]
            if remaining in hash_maps:
                return [hash_maps[remaining],i]
            hash_maps[nums[i]]=i
