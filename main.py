import sheets_functions
import grader
import time

def main():
    sheet_name = input("Please enter the name of the sheet: ")
    grades = grader.grade()
    row = 4
    for student in grades:
        data = {
            "values" : [ 
                [student, 
                 grades[student].get("ela scaled score"),
                 grades[student].get("math scaled score"),
                 grades[student].get("total scaled score")
                ] 
            ]
        }
        sheets_functions.write_data(sheet_name, "B" + str(row), data)
        print(student + " grades added to sheet.")
        time.sleep(1)
        row += 1
    total_questions_correct = grader.all_correct_questions()
    total_questions_incorrect = grader.all_incorrect_questions()
    row = 4
    for question_number in range(1, 115): 
        data = {
            "values" : [ 
                [question_number, 
                 total_questions_correct.count(question_number),
                 total_questions_incorrect.count(question_number)
                ] 
            ]
        }
        sheets_functions.write_data(sheet_name, "G" + str(row), data)
        print("Data for " + str(question_number) + " added to sheet.")
        time.sleep(1)
        row += 1
    print("Complete.")
if __name__ == "__main__":
    main()
