class Solution:
    def largestGoodInteger(self, num: str) -> str:
        count = 1
        prev = num[0]
        res = ""
        for i in range(1, len(num)):
            c = num[i]
            if c == prev:
                count += 1
                if count == 3:
                    if prev > res:
                        res = prev
            else:
                prev = c
                count = 1

        return res * 3
        