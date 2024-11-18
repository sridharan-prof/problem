class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        sign = -1 if x < 0 else 1
        x = abs(x)
        number = 0

        while x != 0:
            rem = x % 10
            x = x // 10
            if number > (INT_MAX - rem) // 10:
                return 0
            number = number * 10 + rem
        return sign * number