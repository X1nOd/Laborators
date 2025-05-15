class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        consecutive = 1
        
        maxSubstr = defaultdict(int)
        maxSubstr[p[0]] = 1
        
        ans = 0
        for x in range(1, len(p)):
            if ord(p[x]) - ord(p[x - 1]) == 1 or p[x] == 'a' and p[x - 1] == 'z':
                consecutive += 1
            else:
                consecutive = 1
            maxSubstr[p[x]] = max(maxSubstr[p[x]], consecutive)
        
        return sum(maxSubstr.values())