class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        new = defaultdict(list)
        for s in strs:
            sortedS = ''.join(sorted(s))
            new[sortedS].append(s)
        return list(new.values())