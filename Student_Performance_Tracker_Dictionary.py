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
def main():
    Student_Performance_Tracker={
        "student_id":[1,2,3,4],
        "student_name":["Subhojit","Adwait","Cindy","Sonali"],
        "marks_math":[100,99,50,90],
        "marks_science":[100,98,80,100],
        "marks_english":[70,30,20,89]
    }
    print("Initial Student_Performance_Tracker\t")
    display_students_stats(Student_Performance_Tracker)   
# Calling Function to add new students and their marks -------------------------------------------    
    Student_Performance_Tracker=insert_Student_Performance_Tracker(Student_Performance_Tracker)
    display_students_stats(Student_Performance_Tracker)

def display_students_stats(SPT):
         for i in SPT["student_id"]:
            total_marks=SPT["marks_math"][i-1]+SPT["marks_science"][i-1]+SPT["marks_english"][i-1]
            avg_marks=total_marks/3
            if avg_marks >= 80:
                gread="A"
            elif avg_marks >= 60:
                gread="B"
            else:
                gread="C"            
            print(f"Total marks for student {SPT["student_name"][i-1]} is {total_marks} and average marks is {avg_marks:.2f} and Gread is {gread}")    

def insert_Student_Performance_Tracker(new_std):
    while True:
        response=input("Do you want to insert a new student details?(Y/y|N/n)").strip().upper()
        if response == "Y" or response == "N":
            #continue
            if response == "Y":
                last_student_id=(new_std["student_id"][-1])
                name=input("Please enter the name you want to add:\t").strip().title()
                math_marks=int(input(f"Please enter the math marks for {name}:\t").strip())
                science_marks=int(input(f"Please enter the science marks for {name}:\t").strip())
                english_marks=int(input(f"Please enter the english marks for {name}:\t").strip())
                new_std["student_id"].append(last_student_id+1)
                new_std["student_name"].append(name)
                new_std["marks_math"].append(math_marks)
                new_std["marks_science"].append(science_marks)
                new_std["marks_english"].append(english_marks)
            else:
                print("Thank you for using this programme, as you have chosen nothing to add bye for now!")
                return new_std
                break    
        else:
            print(f"Please provide valid input(Y/y|N/n)), your input was {response}")
            break


main()