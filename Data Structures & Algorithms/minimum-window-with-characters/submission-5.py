class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        
        need={}
        for c in t:
            need[c]=need.get(c,0)+1
        
        window={}
        have=0
        total_need=len(need)
        res=""
        left=0
        res_len=float("inf")

        for right in range(len(s)):
            c=s[right]
            window[c]=window.get(c,0)+1
            if c in need and window[c]==need[c]:
                have+=1
            while have==total_need:
                if res_len>(right-left+1):
                    res_len=right-left+1
                    res=s[left:right+1]
                window[s[left]]-=1
                if s[left] in need and window[s[left]]< need[s[left]]:
                    have-=1
                left+=1
        return res
        