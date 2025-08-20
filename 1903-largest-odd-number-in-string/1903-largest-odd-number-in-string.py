class Solution:
    def largestOddNumber(self, num: str) -> str:
        
        for i in range(len(num) - 1, -1, -1):
            if int(num[i]) % 2 == 1:
                break

        if i == 0:
            if int(num[0]) % 2 == 0:
                return ""
        return num[:i + 1]

        