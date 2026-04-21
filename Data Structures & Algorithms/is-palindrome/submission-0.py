class Solution:
    def isPalindrome(self, s: str) -> bool:
        currStr = ""
        for i in s:
            if i.isalnum():
                currStr+=i.lower()
        print(currStr)
        return currStr == currStr[::-1]