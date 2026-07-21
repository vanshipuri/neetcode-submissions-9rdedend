class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = set()
        n = len(nums)
        for i in range(n - 2):
            left = i + 1
            right = n - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    result.add((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1
        return [list(t) for t in result]