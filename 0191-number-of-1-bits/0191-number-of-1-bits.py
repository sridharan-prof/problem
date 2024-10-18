class Solution:
    def hammingWeight(self, n: int) -> int:
        binary = bin(n)[2:].count("1")
        return binary

        