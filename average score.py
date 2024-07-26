import numpy as np

# Sample student scores (10 students, 4 subjects: Math, Science, English, History)
student_scores = np.array([
    [85, 90, 78, 92],
    [88, 76, 85, 80],
    [90, 88, 92, 85],
    [78, 81, 74, 88],
    [82, 85, 88, 86],
    [90, 91, 85, 89],
    [88, 84, 82, 80],
    [85, 79, 88, 91],
    [87, 82, 84, 78],
    [80, 86, 90, 84]
])

# Calculate the average score for each subject
average_scores = np.mean(student_scores, axis=0)

# Identify the subject with the highest average score
subjects = ['Math', 'Science', 'English', 'History']
highest_average_subject = subjects[np.argmax(average_scores)]

# Print the results
print("Average scores for each subject:", average_scores)
print("Subject with the highest average score:", highest_average_subject)
