from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        have = 0
        need = len(freq_t := Counter(t))
        freq_s = {}
        i = 0
        minWindow = [-1, -1]
        for j in range(len(s)):
            freq_s[s[j]] = freq_s.get(s[j], 0) + 1
            if s[j] in freq_t and freq_s[s[j]] == freq_t[s[j]]:
                have += 1
            while have == need:
                if minWindow == [-1, -1] or j - i < minWindow[1] - minWindow[0]:
                    minWindow = [i, j]
                freq_s[s[i]] -= 1
                if s[i] in freq_t and freq_s[s[i]] < freq_t[s[i]]:
                    have -= 1
                i += 1
        return "" if minWindow == [-1, -1] else s[minWindow[0]:minWindow[1]+1]