class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        max_area = 0
        for i in range(len(height)):
            for j in range(len(height) - 1, i, -1):
                if height[j] >= height[i]:
                    max_area = max(max_area, height[i] * (j - i))
                    break
                max_area = max(max_area, height[j] * (j - i))

        return max_area

if __name__ == "__main__":
    print Solution().maxArea([1, 2, 3])
