print('GPA Calculator')

A = 4
B = 3
C = 2
D = 1
F = 0

num_classes = int(input('How many classes are you taking (enter number)? '))
grades = []

for i in range(num_classes):
    letter = input('Enter letter grade: ').upper()
    if letter == 'A':
        grades.append(A)
    elif letter == 'B':
        grades.append(B)
    elif letter == 'C':
        grades.append(C)
    elif letter == 'D':
        grades.append(D)
    elif letter == 'F':
        grades.append(F)
    else:
        print('Invalid grade entered') 

GPA = sum(grades) / num_classes

print('Your GPA is a ' + str(GPA))




