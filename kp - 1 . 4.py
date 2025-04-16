class Student:
    '''неуд по матану'''
    def __init__ (self , student_name , marks ):
        self.student_name = student_name
        self.marks = marks
        self.nmarks = nmarks
    def gg(self , student_name , marks , f):
        print(student_name , max(marks))
        print("хотите поменять оценку?")
        c = input()
        if c == 'yes':
            print('введите  новые оценки студента')
            marks = input().split()
        for k in range(0, len(marks)):
            f = f + int(marks[k])
        g = float(f / len(marks))

        print(" {0}, {1} , {2}".format(student_name,"средняя оценка", g ))
f = 0
nmarks = 0
print('введите имя студента')
student_name = input()
print('введите оценки студента')
marks = input().split()
opred = Student(student_name , marks )
opred.gg(opred.student_name , opred.marks , f)
