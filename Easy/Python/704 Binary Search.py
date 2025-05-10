#704. Binary Search
class Solution(object):
    def search(self, s, val):
        a = len(s)
        b = 0
        for i in range(len(s)):
            i = int((a+b)/2)

            if s[i] > val: 
                a = i
            elif s[i] < val:
                b = i
            else: 
                return i 
        return -1