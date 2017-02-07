class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        l1, l2 = len(nums1), len(nums2)

        if l1 == 0:
            return self.median(l2, nums2)

        if l2 == 0:
            return self.median(l1, nums1)

        m1, m2 = self.median(l1, nums1), self.median(l2, nums2)

        while m1 != m2:
            if m2 < m1:
                l1, l2 = l2, l1
                m1, m2 = m2, m1
                nums1, nums2 = nums2, nums1

            l = int(math.floor(min(l1, l2) / 2)) - 1

            if l <= 1:
                return self.median(l1 + l2, sorted(nums1 + nums2))

            nums1 = nums1[l:]
            nums2 = nums2[:-l]

            l1, l2 = len(nums1), len(nums2)
            m1, m2 = self.median(l1, nums1), self.median(l2, nums2)

        return m1

    def median(self, l, nums):
        if l % 2 == 0:
            return 1.0 * (nums[(l / 2) - 1] + nums[(l / 2)]) / 2
        else:
            return nums[(l - 1) / 2]
