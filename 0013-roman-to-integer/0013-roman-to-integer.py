class Solution:
    def romanToInt(self, s: str) -> int:
        num_dict = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}

        out = 0

        prev = "M"
        for c in s:
            if num_dict[c] > num_dict[prev]:
                out += num_dict[c] - 2 * num_dict[prev]
            else:
                out += num_dict[c]

            prev = c

        return out
