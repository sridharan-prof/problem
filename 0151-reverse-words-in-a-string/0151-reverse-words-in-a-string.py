class Solution(object):
    def reverseWords(self, s):
        ls = s.split()
        return " ".join(ls[::-1])

        