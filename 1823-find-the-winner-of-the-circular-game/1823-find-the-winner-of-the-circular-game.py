""" Simple Approach using while loop """
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        
        # Initialize a list with friend numbers from 1 to n because, we are not having any array
        friend_list = list(range(1, n + 1))
        
        index = 0  # Start from the first friend

        # Continue the elimination process until only one friend remains
        # using while loop till length of friend_list greater then 1 
        while len(friend_list) > 1:
            
            # Calculate the index to remove based on the given pattern
            index = (index + k - 1) % len(friend_list)
            
            # Remove the k-th friend based on index 
            friend_list.pop(index)
        
        # Return the remaining friend who is the winner
        return friend_list[0]
        
        
""" Another approach in which I am calculate length of friend list"""      
# class Solution:
#     def findTheWinner(self, n: int, k: int) -> int:
#         initial_list = list(range(1,n+1))
#         n = len(initial_list)
        
#         index_value = 0
        
#         while n > 1:
#             index_value = (index_value + k -1) % n
#             initial_list.pop(index_value)
#             n -= 1
#         return initial_list[0]
