class Solution(object):
    def reverseVowels(self, s):
        vowels = "aeiouAEIOU" 
        ls = list(s)
        i, j = 0, len(s) - 1
        while i < j:
            if ls[i] not in vowels:
                i += 1
            elif ls[j] not in vowels:
                j -= 1
            else:
                ls[i], ls[j] = ls[j], ls[i]
                i += 1
                j -= 1
        
        return "".join(ls)
        