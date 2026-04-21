class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        curr= set()
        maxLen = l = 0
        for r in range(len(s)):
            if s[r] in curr:
                while l < r and s[r] in curr:
                    curr.remove(s[l])
                    l+=1
            curr.add(s[r])
            maxLen = max(maxLen, r-l+1)
        return maxLen
