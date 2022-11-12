import sheets_functions
import pprint

answer_key = sheets_functions.get_range("Answer Key!B2:B115")
print("Answer key populated.")

students = sheets_functions.read_sheets()
print("Students' sheets retrieved.")

student_answers = []

for student in students:
    student_answers.append([student, sheets_functions.get_range(student + "!B2:B115")])
print("Students' answers populated.")


grades = {}
total_questions_correct = []
total_questions_incorrect = []

scale = {1:14,2:30,3:39,4:54,5:68,6:79,7:90,8:100,9:111,10:118,11:126,12:135,13:141,14:147,15:153,16:158,17:163,18:169,19:173,20:178,21:183,22:187,23:191,24:194,25:197,26:201,27:204,28:208,29:212,30:215,31:219,32:222,33:226,34:229,35:232,36:236,37:240,38:243,39:247,40:250,41:254,42:257,43:261,44:265,45:269,46:274,47:278,48:283,49:290,50:298,51:305,52:314,53:323,54:333,55:342,56:352,57:360}

def grade():
    for student in student_answers:
        print("Grading " + student[0] + ".")
        data = {}
        correct_answers = 0
        correct_questions = []
        incorrect_questions = []
        ela_correct_answers = 0
        math_correct_answers = 0
        for answer in range(len(answer_key)):
            # print(count)
            # print("correct answer: ")
            # print(answer)
            # print("student answer: ")
            # print(student[1][count])
            if student[1][answer] == answer_key[answer]:
                correct_answers += 1
                if answer < 57:
                    ela_correct_answers += 1
                else:
                    math_correct_answers += 1
                correct_questions.append(answer + 1)
                total_questions_correct.append(answer + 1)
                # print("correct")
            else: 
                incorrect_questions.append(answer + 1)
                total_questions_incorrect.append(answer + 1)
        data.update({"correct answers":correct_answers})
        data.update({"questions answered correct":correct_questions})
        data.update({"questions answered incorrect":incorrect_questions})
        data.update({"ela correct answers":ela_correct_answers})
        data.update({"math correct answers":math_correct_answers})
        data.update({"ela scaled score":scale[ela_correct_answers]})
        data.update({"math scaled score":scale[math_correct_answers]}) 
        data.update({"total scaled score":scale[ela_correct_answers] + scale[math_correct_answers]})
        grades.update({student[0]:data})
    print("Grading complete.")
    return grades

def all_correct_questions():
    return total_questions_correct

def all_incorrect_questions():
    return total_questions_incorrect

# print(grades)
# pprint.pprint(grades)


    

            
        