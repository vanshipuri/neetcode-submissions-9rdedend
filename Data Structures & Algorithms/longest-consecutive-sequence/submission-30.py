class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        my_nums=set(nums)
        n=len(nums)
        longest=0
        for num in my_nums:
            if num - 1 not in my_nums:
                current = num
                count = 1
                while current + 1 in my_nums:
                    current += 1
                    count += 1
                longest=max(longest,count)
        return longest
        