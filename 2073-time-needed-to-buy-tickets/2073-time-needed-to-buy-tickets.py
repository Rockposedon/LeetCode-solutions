class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        n = len(tickets)
        count1 = 0
        
        while tickets[k] > 0:
            
            for i in range(n):
                if tickets[i] != 0:
                    tickets[i] -= 1
                    count1 += 1
                    
                    if tickets[k] == 0:
                        return count1
        return count1