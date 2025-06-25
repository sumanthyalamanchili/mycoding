class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dana = {}
        for i in range(0,len(s)):
            if s[i] in dana:
                dana[s[i]]=dana[s[i]]+1
            else:
                dana[s[i]]=1
        for i in range(0,len(t)):
            if t[i] in dana:
                if dana[t[i]]==0:
                    return False      
                else:
                    dana[t[i]]=dana[t[i]]-1
            else:
                return False
        for i in dana.keys():
            if dana[i]==0:
                continue
            else:
                return False
        return True                           