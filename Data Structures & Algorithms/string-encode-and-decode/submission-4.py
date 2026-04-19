class Solution:

    def encode(self, strs: List[str]) -> str:
        res=''
        for word in strs:
            res+=str(len(word))+'#'+word
        return res

    def decode(self, s: str) -> List[str]:
        i=0
        result=[]
        while len(s)>i:
            j=i
            while s[j]!='#':
                j+=1
            length=int(s[i:j])
            j+=1
            word=s[j:j+length]
            result.append(word)
            i=j+length
        return result