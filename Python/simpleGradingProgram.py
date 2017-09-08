#   This is a simple grading program to showcase the IF/ELIF/ELSE cases
#   We will convert a number score to a letter grade

yourGrade = raw_input("What is your current mark: ")

def letterGrade(yourGrade):
    if yourGrade >=90:
        letter = "A"
    elif yourGrade >=80:
        letter = "B"
    elif yourGrade >=70:
        letter = "C"
    elif yourGrade >=50:
        letter = "D"
    elif yourGrade <50:
        letter = "F"

    finalGrade = "Your final mark is " + letter
    return finalGrade

print letterGrade(int(yourGrade))

