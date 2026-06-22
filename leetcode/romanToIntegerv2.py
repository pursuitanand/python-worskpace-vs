class Solution:
    def romanToInt(self, s: str) -> int:
        # Provide fastest implementation here
        roman_numerals = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        num = 0
        prev_value = 0
        #print(reversed(s))
        for char in reversed(s):
            curr_value = roman_numerals[char]
            if curr_value < prev_value:
                num -= curr_value
            else:
                num += curr_value
            prev_value = curr_value
        return num

s = Solution()
print(s.romanToInt("CLLLIX"))      # 3
#print(s.romanToInt("LIXIV"))      # 63
#print(s.romanToInt("IV"))       # 4
#print(s.romanToInt("IX"))       # 9
#print(s.romanToInt("LVIII"))    # 58
#print(s.romanToInt("MCMXCIV"))  # 1994