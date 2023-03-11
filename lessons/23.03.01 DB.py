import pandas as pd

table = pd.DataFrame({
    'name': [],
    'age': [],
    'grades': [],
})



class Student:
    def __init__(self, name, age, grade, inf=None):
        self.name = name
        self.age = age
        self.grade = grade
        self.inf = inf 
    

class Table:
    def __init__(self):
        self.name = []
        self.age = []
        self.grade = []
        self.inf = []


    def add_student(self, student):
        self.name.append(student.name)
        self.age.append(student.age)
        self.grade.append(student.grade)
        self.inf.append(student.inf)


    def delete_student(self, student):
        self.name.remove(student.name)
        self.age.remove(student.age)
        self.grade.remove(student.grade)
        self.inf.remove(student.inf)


    def get_av_grades(self):
        res = 0 
        for i in self.grade:
            res += int(i)
        return res/len(self.grade)


    def change_inf(self, name):
        index = self.name.index(name)
        self.inf[index] = str(input())


    def get_table(self):
        data = pd.DataFrame({'name': self.name,
                             'age': self.age,
                             'grade': self.grade,
                             'info': self.inf
                             })
        return data


students = Table()
petar = Student('Petar', '20', '5', 'rap')
lobachevskiy = Student('lobachevskiy', '16', '2', 'good genshin impact [i][j]')
base = Student('Base', '16,','5')

students.add_student(petar)
students.add_student(lobachevskiy)
students.add_student(base)


print(students.get_table())

students.delete_student(base)
students.change_inf('Petar')
print(students.get_table())
