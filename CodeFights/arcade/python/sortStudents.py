def sortStudents(students):
    students.sort(key=lambda name: name.split(' ')[-1])
    return students
