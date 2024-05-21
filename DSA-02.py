class Solution(object):
    def lengthOfLongestSubstring(self, s):
        s = list(s)
        lists_count = []
        while s:
            seen = []
            count = 0
            for i in s:
                if i not in seen:
                    seen.append(i)
                    count += 1
                    if count == len(s):
                        lists_count.append(count)
                else:
                    lists_count.append(count)
                    seen = []
                    break
            s.pop(0)
        if len(lists_count) == 0:
            return 0
        return max(lists_count)
        