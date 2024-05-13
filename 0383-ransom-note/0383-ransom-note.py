from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counter = Counter(magazine)
        for i in ransomNote:
            if i not in counter:
                return False
            if counter[i] == 1:
                del counter[i]
            if i in counter:
                counter[i] -=1
        return True