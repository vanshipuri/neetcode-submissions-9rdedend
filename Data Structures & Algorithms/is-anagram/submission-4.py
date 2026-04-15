class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n=len(str(s))
        m=len(str(t))
        if n!=m:
            return False
        count = [0]*26
        for chr in s:
            index=ord(chr)-ord('a')
            count[index]+=1
        for chr in t:
            index=ord(chr)-ord('a')
            count[index]-=1
            if count[index]<0:
                return False
        return True