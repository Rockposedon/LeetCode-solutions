# 1st Approach(wrong answer)
"""
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        n = len(students)
        for i in range(n):
            if students[i] == sandwiches[i]:
                students.pop(0)
                sandwiches.pop(0)
            elif students[i] != sandwiches[i]:
                students.append(students.pop(0))
        return len(students)

"""

# 2nd Approach(limit exceed)
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        
        """
            circular count --> c_count
            square count --> s_count
            sandwiches_count --> sd_count
            remaining students --> rm_students
        """
        
        """n = len(students)
        c_count = students.count(0)
        s_count = n - c_count
        
        m = len(sandwiches)
        sd_count = sandwiches.count(0)
        cd_count = n - sd_count
        
        if sd_count >= c_count:
            return 0
        
        rm_students = min(c_count-sd_count,s_count)
        return rm_students
        """
 
# 3rd Approach(Working)

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        while len(sandwiches)!=0 and sandwiches[0] in students:
            if students[0]==sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
            else:
                students.append(students.pop(0))
        return len(students)
