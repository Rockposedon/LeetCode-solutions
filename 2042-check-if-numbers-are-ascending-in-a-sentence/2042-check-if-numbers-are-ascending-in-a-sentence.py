class Solution(object):

        def areNumbersAscending(self, s):
        # split strin into list of substrings
            l=s.split() 
        
        # n to store the previous number
            n = 0 
            for i in l:
                if i.isdigit():
                
                
                    if int(i) <= n: #if at any point the previous number is greater, return False
                        return False
                    n = int(i) #update the previous number
            return True