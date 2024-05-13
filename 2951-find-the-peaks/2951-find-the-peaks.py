class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        # peak list to store the peak of mountain
        peak = []
        
        # Iterating in mountain while excluding first and last element
        for i in range(1,len(mountain)-1):
            
            # Checking peak element conditions 
            if mountain[i-1] < mountain[i] > mountain[i+1]:
                
                # Adding index of peak from mountain in peak list
                peak.append(i)
                
        # Returning index list of peak from mountain
        return peak