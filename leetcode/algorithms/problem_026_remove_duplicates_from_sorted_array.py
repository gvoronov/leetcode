class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        last_num, i = None, 0
        while i < len(nums):
            if nums[i] == last_num:
                nums.pop(i)
            else:
                last_num = nums[i]
                i += 1

        return len(nums)

if __name__ == "__main__":
    print Solution().removeDuplicates([1, 1, 2])
    print Solution().removeDuplicates([0, 1, 2, 3])
    print Solution().removeDuplicates([])
