class Solution(object):
    pair_map = {'(': ')', '{': '}', '[': ']'}

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        len_s = len(s)
        while len_s > 0:
            s = ''.join(s.split('()'))
            s = ''.join(s.split('[]'))
            s = ''.join(s.split('{}'))

            if len(s) < len_s:
                len_s = len(s)
            else:
                return False

        return True

    def isValid_02(self, s):
        """
        :type s: str
        :rtype: bool
        """

        len_s = len(s)
        while len_s > 0:
            for i in xrange(len(s) - 1):
                if s[i] in self.pair_map and s[i+1] == self.pair_map[s[i]]:
                    s = s[:i] + s[(i + 2):]
                    break

            if len(s) < len_s:
                len_s = len(s)
            else:
                return False

        return True

    def isValid_01(self, s):
        """
        :type s: str
        :rtype: bool
        """

        if len(s) % 2 == 1:
            return False

        if (
                not self.check_pair_count(s, '(') or
                not self.check_pair_count(s, '{') or
                not self.check_pair_count(s, '[')):
            print 'I got called'
            return False

        while len(s) > 0:
            shortened = False
            if s[0] not in self.pair_map:
                return False

            pair_index_list = [i for i, c in enumerate(s[1:]) if c == self.pair_map[s[0]]]

            for pair_index in pair_index_list:
                if self.isValid(s[1:(1 + pair_index)]):
                    s = s[(2 + pair_index):]
                    shortened = True
                    break

            if not shortened:
                return False

        return True

    def check_pair_count(self, s, delim):
        l_delim_list = [i for i, c in enumerate(s) if c == delim]
        r_delim_list = [i for i, c in enumerate(s) if c == self.pair_map[delim]]

        if len(l_delim_list) == len(r_delim_list):
            return True
        else:
            return False

if __name__ == "__main__":
    print Solution().isValid('')
    print Solution().isValid('(')
    print Solution().isValid('}')
    print Solution().isValid('()')
    print Solution().isValid('([)]')
