class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        best = 0
        htable = dict()
        for i, x in enumerate(s):
            if x in htable:
                l1 = len(htable)
                old_i = htable.pop(x)
                htable = dict(
                    [(k, v) for k, v in htable.iteritems() if v > old_i])
                l2 = len(htable) + 1

                tmp_best = max(l1, l2)
                if tmp_best > best:
                    best = tmp_best

            htable[x] = i

        len_htable = len(htable)
        if len_htable > best:
            return len_htable
        else:
            return best
            
