class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        
        res = numBottles
        empty = numBottles
        
        while empty>=numExchange:
            
            empty-=numExchange
            
            if empty>=0: #because if it is -ve then exchange won't be possibe
                res+=1 #will drink instantly
                numExchange+=1 #following the condition
                empty+=1
                
            else:
                break

            
        
        return(res)