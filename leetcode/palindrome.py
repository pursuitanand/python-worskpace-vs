class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x < 0:
            return False
        
        strX = str(x)
        lenX = len(strX)
        mid = lenX // 2
        for i in range(mid):
            if strX[i] != strX[lenX - 1 - i]:
                return False
        original = x
        reversed_num = 0
        while x > 0:
            digit = x % 10
            reversed_num = reversed_num * 10 + digit
            x //= 10
        return original == reversed_num
s = Solution()
print(s.isPalindrome(121))  # True
print(s.isPalindrome(-121))  # False
print(s.isPalindrome(10))    # False    