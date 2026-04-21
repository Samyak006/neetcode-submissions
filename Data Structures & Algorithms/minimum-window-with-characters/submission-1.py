from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        have = 0
        need = len(set(t))
        freq_s = dict()
        freq_t = Counter(t)
        i = 0
        minWindow = [-1, -1]
        for j in range(len(s)):
            freq_s[s[j]] = freq_s.get(s[j],0)+1
            if s[j] in freq_t and freq_s[s[j]] == freq_t[s[j]]:
                have += 1 
            while need == have:
                if minWindow == [-1, -1] or j - i < minWindow[1] - minWindow[0]:
                    minWindow = [i, j]
                freq_s[s[i]]-=1
                if s[i] in freq_t and freq_s[s[i]]<freq_t[s[i]]:
                    have -=1
                if freq_s[s[i]] == 0:
                    del freq_s[s[i]]
                i+=1
        return "" if sum(minWindow) == -2 else s[minWindow[0]:minWindow[1]+1]
            
