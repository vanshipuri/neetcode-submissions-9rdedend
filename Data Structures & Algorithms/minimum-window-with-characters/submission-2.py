class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return " "
        
        need={}
        for c in t:
            need[c]=need.get(c,0)+1
        
        window={}
        have=0
        total_need=len(need)
        l=0
        res=""
        res_len=float("inf")

        for r in range(len(s)):
            c=s[r]
            window[c]=window.get(c,0)+1
            if c in need and window[c]==need[c]:
                have+=1
            while total_need==have:
                if (r-l+1)<res_len:
                    res_len=r-l+1
                    res=s[l:r+1]

                window[s[l]]-=1
                if s[l] in need and window[s[l]]<need[s[l]]:
                    have-=1
                l+=1
        return res

        