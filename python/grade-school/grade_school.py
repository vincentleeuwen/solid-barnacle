class School(object):
    students = dict()

    def __init__(self, name):
        self.name = name
        for i in range(1, 9):
            self.students[i] = set()

    def add(self, student, grade):
        self.students[grade].add(student)

    def grade(self, grade):
        return self.students[grade]

    def sort(self):
        sorted_students = []
        for grade in self.students.keys():
            if self.students.get(grade):
                sorted_students.append((grade, tuple(sorted(self.students[grade]))))
        return sorted_students
