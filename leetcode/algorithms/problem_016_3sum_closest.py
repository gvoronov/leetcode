import sys
import math

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        closest = sys.maxint
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    s = nums[i] + nums[j] + nums[k]
                    if math.fabs(s - target) < math.fabs(closest - target):
                        closest = s

        return closest
