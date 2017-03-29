class Solution(object):
    pair_map = {'(': ')', '{': '}', '[': ']'}

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        while len(s) > 0:
            shortened = False
            if s[0] not in self.pair_map:
                return False

            pair_index_list = [i for i, c in enumerate(s[1:]) if c == self.pair_map[s[0]]]
            # pair_index_list.reverse()
            for pair_index in pair_index_list:
                if self.isValid(s[1:(1 + pair_index)]):
                    s = s[(2 + pair_index):]
                    shortened = True
                    break

            if not shortened:
                return False

        return True


if __name__ == "__main__":
    print Solution().isValid('')
    print Solution().isValid('(')
    print Solution().isValid('}')
    print Solution().isValid('()')
