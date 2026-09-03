class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l=0
        r = len(s1)-1
        while r in range(len(s2)):
            window = s2[l:r+1]
            if sorted(window) == sorted(s1):
                return True
            l+=1
            r+=1
        return False
            
