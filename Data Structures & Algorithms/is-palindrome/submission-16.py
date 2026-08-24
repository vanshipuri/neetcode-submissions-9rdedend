class Solution:
    def isPalindrome(self, s: str) -> bool:
        res=[]
        for chr in s:
            if chr.isalnum():
                res.append(chr.lower())
        return res==res[::-1]

        