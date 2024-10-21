class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_word = Counter(ransomNote)
        magazine_word = Counter(magazine)

        for char, count in ransom_word.items():
            if magazine_word[char] < count:
                return False
        return True

        