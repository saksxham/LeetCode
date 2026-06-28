class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        if not s:
            return 0
        
        i = 0
        sign = 1
        # Check for sign
        if s[i] == '-':
            sign = -1
            i += 1
        elif s[i] == '+':
            i += 1
            
        res = 0
        # Convert digits
        while i < len(s) and s[i].isdigit():
            res = res * 10 + int(s[i])
            i += 1
            
        # Apply sign
        res *= sign
        
        # Clamp to 32-bit integer range
        int_max = 2**31 - 1
        int_min = -2**31
        
        if res > int_max:
            return int_max
        if res < int_min:
            return int_min
            
        return res