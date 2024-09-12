class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        mapping_s_to_t = {}
        mapping_t_to_s = {}
        
        for i in range(len(s)):
            char_s = s[i]
            char_t = t[i]
            
            # Check if there's an inconsistent mapping from s to t
            if char_s in mapping_s_to_t and mapping_s_to_t[char_s] != char_t:
                return False
            
            # Check if there's an inconsistent mapping from t to s
            if char_t in mapping_t_to_s and mapping_t_to_s[char_t] != char_s:
                return False
            
            # Add or update the mappings
            mapping_s_to_t[char_s] = char_t
            mapping_t_to_s[char_t] = char_s
        
        return True

        