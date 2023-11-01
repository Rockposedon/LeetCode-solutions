class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        
        # Helper function to traverse the tree and count values
        def traverse(node, value_count):
            if node is None:
                return value_count

            # Increment the count for the current node's value
            if node.val in value_count:
                value_count[node.val] += 1
            else:
                value_count[node.val] = 1

            # Recursively traverse the left and right subtrees
            if node.left is not None:
                value_count = traverse(node.left, value_count)
            if node.right is not None:
                value_count = traverse(node.right, value_count)

            return value_count

        # Initialize a dictionary to store value counts
        value_count = dict()

        # Call the helper function to traverse the tree and count values
        value_count = traverse(root, value_count)

        # Find the maximum count in the dictionary
        max_count = max(value_count.values())

        # Return a generator with values that have a count equal to the maximum
        return (value for value, count in value_count.items() if count == max_count)
