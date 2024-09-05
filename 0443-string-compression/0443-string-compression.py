class Solution(object):
    def compress(self, chars):
        i = 0
        res = 0
        while i < len(chars):
            gp_len = 1
            while(i + gp_len < len(chars) and chars[i + gp_len] == chars[i]):
                gp_len += 1
            chars[res] = chars[i]
            res += 1
            if gp_len > 1:
                st = str(gp_len)
                chars[res:res + len(st)] = list(st)
                res += len(st)
            i += gp_len
        return res
