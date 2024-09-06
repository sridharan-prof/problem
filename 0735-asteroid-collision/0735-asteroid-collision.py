class Solution(object):
    def asteroidCollision(self, a):
        res = []
        for i in a:
            while res and i < 0 and res[-1] > 0:
                if res[-1] < -i:
                    res.pop()
                    continue
                elif res[-1] == -i:
                    res.pop()
                break
            else:
                res.append(i)
        return res