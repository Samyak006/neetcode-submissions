class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret = []
        def dfs(i, curr):
            if i >=len(nums):
                ret.append(curr)
                return
            #take
            dfs(i+1,curr+[nums[i]])
            #skip
            dfs(i+1,curr)
        dfs(0,[])
        return ret
