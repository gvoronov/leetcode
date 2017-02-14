class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        common_prefix = ''

        if len(strs) == 0:
            return common_prefix

        for i in range(min([len(x) for x in strs])):
            if len(set([x[i] for x in strs])) == 1:
                common_prefix += strs[0][i]
            else:
                break

        return common_prefix
