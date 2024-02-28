class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = dict()
        
        s_list = s.split()
        if len(s_list) != len(pattern):
            return False
        for n,p in enumerate(pattern):
           if p not in words.values():
            words[s_list[n]] = p
        
        for n,w in enumerate(s_list):
            if words.get(w) != pattern[n]:
                return False
        return True
            
