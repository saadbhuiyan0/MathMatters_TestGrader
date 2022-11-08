import sheets_functions
import grader

def main():
    sheet_name = input("Please enter the name of the sheet: ")
    row = 4
    grades = grader.grade()
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
        sheets_functions.write_data(sheet_name, "A" + str(row), data)
        print(student + " grades added to sheet.")
        row += 1
    print("Complete.")
    
if __name__ == "__main__":
    main()
