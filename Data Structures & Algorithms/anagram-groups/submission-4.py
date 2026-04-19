from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result=defaultdict(list)
        for word in strs:
            count=[0]*26
            for chr in word:
                count[ord(chr)-ord('a')]+=1
            key=tuple(count)
            result[key].append(word)
        return list(result.values())
        