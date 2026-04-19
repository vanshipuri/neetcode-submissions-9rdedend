class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        my_set=set(nums)
        n=len(my_set)
        longest_count=0
        for num in my_set:
            if num-1 not in my_set:
                current=num
                count=1
                while current+1 in my_set:
                    count+=1
                    current+=1
                longest_count=max(longest_count,count)
        return longest_count
        

    


            

        