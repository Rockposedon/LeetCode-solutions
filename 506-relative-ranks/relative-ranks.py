class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_score = sorted(score,reverse=True)
        dictionary = {}
        
        for i in range(len(sorted_score)):
            if i == 0:
                dictionary[sorted_score[i]] = "Gold Medal"
            elif i == 1:
                dictionary[sorted_score[i]] = "Silver Medal"
            elif i == 2:
                dictionary[sorted_score[i]] = "Bronze Medal"
            else:
                dictionary[sorted_score[i]] = str(i+1)
        
        result = []
        for i in score:
            result.append(dictionary[i])
        return result 