class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 1:
            return False
        count = 1
        sqrt = int(math.sqrt(num))
        for i in range(2, sqrt + 1):
            if num%i == 0:
                count += i
                if i != num // i:
                    count += num // i
        return count == num
        