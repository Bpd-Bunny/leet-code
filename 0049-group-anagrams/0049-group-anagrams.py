from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = defaultdict(list)
        for i in strs:
            count = [0]*26
            for j in i:
                count[ ord(j) - ord('a')] += 1

            key= tuple(count)
            anagram_dict[key].append(i)

        return anagram_dict.values()        