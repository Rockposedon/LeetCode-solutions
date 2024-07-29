# 1st Approach got the TLE due to nested looping
"""
class Solution:
    def numTeams(self, rating: List[int]) -> int:
        
        result = 0
        n = len(rating)
        
        # Iterate through each possible triplet
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    if (rating[i] < rating[j] < rating[k]) or (rating[i] > rating[j] > rating[k]):
                        result += 1
        
        return result
"""
class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        count = 0
        
        for j in range(n):
            left_less = left_greater = right_less = right_greater = 0
            
            for i in range(j):
                if rating[i] < rating[j]:
                    left_less += 1
                elif rating[i] > rating[j]:
                    left_greater += 1
            
            for k in range(j + 1, n):
                if rating[k] < rating[j]:
                    right_less += 1
                elif rating[k] > rating[j]:
                    right_greater += 1
            
            count += left_less * right_greater + left_greater * right_less
        
        return count
        
