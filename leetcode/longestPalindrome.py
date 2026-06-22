class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0:
            return ""
        if len(s) == 1:
            return s
        left, right = 0, 0
        answer = s[0]
        for i in range(len(s)):
            left = i
            # find all occurrences of s[i] in s other than index i
            occurrences = self.findAllOccurrences(s, s[i], i)
            for j in occurrences:
                right = j + 1
                substring = s[left:right]
                is_same = substring == substring[::-1]
                if is_same and len(substring) > len(answer):
                    answer = s[left:right]
                    found = True

        return answer

    def findAllOccurrences(self, s: str, char: str, exclude_index: int) -> list:
        occurrences = []
        for index in range(len(s)):
            if s[index] == char and index != exclude_index:
                occurrences.append(index)
        return occurrences[::-1]
s = Solution()
print(s.longestPalindrome("babad")) 
#print(s.longestPalindrome("xydaladyx")) # Output: "bab" or "aba"