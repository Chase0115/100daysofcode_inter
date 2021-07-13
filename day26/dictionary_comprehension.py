# new_dict = {new_key: new_value for item in list}
# OR
# new_dict = {new_key: new_value for (key,value) in dict.items()}

# new_dict = {new_key: new_value for (key,value) in dict.items() if condition}


# import random

names = ["Alexa", "Siri", "Bixbi", "Dave", "Alex"]

student_score = {
    'Alexa': 85,
    'Siri': 10,
    'Bixbi': 15,
    'Dave': 76,
    'Alex': 79
}

# student_score = {student:random.randint(1,100) for student in names}
#
# print(student_score)

passed_students = {student:  score for (student, score) in student_score.items()
                   if student_score[student] > 60}
print(passed_students)

