marks_dict = {
    "Manju": 72,
    "Ram": 90,
    "Krishna": 45,
    'Hanuman': 25,
    'Ganesh': 86,
    "Manu": 95,
    'Swamy': 78
}

grade_dict = {}
grade_dict = dict()

for name in marks_dict:
    marks = marks_dict[name]
    grade = ''
    if marks >= 91:
        grade = 'A+'
    elif marks >= 81 and marks <= 90:
        grade = 'A'
    elif marks >= 71 and marks <= 80:
        grade = 'B+'
    elif marks >= 61 and marks <= 70:
        grade = 'B'
    elif marks >= 51 and marks <= 60:
        grade = 'C+'
    elif marks >= 41 and marks <= 50:
        grade = 'C'
    elif marks >= 31 and marks <= 40:
        grade = 'D'
    else:
        grade = 'H'

    grade_dict[name] = grade

print(marks_dict)
print(grade_dict)
