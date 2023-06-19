print("Enter Marks Obtained in 5 subjects: ")
sub1 = int(input())
sub2 = int(input())
sub3 = int(input())
sub4 = int(input())
sub5 = int(input())

total = sub1+sub2+sub3+sub4+sub5
average = total/5
percentage = (total/500.0)*100

if average>=90:
    grade = 'A'
elif average>=80 and average<90:
    grade = 'B'
elif average>=70 and average<80:
    grade = 'C'
elif average>=60 and average<70:
    grade = 'D'
else:
    grade = 'E'

print(" The Total marks obtained are: ",total)
print(" The average marks are: ",average)
print(" The percentage is: ",percentage,"%")
print(" The Grade is: ", grade)
