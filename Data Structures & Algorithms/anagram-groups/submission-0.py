class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for s in strs:
            curr = []
            for i in s:
                curr.append(i)
            key = list(sorted(curr))
            anagrams[tuple(key)].append(s)
        return list(anagrams.values())
