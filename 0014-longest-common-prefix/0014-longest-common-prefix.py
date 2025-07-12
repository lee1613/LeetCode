class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest = min(list(map(len, strs)))
        if len(strs) == 1:
            return strs[0]
        out = ""
        i = 0
        while i < shortest:
            c = strs[0][i]
            for word in strs:
                if word[i] != c:
                    return out
            
            out += c
            i += 1 

        return out
