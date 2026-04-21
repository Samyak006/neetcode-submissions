class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        count1 = {}
        for i in s1:
            count1[i] = 1+count1.get(i,0)
        
        def check(curr):
            for i,j in count1.items():
                if i not in curr or curr[i] != j:
                    return False
            return True

        # cannot contain s1 as s2 is smaller than s1
        if len(s2)<len(s1):
            return False
        
        l = 0
        curr = {}
        for r in range(len(s2)):
            curr[s2[r]] = 1+curr.get(s2[r],0)
            if r-l+1 == len(s1):
                if check(curr):
                    return True
                curr[s2[l]]-=1
                l+=1
        return False