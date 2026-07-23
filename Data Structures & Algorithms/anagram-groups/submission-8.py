class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group=defaultdict(list)
        for words in strs:
            key=''.join(sorted(words))
            group[key].append(words)
        return list(group.values())
        