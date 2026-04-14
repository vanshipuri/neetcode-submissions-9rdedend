class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(str(s))!=len(str(t)):
            return False
        count={}
        for chr in s:
            count[chr]=count.get(chr,0)+1
        for chr in t:
            if chr not in count:
                return False
            count[chr]-=1
            if count[chr]<0:
                return False
        return True
        

        