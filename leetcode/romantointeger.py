class Solution:
    def romanToInt(self, s: str) -> int:
        num : int = 0
        sUp = s.upper()
        length = len(sUp)
        #print(length)
        i=0
        while i < length:
            #print(i)
            if (i < length - 1 and sUp[i] == 'I') and (sUp[i+1] == 'V' or sUp[i+1] == 'X'):
                num = num + self.matchroman(str(sUp[i]+sUp[i+1]))
                i = i+1
            elif (i < length - 1 and sUp[i] == 'X') and (sUp[i+1] == 'L' or sUp[i+1] == 'C'):
                num = num + self.matchroman(str(sUp[i]+sUp[i+1]))
                i = i+1
            elif (i < length - 1 and sUp[i] == 'C') and (sUp[i+1] == 'D' or sUp[i+1] == 'M'):
                num = num + self.matchroman(str(sUp[i]+sUp[i+1]))
                i = i+1
            else:
                num = num + self.matchroman(sUp[i])
            i = i+1
        return num

    def matchroman(self, ch: str) -> int:
        #print(ch)
        match ch:
            case 'I':
                return 1
            case 'IV':
                return 4
            case 'V':
                return 5
            case 'IX':
                return 9
            case 'X':
                return 10
            case 'XL':
                return 40
            case 'L':
                return 50
            case 'XC':
                return 90
            case 'C':
                return 100
            case 'CD':
                return 400
            case 'D':
                return 500
            case 'CM':
                return 900
            case 'M':
                return 1000

        return 0

s = Solution()
print(s.romanToInt("III"))      # 3    
print(s.romanToInt("IV"))       # 4
print(s.romanToInt("IX"))       # 9
print(s.romanToInt("LVIII"))    # 58
print(s.romanToInt("MCMXCIV"))  # 1994