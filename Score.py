import csv 
from colorama import Fore, Back, Style
scale = {1:14,2:30,3:39,4:54,5:68,6:79,7:90,8:100,9:111,10:118,11:126,12:135,13:141,14:147,15:153,16:158,17:163,18:169,19:173,20:178,21:183,22:187,23:191,24:194,25:197,26:201,27:204,28:208,29:212,30:215,31:219,32:222,33:226,34:229,35:232,36:236,37:240,38:243,39:247,40:250,41:254,42:257,43:261,44:265,45:269,46:274,47:278,48:283,49:290,50:298,51:305,52:314,53:323,54:333,55:342,56:352,57:360}

# -------------------CREATING CORRECT ANSWERS DICTIONARY-------------

correct_answers = {}
with open('correct.csv') as file:
	reader = csv.reader(file)
	count = 0

	for row in reader:
		correct_answers[row[0]] = row[1]

correct_answers.pop('\ufeffnumber')

int_correct_answers = {}

for key in correct_answers:
	int_correct_answers[int(key)] = correct_answers[key]

ela_correct_answers = {}
math_correct_answers = {}

for key in int_correct_answers:
	#print(key)
	if key < 58:
		ela_correct_answers[key] = int_correct_answers[key]
	elif key > 57:
		math_correct_answers[key] = int_correct_answers[key]


# -------------------CREATING STUDENT ANSWERS DICTIONARY-------------

student_answers = {}
with open('student.csv') as file:
	reader = csv.reader(file)
	count = 0

	for row in reader:
		student_answers[row[0]] = row[1]

student_answers.pop('\ufeffnumber')

int_student_answers = {}

for key in student_answers:
	int_student_answers[int(key)] = student_answers[key]

ela_student_answers = {}
math_student_answers = {}

for key in int_student_answers:
	if key < 58:
		ela_student_answers[key] = int_student_answers[key]
	elif key > 57:
		math_student_answers[key] = int_student_answers[key]

# ------------------------CALCULATING STUDENT ANSWERS-----------------


student_correct_math_counter = 0
student_correct_ela_counter = 0

student_wrong_math_counter = 0
student_wrong_ela_counter = 0

student_correct_math_list = []
student_correct_ela_list = []

student_wrong_math_list = []
student_wrong_ela_list = []

for i in range(1,58):
	if ela_correct_answers[i] == ela_student_answers[i]:
		student_correct_ela_counter = student_correct_ela_counter + 1
		student_correct_ela_list.append(i)
	elif ela_correct_answers[i] != ela_student_answers[i]:
		student_wrong_ela_counter = student_wrong_ela_counter + 1
		student_wrong_ela_list.append(i)

for i in range(58,115):
	if math_correct_answers[i] == math_student_answers[i]:
		student_correct_math_counter = student_correct_math_counter + 1
		student_correct_math_list.append(i)
	elif math_correct_answers[i] != math_student_answers[i]:
		student_wrong_math_counter = student_wrong_math_counter + 1
		student_wrong_math_list.append(i)

scaled_math = scale[student_correct_math_counter]
scaled_ela = scale[student_correct_ela_counter]


print(Fore.RED + "-----------------------------PRINTING MATH-------------------")
print(f'Math Questions Correct: {student_correct_math_counter}')
print(f'Math Questions Wrong: {student_wrong_math_counter}')
print(f'Scaled Math Score: {scaled_math}/400 ')
print(f'List of Math Correct {student_correct_math_list}')
print(f'List of Math Wrong {student_wrong_math_list}')
print(Fore.YELLOW +"-----------------------------PRINTING ELA-------------------")
print(f'ELA questions correct: {student_correct_ela_counter}')
print(f'ELA questions Wrong: {student_wrong_ela_counter}')
print(f'Scaled ELA Score: {scaled_ela}/400 ')
print(f'List of ELA Correct {student_correct_ela_list}')
print(f'List of ELA Wrong {student_wrong_ela_list}')
print(Fore.GREEN +"-----------------------------PRINTING TOTAL-------------------")
print(f'Total score is {scaled_ela + scaled_math}/800')












