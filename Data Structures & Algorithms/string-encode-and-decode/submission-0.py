class Solution:
    def encode(self, strs: List[str]) -> str:
        delimiter = "/e"
        ret = ""
        for s in strs:
            ret+=s
            ret+=delimiter
        return ret

    def decode(self, s: str) -> List[str]:
        return s.split("/e")[:-1]