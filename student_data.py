import csv

total_students = 0
total_age = 0
student_list = []

with open("students.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        total_students += 1
        age = int(row["Age"])
        total_age += age
        student_list.append(row["Name"])

average_age = total_age / total_students

print("===== Student Report =====")
print("Total Students :", total_students)
print("Average Age    :", round(average_age, 2))

print("\nStudent List:")
for student in student_list:
    print("-", student)
