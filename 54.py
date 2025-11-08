class Solution:
    def intersect(self, nums1, nums2):
        c1 = Counter(nums1)
        res = []
        for n in nums2:
            if c1[n] > 0:
                res.append(n)
                c1[n] -= 1
        return res
