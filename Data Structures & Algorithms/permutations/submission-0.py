class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ret = []
        def generate(nums, l):
            if not nums:
                ret.append(l)
                return
            for i in nums:
                curr = nums[::-1]
                curr.pop(curr.index(i))
                generate(curr, l+[i])
        generate(nums, [])
        return ret