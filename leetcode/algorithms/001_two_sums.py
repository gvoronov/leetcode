# import itertools

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # for i, j in itertools.combinations(range(len(nums)), 2):
        #     if nums[i] + nums[j] == target:
        #         return [i, j]

        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]

        new_nums = sorted(zip(range(len(nums)), nums), key=lambda item: item[1])
        return self.recursive_search(new_nums[0], new_nums[1:], target)


    def recursive_search(self, parent, nums, target):
        tmp = target - parent[1]

        new_nums = [num for num in nums if num[1] <= tmp]
        solution = [num for num in new_nums if num[1] == tmp]

        if len(solution) == 1:
            return [parent[0], solution[0][0]]
        else:
            return self.recursive_search(new_nums[0], new_nums[1:], target)

        
