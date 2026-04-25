class Solution:
    def findMin(self, nums: List[int]) -> int:
        ret = nums[0]
        l,r = 0,len(nums)-1
        while l<=r:
            m = (l+r)//2
            if nums[m]<= nums[r]:
                ret = min(ret,nums[m])
                r = m - 1
            else:
                l = m + 1
        return ret