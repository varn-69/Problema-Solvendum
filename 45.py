class Solution:
    def titleToNumber(self, columnTitle):
        res = 0
        for c in columnTitle:
            res = res * 26 + ord(c) - 64
        return res
