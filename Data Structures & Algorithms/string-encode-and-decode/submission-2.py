class Solution:


    def encode(self, strs: List[str]) -> str:
        en_strs = ""

        for s in strs:
            en_strs += f"{len(s)}#{s}"
        return en_strs

    def decode(self, s: str) -> List[str]:
        de_strs = []
        i = 0
        while i < len(s):
            delimiter = s.find('#', i)
            length = int(s[i:delimiter])
            de_strs.append(s[delimiter + 1 : delimiter + 1 + length])
            i = delimiter + 1 + length
        return de_strs
