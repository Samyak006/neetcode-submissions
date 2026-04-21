class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ret = []
        def generate(o,c,curr):
            if o+c == 2*n:
                ret.append(curr)
                return 
            # take/skip
            if o<n:
                generate(o+1,c,curr+"(")
            if c<o:
                generate(o,c+1,curr+")")
        generate(0,0,"")
        return ret