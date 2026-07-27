class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums.sort()
        count={}
        for num in nums:
            count[num]=count.get(num,0)+1
            res=sorted(count,key=count.get,reverse=True)
        return res[:k]