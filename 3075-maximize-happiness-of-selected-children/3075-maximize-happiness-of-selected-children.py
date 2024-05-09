"""
# Approach 1 (Divide and conqurer)
class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort()
        h_ch = []
        if k == 1:
            h_ch = happiness.pop()
            return h_ch
        else:
            n = len(happiness)
            
            while k >= 1:
                for i in range (0,n):
                    # h_ch.append(happiness.pop())
                    if n >= 1:
                        happiness[i] -= 1
                        h_ch.append(happiness.pop())
                k -= 1
            return sum(h_ch)
"""
class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)  
        total_happiness_sum = 0
        for i in range(k):
            if happiness[i] - i > 0:  # Check if happiness is positive before decrementing
                total_happiness_sum += happiness[i] - i
        return total_happiness_sum