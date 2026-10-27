class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ret =[] 
        n = len(candidates)
        candidates.sort()
        
        def dfs(i,curr, total):
            if total == target:
                ret.append(curr[::])
                return
            for j in range(i, n):
                if candidates[j]+ total > target:
                    break
                if j>i and candidates[j] == candidates[j-1]:
                    continue
                curr.append(candidates[j])
                dfs(j+1, curr, total+candidates[j])
                curr.pop()
        dfs(0,[],0)
        return ret