class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        
        for detail in details:
            # Extract age (characters at index 11 and 12)
            age = int(detail[11:13])
            # Check if age is strictly more than 60
            if age > 60:
                count += 1
        return count
                    
                    