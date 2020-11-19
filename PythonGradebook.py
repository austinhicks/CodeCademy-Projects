# Python Gradebook project from CodeCademy
# 11/19/2020

# Came in project already
last_semester_gradebook = [("politics", 80), ("latin", 96), ("dance", 97), ("architecture", 65)]

# subjects contains what classes I'm taking
subjects = ['physics', 'calculus', 'poetry', 'history']

# grades contains my scores
grades = [98, 97, 85, 88]

# add additional grade for computer science
subjects.append('computer science')
grades.append(100)

# combine subjects and grades with zip()
gradebook = list(zip(subjects, grades))

# add a pair to the combined list
gradebook.append(('visual arts', 93))

print(gradebook)

full_gradebook = last_semester_gradebook + gradebook

print(full_gradebook)