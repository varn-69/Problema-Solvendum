class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        c = Counter(magazine)
        for k in ransomNote:
            if c[k] == 0:
                return False
            c[k] -=1
        return True
        