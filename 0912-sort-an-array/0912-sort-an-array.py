class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        # Function to perform merge sort
        def merge_sort(arr):
            if len(arr) > 1:
                mid = len(arr) // 2
                left = arr[:mid]
                right = arr[mid:]
                
                # Recursively sort the left and right halves
                merge_sort(left)
                merge_sort(right)

                # Merge the sorted halves
                i = j = k = 0
                while i < len(left) and j < len(right):
                    if left[i] <= right[j]:
                        arr[k] = left[i]
                        i += 1
                    else:
                        arr[k] = right[j]
                        j += 1
                    k += 1

                # Check if any element was left
                while i < len(left):
                    arr[k] = left[i]
                    i += 1
                    k += 1
                while j < len(right):
                    arr[k] = right[j]
                    j += 1
                    k += 1

        merge_sort(nums)
        return nums
