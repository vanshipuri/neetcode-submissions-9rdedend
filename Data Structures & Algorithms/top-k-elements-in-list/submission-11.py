class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)
        nums.sort()
        count={}
        result=set()
        for num in nums:
            count[num]=count.get(num,0)+1
            result=sorted(count,key=count.get,reverse=True)
        return result[:k]
        