'''
Problem Statement: Student Performance Tracker using Python Dictionary
You are building a Student Performance Tracker for a training institute.
Each student is identified by a unique student ID and has the following details:
Name
Marks in three subjects: Maths, Science, English

You must use Python dictionaries to store and manage this data.
Requirements
Create a dictionary where:
Key → student_id
Value → another dictionary containing:
name
maths
science
english

Implement the following operations using dictionary logic only:
Add a new student
Update marks of an existing student
Delete a student record
Display all student details

Compute and display:
Total marks for each student
Average marks for each student
Grade based on average:
A → avg ≥ 80
B → avg ≥ 60 and < 80
C → avg < 60

Find:
Student with highest average
Student with lowest average
'''

Student_Performance_Tracker={
    "student_id":[1,2,3,4],
    "student_name":["Subhojit","Adwait","Cindy","Sonali"],
    "marks_math":[100,99,50,90],
    "marks_science":[100,98,80,100],
    "marks_english":[70,30,20,89]
}

#print(Student_Performance_Tracker)
for i in Student_Performance_Tracker["student_id"]:
    #print(i)
    #print(Student_Performance_Tracker["student_id"][i-1])
    #print(f"Student Roll Number:\t{Student_Performance_Tracker["student_id"][i-1]}\tName:\t{Student_Performance_Tracker["student_name"][i-1]}\tMath:\t{Student_Performance_Tracker["marks_math"][i-1]}\t")
    total_marks=Student_Performance_Tracker["marks_math"][i-1]+Student_Performance_Tracker["marks_science"][i-1]+Student_Performance_Tracker["marks_english"][i-1]
    avg_marks=total_marks/3
    if avg_marks >= 80:
        gread="A"
    elif avg_marks >= 60:
        gread="B"
    else:
        gread="C"            
    #print(f"Total Marks for Student: {Student_Performance_Tracker["student_name"][i-1]} is {Student_Performance_Tracker["marks_math"][i-1]+Student_Performance_Tracker["marks_science"][i-1]+Student_Performance_Tracker["marks_english"][i-1]}")
    print(f"Total marks for student {Student_Performance_Tracker["student_name"][i-1]} is {total_marks} and average marks is {avg_marks:.2f} and Gread is {gread}")