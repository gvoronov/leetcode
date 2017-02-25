class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        nums_dict = dict()
        for num in nums:
            if num in nums_dict:
                nums_dict[num] += 1
            else:
                nums_dict[num] = 1
        nums = sorted(nums)

        three_sums_set = set()
        i, j = 0, len(nums)
        while i != j:
            a, b = nums[i], nums[j]

        return [list(t) for t in three_sums_set]

    def threeSum_slow_for_testing(self, nums):
        nums = sorted(nums)

        three_sums_set = set()
        for i in range(len(nums)):
            a = nums[i]
            if a > 0:
                break
            for j in range(i + 1, len(nums)):
                b = nums[j]
                if 2 * b > -a:
                    break
                for k in range(j + 1, len(nums)):
                    c = nums[k]
                    if a + b + c == 0:
                         three_sums_set.add((a, b, c))
                         break
                    elif c > -(a + b):
                        break

        return [list(t) for t in three_sums_set]

if __name__ == "__main__":
    print Solution().threeSum([-1, 0, 1, 2, -1, -4])
