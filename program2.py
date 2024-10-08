class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        romanMap = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        total = 0
        for i in range(len(s)):
            currentVal = romanMap[s[i]]
            if i + 1 < len(s) and currentVal < romanMap[s[i + 1]]:
                total -= currentVal
            else:
                total += currentVal
        return total

