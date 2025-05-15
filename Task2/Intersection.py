class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        map = dict(); ans = []

        for i in nums1:
            map[i] = map.get(i, 0) + 1

        for i in nums2:
            if map.get(i):
                ans.append(i)
                map[i] -= 1
        
        return ans