class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest=0
        n=len(nums)
        num_set=set(nums)
        for num in num_set:
            if num-1 not in num_set:
                current = num
                count = 1
                while current+1 in num_set:
                    count+=1
                    current+=1
                longest=max(count,longest)
        return longest
        