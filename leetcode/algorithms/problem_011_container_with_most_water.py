import sys
import itertools

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        grouped_height = itertools.groupby(sorted(
            [(i, h) for i, h in enumerate(height)], key=lambda item: item[1], reverse=True),
            lambda item: item[1])

        left_window, right_window, max_area = sys.maxint, -1, 0
        for group in grouped_height:
            positions = [item[0] for item in group[1]]
            left_group_window, right_group_window = min(positions), max(positions)

            if left_group_window < left_window:
                left_window = left_group_window

            if right_group_window > right_window:
                right_window = right_group_window

            max_area = max(max_area, (right_window - left_window) * group[0])

        return max_area

if __name__ == "__main__":
    print Solution().maxArea([1, 2, 3])
