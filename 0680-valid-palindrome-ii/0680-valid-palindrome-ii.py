class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def is_palindrome_range(s, left, right):
            
            return all(s[i] == s[right - i + left] for i in range(left, right))

        left, right = 0, len(s) - 1
        
        while left < right:
            if s[left] != s[right]:
                return is_palindrome_range(s, left + 1, right) or is_palindrome_range(s, left, right - 1)
            left += 1
            right -= 1
        
        return True
        