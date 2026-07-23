class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        pairs={')':'(','}':'{',']':'['}
        for chr in s:
            if chr in pairs:
                if not stack or stack[-1]!=pairs[chr]:
                    return False
                stack.pop()
            else:
                stack.append(chr)
        return len(stack)==0
        