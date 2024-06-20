def main():
    students = [1, 1, 1, 0, 0,1 ]
    sandwiches = [1, 0, 0, 0, 1, 1]
    print(countStudents(students, sandwiches))
    
def countStudents(students: list[int], sandwiches: list[int]) -> int:
    # if there are no students
    if len(students) == 0:
        return len(students)
    
    # if there are no sandwiches
    if len(sandwiches) == 0:
        return len(students)
    
    # normal case: there are students and sandwiches
    count = 0
    while count != len(students):
        # if student take sandwich
        if students[0] == sandwiches[0]:
            students = students[1:]
            sandwiches = sandwiches[1:]
            count = 0
        # if student doesn't take sandwich
        else:
            students.append(students[0])
            students = students[1:]
            count += 1
        
        # if students do not prefer sandwich
        if count == len(students):
            return len(students)
    
main()