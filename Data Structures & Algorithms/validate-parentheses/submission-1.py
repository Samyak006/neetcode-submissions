class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opps = {"(":")",")":"(","[":"]","]":"[","{":"}","}":"{"}
        Open = ["(","[","{"]
        for i in s:
            if not stack:
                stack.append(i)
            else:
                if stack[-1] in Open:
                    if opps[stack[-1]] == i:
                        stack.pop()
                    else:
                        stack.append(i)
                else:
                    return False
        return len(stack)==0