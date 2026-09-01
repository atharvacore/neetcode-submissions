class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        maxs = 0
        l = 0
        r=0
        while r<len(s):
            while s[r] in seen:
                seen.remove(s[l])
                l+=1
            seen.add(s[r])
            current = r-l+1
            maxs= max(current,maxs)
            r+=1
        return maxs           

            
        