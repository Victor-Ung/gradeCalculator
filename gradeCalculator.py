print("Hello, this is a simple grade calculator program")
while True:
    try:
        numberOfStudents = int(input("How many students do you have? "))
        if numberOfStudents > 35:
            print("Sorry, that is way too many students for this program to handle")
        elif numberOfStudents == 0:
            print("Sorry, it looks like you entered 0 students")
        elif numberOfStudents < 0:
            print("Sorry, it looks like you entered a negative number")
        else:
            break
        
    except ValueError:
        print("Whoops, looks like that was not an integer.")
        continue

while True:
    try:
        homeworkWeight = int(input("How much % are homework assignments worth? "))
        homeworkWeight = homeworkWeight / 100

        quizzesWeight = int(input("How much % are quizzes worth? "))
        quizzesWeight = quizzesWeight / 100

        testsWeight = int(input("How much % are tests worth? "))
        testsWeight = testsWeight / 100
       
        break
   
    except ValueError:
        print("Whoops, looks like that was not an integer.")
        continue

def average(numbers):
    average = float(sum(numbers))/len(numbers)   
    return average

def getAverage(student):
  homework = average(Data["homework"])
  quizzes = average(Data["quizzes"])
  tests = average(Data["tests"])
  
  homework = float(homework) * float(homeworkWeight)
  quizzes = float(quizzes) * float(quizzesWeight)
  tests = float(tests) * float(testsWeight)

  total = homework + quizzes + tests

  return total

def getLetterGrade(score):
  if score >= 90:
    return "A"
  elif score >= 80:
    return "B"
  elif score >= 70:
    return "C"
  elif score >= 60:
    return "D"
  else :
    return "F"

for students in range(numberOfStudents):
    Data = {"name": [],
            "homework": [],
             "quizzes": [],
             "tests": []}
    studentName = input("What is the name of your student? ")
    Data["name"].append(studentName)
    numberOfHomeworks = int(input("How many homework assignments do you want to enter? "))
    for homeworkAmount in range(numberOfHomeworks):
        homework = float(input("How much did the student get for the homework assignment? "))
        Data["homework"].append(homework)
    numberOfQuizzes = int(input("How many quizzes do you want to enter? "))
    for quizAmount in range(numberOfQuizzes):
        quiz = float(input("How much did the student get for this quiz? "))
        Data["quizzes"].append(quiz)
    numberOfTests = int(input("How many Tests do you want to enter? "))
    for TestsAmount in range(numberOfTests):
        test = float(input("How much did the student get for this test? "))
        Data["tests"].append(test)
    print("{} has a(n) {} letter grade with an average of {:.2f}.".format(studentName, getLetterGrade(getAverage(studentName)), getAverage(studentName)))

