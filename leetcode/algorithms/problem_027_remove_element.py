class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        i = 0
        while i < len(nums):
            if nums[i] == val:
                nums.pop(i)
            else:
                i += 1

        return len(nums)

if __name__ == "__main__":
    print Solution().removeDuplicates([3, 2, 2, 3])
