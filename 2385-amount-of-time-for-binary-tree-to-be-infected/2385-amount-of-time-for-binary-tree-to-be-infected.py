# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        adjacency_list = defaultdict(list)
        stack = [(root, None)]
        
        while stack:
            current_node, parent_node = stack.pop()
            
            if parent_node:
                adjacency_list[parent_node.val].append(current_node.val)
                adjacency_list[current_node.val].append(parent_node.val)
            
            if current_node.left:
                stack.append((current_node.left, current_node))
            
            if current_node.right:
                stack.append((current_node.right, current_node))
        
        steps = -1
        visited = {start}
        node_queue = deque([start])
        
        while node_queue:
            for _ in range(len(node_queue)):
                current_node = node_queue.popleft()
                
                for neighbor in adjacency_list[current_node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        node_queue.append(neighbor)
            
            steps += 1
        
        return steps