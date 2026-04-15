class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if sorted(str(s))==sorted(str(t)):
            return True
        return False


        

        