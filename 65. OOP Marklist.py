class Student:
    def __init__(self,roll,Name,mid1_marks,mid2_marks,quiz_marks):
        self.roll = roll
        self.Name = Name
        self.mid1_marks = mid1_marks
        self.mid2_marks = mid2_marks
        self.quiz_marks = quiz_marks
    def marksList(self):
        print("ROLL NUMBER:",self.roll)
        print("NAME:",self.Name)
        print("MID1:",self.mid1_marks)
        print("MID2:",self.mid2_marks)
        print("QUIZ:",self.quiz_marks)
        total = self.mid1_marks + self.mid2_marks + self.quiz_marks
        print("TOTAL:",total)
        if(total>=80):
            print("GRADE: A GRADE")
        elif(total<80 and total>=60):
            print("GRADE: B GRADE")
        elif(total<60 and total>=50):
            print("GRADE: C GRADE")
        else:
            print("Fail!!")
s = Student(361,"Kavya",8,2,20)
s.marksList()
        
