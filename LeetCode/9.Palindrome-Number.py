class Solution:
    def isPalindrome(self, x: int) -> bool:
        x1 = str(x)
        x2 = ""
        for i in range(len(x1)-1,-1,-1):
            x2 = x2+x1[i]
        if x1 == x2:
            return True
        return False
        