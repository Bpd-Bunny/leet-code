class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counter = defaultdict(int)
        balloon = 'balloon'

        for s in text:
            if s in balloon:
                counter[s] += 1
        
        if any( c not in counter for c in counter ):
            return 0
        
        return min(counter['b'], counter['a'], counter['l']//2, counter['o']//2, counter['n'])