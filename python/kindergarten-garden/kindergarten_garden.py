class Garden(object):
    students = [
        'Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Fred', 'Ginny', 'Harriet',
        'Ileana', 'Joseph', 'Kincaid', 'Larry'
    ]
    # grass, clover, radishes, and violets
    plant_map = {
        'C': 'Clover',
        'G': 'Grass',
        'R': 'Radishes',
        'V': 'Violets',
    }
    plants_per_student = 2

    def __init__(self, diagram, students=None):
        if students:
            self.students = students
            self.students.sort()
        self.diagram = diagram.split('\n')

    def plants(self, student):
        planted = []
        for d in self.diagram:
            for i in range(
                self.students.index(student) * self.plants_per_student,
                    self.students.index(student) * self.plants_per_student +
                    self.plants_per_student):
                        planted.append(self.plant_map[d[i]])
        return planted
