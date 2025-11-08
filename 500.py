class Solution:
    def findWords(self, words):
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")
        res = []
        for w in words:
            s = set(w.lower())
            if s <= row1 or s <= row2 or s <= row3:
                res.append(w)
        return res
