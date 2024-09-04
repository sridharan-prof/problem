class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        ar = []
        x = 0
        y = 0
        a, b = len(word1), len(word2) 
        while x < a or y < b:
            if x < a:
                ar.append(word1[x])
                x += 1
            if y < b:
                ar.append(word2[y])
                y += 1
            
        return "".join(ar)