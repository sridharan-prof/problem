class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "0"
        result = ''
        is_neg = num < 0
        num = abs(num)

        while num > 0:
            result = str(num % 7) + result
            num //= 7
        if is_neg:
            result = "-" + result
        return result
        