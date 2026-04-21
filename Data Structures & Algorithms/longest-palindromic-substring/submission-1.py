class Solution:
    def longestPalindrome(self, s: str) -> str:
        ret = 1
        retS = [0,0]
        for i in range(len(s)):
            l,r = i,i
            while l>=0 and r<len(s):
                if s[l] == s[r]:
                    if ret<(r-l+1):
                        ret = max(ret, r-l+1)
                        retS = [l,r]
                else:
                    break
                l-=1
                r+=1
            l,r = i,i+1
            while l>=0 and r<len(s):
                if s[l] == s[r]:
                    if ret<(r-l+1):
                        ret = max(ret, r-l+1)
                        retS = [l,r]
                else:
                    break
                l-=1
                r+=1
        return s[retS[0]:retS[1]+1]