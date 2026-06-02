class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        n = len(nums)
        for i in range(n):
            remaining = target - nums[i]

            if remaining in hashmap:
                return [hashmap[remaining], i]
            hashmap[nums[i]] = i