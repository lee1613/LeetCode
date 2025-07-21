class Solution:
    def makeFancyString(self, s: str) -> str:
        out = ""
        prev = ""
        rep = 0
        for c in s:
            if c != prev:
                out += c
                prev = c
                rep = 1
            else:
                rep += 1
                if rep == 3:
                    rep -= 1
                else:
                    out += c

        return out

