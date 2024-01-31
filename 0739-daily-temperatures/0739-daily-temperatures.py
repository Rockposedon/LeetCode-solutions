# class Solution:
#     def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
#         n = len(temperatures)
#         list1 = []

#         i = 0
#         while i < n - 1:
#             if temperatures[i] < temperatures[i+1]:
#                 list1.append(1)
#             elif temperatures[i] > temperatures[i+1]:
#                 j = i + 1
#                 while j < n - 1 and temperatures[i] > temperatures[j]:
#                     j += 1
#                 if j < n - 1:
#                     list1.append(j - i)
#                 else:
#                     list1.append(0)
#             else:
#                 list1.append(0)
#             i += 1

#         list1.append(0)
#         return list1
class Solution:
    def dailyTemperatures(self, temperatures):
        n = len(temperatures)
        answer = [0] * n
        stack = []

        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                index = stack.pop()
                answer[index] = i - index
            stack.append(i)

        return answer