class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        string = s.split()
        lower_case = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        if lower_case == lower_case[::-1]:
            return True
        else:
            return False
        