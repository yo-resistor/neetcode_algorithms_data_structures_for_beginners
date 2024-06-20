class Solution:
    def countStudents(self, students: list[int], sandwiches: list[int]) -> int:
        count = 0
        
        while count != len(students):
            # first student takes first sandwich
            if students[0] == sandwiches[0]:
                students = students[1:]
                sandwiches = sandwiches[1:]
                count = 0
            # first students cannot take first sandwich
            else:
                students.append(students[0])
                students = students[1:]
                count += 1
            
        return len(students)
    

sol = Solution()

students = [1, 1, 0, 0]
sandwiches = [0, 1, 0, 1]    
print(sol.countStudents(students, sandwiches))

students = [1, 1, 1, 0, 0, 1]
sandwiches = [1, 0, 0, 0, 1, 1]    
print(sol.countStudents(students, sandwiches))