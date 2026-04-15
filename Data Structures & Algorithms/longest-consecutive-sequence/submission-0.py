class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums=sorted(set(nums))
        n=len(set(nums))
        longest=1
        count=1
        for i in range(1,n):
            if nums[i]==nums[i-1]+1:
                count+=1
            else:
                count=1
            longest=max(longest,count)
        return longest
            


            
        