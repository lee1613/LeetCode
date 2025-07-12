class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        return all([x[i] == x[-(i + 1)] for i in range(len(x) // 2)])