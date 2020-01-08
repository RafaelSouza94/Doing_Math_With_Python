import correlation
import matplotlib.pyplot as plt

grades_general = [90, 92, 95, 96, 87, 87, 90, 95, 98, 96]
grades_math = [83, 85, 84, 96, 94, 86, 87, 97, 97, 85]
exam_results = [85, 87, 86, 97, 96, 88, 89, 98, 98, 87]

plt.title("Scatter General Grades x Exam Results")
plt.xlabel("General grades")
plt.ylabel("Exam results")
plt.scatter(grades_general, exam_results)
plt.show()

plt.title("Scatter Math Grades x Exam Results")
plt.xlabel("Math grades")
plt.ylabel("Exam results")
plt.scatter(grades_math, exam_results)
plt.show()