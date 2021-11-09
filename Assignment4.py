"""Assignment 4: Validating data
by Steven Michalove
Nov 6 2011
Objectives
In this assignment you will learn how to validate data in your automated interview.

Instructions
Start by reviewing the entire problem described below.
When you are familiar with the requirements, start to plan how you will write the Python code.
As you write the code be sure to test it frequently.
Submit your complete assignment when you are sure you have implemented all of the requirements.
Basics
You will recall that from last weeks' assignment we have two files:

Firstly

questionid, sequencenumber, question,deletedflag

10,1,”What is your email”, False

And then

questionid,nameofpersoninterviewed,answer

2,”Andy”,”akmiles@uw.edu”

In this weeks' assignment we are going to add validation and exception tracking code to last week's submission.

Here are the steps you need to follow. We start with the questions file.

Write new functionality that will read through the questions file one record at a time.
For each record, ask the user to validate that the question is correct.
"Correct" means the user is happpy with the wording.
ALso, the question must be between 10 and 30 character long. 3.Display a message that asks the user
if they wish to correct the question. Then capture corrected value as needed.
Also ask the user if the question is needed, or if it should be deleted. Validate the users
repsonse and allow them to retry entering an answer.
If the user wants to delete the question, ask if they are sure. Validate the user's input,
 and then either delete or move on.
Introduce validations using a similar pattern for at least 3 more questions.
HINT: be sure to get the validations in the correct sequence, so the flow makes sense to the user.
Also, you may wish to open the current file for reading, and create a new file, that gets "flipped"
back to the original filename when done.

BE VERY CAREFUL TO MAINTAIN RELATIONSHIPS BETWEEN EXISTING QUESTIONS AND THEIR ANSWERS.

Now to the answers file:

Add code to make sure that the email address is provided and that it is in a valid email format.
Make sure that if the email fails any validation that the incorrect value is displayed, and that the user is asked to provide the email address again.
Verify that answers have been provided to each question. If an answer is missing, reprompt the user and save the answer.
Make sure you delete any "dangling" answers; that is, answers that no longer have a question because
the question was deleted.
HINT: take care to make sure that you identifty the answer that corresponds to its associated question. Give some thought as to how you can do this.

When all validation is done, produce a report that shows the number of questions that were validated successfuly, the number of answers that were validated successfully, the number of questions that failed validation, and the before and after values for each (that is, the invlaid and corrected values), the number of answers that failed validation, and the before and after values for each (that is, the invlaid and corrected values). Also list the questions that were deleted."""
import csv
import shutil
try:
    answerfile = open("answers.csv","a")
    csvreader = csv.reader(answerfile)
except FileNotFoundError:
    print("Couldn't find answers.csv")
try:
    sessfile = open("sessions.csv","a")
except FileNotFoundError:
    print("Couldn't find sessions.csv")

try:
    qfile = open("questions.csv","a")
except FileNotFoundError:
    print("Couldn't find questions.csv")
answers = []
questions = []
sessions = []
# sessfile = open("sessions.csv")
qfile = open("questions.csv")
#sessfile = open("sessions.csv")
# answerfile = open("answers.csv")
#
# questions = qfile.read().splitlines()
# answers = answerfile.read().splitlines()
answers = []
questions = []
sessions = []

def openfiles():
    print("opening files")
    try:
        answerfile = open("answers.csv")
        csvreader = csv.reader(answerfile)
        return answerfile
    except FileNotFoundError:
        print("Couldn't find answers.csv")
    try:
        sessfile = open("sessions.csv")
        return sessfile
    except FileNotFoundError:
        print("Couldn't find sessions.csv")

    try:
        qfile = open("questions.csv")
        return qfile
    except FileNotFoundError:
        print("Couldn't find questions.csv")


def validateansers(ID):
    openfiles()
    answers =[]
    answerfile = open("answers.csv")
    f = open("answers.tmp","w")
    deleted = 0
    change = 0
    kept = 0
    different_student = 0
    newanswers = []
    output = []

    for line in csv.reader(answerfile, delimiter=','):
        answers.append(line)
    sortedanswers = sorted(answers, key=lambda s: s[0])
    print(sortedanswers)
    line = []
    for row in sortedanswers:
        print("row", row)
        line = row
        if row[0] != ID:
            different_student = different_student + 1
            #save the other students
            newanswers.append(line[0])
            newanswers.append(line[1])
            newanswers.append(line[2])
            csv_out = ",".join(newanswers)
            output = csv_out
            newanswers.append("\n")

            newanswers.clear()
            f.writelines(output + "\n")
            newanswers.clear()

        else:
            print(f'Your answer is: {line[2]}')
            printquestions(line[1], line[2])
            valid = True
            # print(f'Question is:  {newquestion}')
            print(f"Do you wish to Correct (C)  or Keep (K)question  {line[1]} ? (C/K) ")
            while valid:
                choice = input()
                choice = choice.upper()
                if len(choice) > 1:
                    valid = True
                    print("Invalid answer! Needs (C/D) (too long)")
                    choice = input()
                    choice = choice.upper()

                if choice.find("C") > -1 or choice.find("K") > -1:
                    valid = False

                else:
                    print(f"Invalid answer {choice.upper()}must be C/K")
                    choice = input()
                    valid = True

            if len(line[2]) < 2:
                print (f"{line[2]} too short so you need to change it!")
                printquestions(line[1], line[2])
                choice = "C"
            if choice.upper() == "C":
                change = change + 1
                print(f'Question Number: {line[1]} is {line[2]}\n')
                printquestions(line[1], line[2])
                newanswer = input("Enter a new Answer:")
                print(f"The new answer is: {newanswer}")
                print("Thanks for the correction!")
                newanswers.append(line[0])
                newanswers.append(line[1])
                newanswers.append(newanswer)
                newanswers.append("False")
                csv_out = ",".join(newanswers)
                output = csv_out
                newanswers.append("\n")
                newanswers.clear()
                f.writelines(output + "\n")
                newanswers.clear()

            else:
                found = True
                found = printquestions(line[1], line[2])
                if found:
                    printquestions(line[1], line[2])
                    print("keeping:", newanswers)
                    newanswers.append(line[0])
                    newanswers.append(line[1])
                    newanswers.append(line[2])
                    csv_out = ",".join(newanswers)
                    output = csv_out
                    f.writelines(output + "\n")
                    newanswers.clear()
                    kept = kept + 1
                else:
                    for x in sortedquestions:
                        # add logic to omit delete questions
                        if x[3] == "True":
                            print("That question was deleted, so skipping")
                            deleted = deleted +1
                newanswers.clear()

    f.close()
    # create tmp file and write new questions
    qfile.close()
    # remple question file with tmp file
    answerfile.close()
    oldfile = r'answers.tmp'
    newfile = r'answers.csv'
    shutil.copyfile(oldfile, newfile)
    print("Number of answers kept is: ", kept)
    print("Number of answers change is: ", change)
    print("Number of answers delete because question was deleted: ",deleted)
    print("Number skipped since not this student: ", different_student)
    # end



def addquestions():
    openfiles()
    print("add questions\n\n")
    #qfile = open("questions.csv")
    questions = qfile.read().splitlines()
    qfile.close()
    qfile = open("questions.csv", "a")
    ID = str(len(questions))
    runagain = True
    while runagain:
        delteflag = False
        answer = []
        ID = int(ID) + 1
        answer.append(str(ID))
        print("Enter Sequence Number: ")
        sequence = (input())
        try:
            int(sequence)
        except:
            print(f"{sequence} is not a Number")
            print("Enter Sequence Number: ")
            sequence = (input())

        answer.append(sequence)
        print("Enter Question to Ask : ")
        questionis = input()
        answer.append(questionis)
        answer.append(str(delteflag))
        print(answer)
        print("Add another question?  y/n: ")

        more = input()
        if "Y" == more.upper():
            runagain = True
        else:
            runagain = False
        csv = ",".join(answer)
        print(f"added {csv}")
        output = csv
        qfile.writelines(output + "\n")

    qfile.close()
    listquestions()


# end

def deletequestions():
    openfiles()
    listquestions()
    print("Do you want to delete questions (y/n):")
    willdelete = input()
    if "Y" == willdelete.upper():

        import csv
        import shutil
        f = open('questions.tmp', 'w', newline='\n')
        write = csv.writer(f)
        listquestions()
        qfile = open("questions.csv")
        delq = input()
        csvreader = csv.reader(qfile)
        # questions= qfile.read().splitlines()
        print("What question do you want to delete (number)? :")
        delq = input()
        csvreader = csv.reader(qfile)

        # Copy the old file to .tmp
        # delete a question then move .tmp to .csv

        for row in csvreader:
            # print(row)
            if row[1] == delq:
                row[3] = "True"
                print(row)

            write.writerows([row])

        qfile.close()
        f.close()
        oldfile = r'questions.tmp'
        newfile = r'questions.csv'
        shutil.copyfile(oldfile, newfile)
    else:
        print("See you, bye!")


# end


def picksessions(ID):  # register for classes
        qfile = open("sessions.txt")
        sessions = qfile.read().splitlines()
        # output sessions chosen to answers.txt
        answerfile = open("sessions.csv", "a")
        print("Select which of the following sessions you wish to attend – enter y or n:")
        choice = []
        for x in sessions:

            print(x)
            n = 1
            inp = input()
            if inp.upper() == "Y":
                choice.append(ID)
                choice.append(x)
                csv_out = ",".join(choice)
                output = csv_out
                answerfile.writelines(output + "\n")
                print(f"you have chosen:{choice[1]}")
            choice.clear()
        output = csv_out
        answerfile.writelines(output + "\n")
        answerfile.close()
# end

def checkemail(email):
    import re
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    # pass the regular expression
    # and the string into the fullmatch() method
    if (re.fullmatch(regex, email)):
        print("Valid Email")
        return True
    else:
        print("Invalid Email")
        return False


# end

def whowhat(ID):  # who are you and what conference
    import csv
    name = ID
    openfiles()
    answerfile = open("answers.csv","a")
    csvreader = csv.reader(answerfile)
    qfile = open("questions.csv")
    # questions = qfile.read().splitlines()
    # answers = answerfile.read().splitlines()
    sessfile = open("sessions.csv")
    answers = []
    questions = []
    sessions = []

    qfile = open("questions.csv")
    sessfile = open("sessions.csv")
    import re  # regex
    # Read questions from questions.txt and output input to answers.txt
    questions = []
    listquestions()
    print("\n"*2)
     # answerfile = open("answers.csv","a")

    csvreader = csv.reader(answerfile)
    qfile = open("questions.csv")
    # questions = qfile.read().splitlines()
    # answers = answerfile.read().splitlines()
    sessfile = open("sessions.csv")
    answers = []
    questions = []
    sessions = []

    qfile = open("questions.csv")
    sessfile = open("sessions.csv")

    #answerfile = open("answers.csv", "a")
    for row in csv.reader(qfile, delimiter=','):
        questions.append(row)
    sortedquestions = sorted(questions, key=lambda s: int(s[1]))
    answer = []
    for x in sortedquestions:
        # add logic to omit delete questions
        if x[3] == "False":
            print(f'Question: {x[2]} ?')
            line = input()

            if x[2].find("Email") > 0:
                valid = False
                while not valid:
                    print(line,checkemail(line) )
                    if checkemail(line):
                        valid = True
                        print(line)
                    else:
                        valid = False
                        print(f"Invalid input for email!,{line}")
                        line = input(x[2])
                        line = input()

            print(f'{x[2]} is {line}')
            answer.append(ID)
            answer.append(x[0])
            answer.append(line)
            csv_out = ",".join(answer)
            print(f"added {answer[2]}")
            output = csv_out
            answerfile.writelines(output + "\n")
            answer.clear()

    answerfile.close()
    answerfile = open("answers.csv")
    picksessions(ID)


# end

def printsessions():

    count = 0
    answers = []
    sessions = []
    sessfile = open("sessions.csv")
    answerfile = open("answers.csv")
    for row in csv.reader(sessfile, delimiter=','):
        sessions.append(row)
    sortedsessions = sorted(sessions, key=lambda s: s[0])
    for line in csv.reader(answerfile, delimiter=','):
        answers.append(line)
    sortedsessions = sorted(sessions, key=lambda s: s[0])
    for i in range(len(sortedsessions)):
        line = sortedsessions[i]
        n = i + 1
        name = line[0]
        if n != len(sortedsessions):
            nextline = sortedsessions[n]
        if count == 0:
            print("Registrant: \n", name)
            count = count + 1
            # printsessions(name)

        print(f'\t\t{line[1]}')
        # printsessions(name)

        if str(line[0]) != str(nextline[0]):
            name = nextline[0]
            print("Registrant: \n", name)
#end

def printquestions(number, answer):
    # print(number,answer)
    qfile = open("questions.csv")
    for row in csv.reader(qfile, delimiter=','):
        questions.append(row)
    sortedquestions = sorted(questions, key=lambda s: int(s[1]))

    for x in sortedquestions:
        # print(x[3],answer)
        if x[0] == number:
            if x[3] == "False":
                print(f'\t\t {x[2]} is {answer}')
                return True
            else:
                return False
def search():
    answerfile = open("answers.csv")
    for line in csv.reader(answerfile, delimiter=','):
        answers.append(line)
    sortedanswers = sorted(answers, key=lambda s: s[0])
    count = 0
    for i in range(len(sortedanswers)):
        line = sortedanswers[i]
        n = i + 1
        name = line[0]
        if n != len(sortedanswers):
            nextline = sortedanswers[n]
        if count == 0:
            print("Registrant: \n", name)
            count = count+1
            #printsessions(name)

        printquestions(line[1], line[2])
        #printsessions(name)

        if str(line[0]) != str(nextline[0]):
            name = nextline[0]
            print("-"*80)
            print("Registrant: \n", name)

    print("-" * 40, "Sessions", "-" * 40)
    printsessions()
#end
    

def check_question(ques):
    print(f"question is {ques} length is {len(ques)}")
    if len(ques) > 10 and len(ques) < 30:
        q = ques
        print("question is", q)

    if len(ques) < 10:
        print(f"ERROR: Length of {ques} is not between 10 and 30 in length, So Enter a new question:")
        q = input("Enter a new question Length between 10 and 30 in length:")
    elif len(ques) > 30:
        while True:
            q = input("Enter a new question Length between 10 and 30 in length:")
            if len(q) < 10:
                q = input("Enter a new question Length between 10 and 30 in length:")
                print("Thanks for the correction!")
                print(f"{q} length is {len(q)}")
            elif len(q) > 30:
                print(f"{q} length is {len(q)}")
                q = input("Enter a new question Length between 10 and 30 in length:")
            else:
                ques = q
                break

    return q
#end

def validate_question():
    #name = ID
    import csv
    print("Let's review questions")
    # Read questions from questions.txt and output input to answers.txt
    questions = []
    listquestions()
    qfile = open("questions.csv")

    # Builf list of questions file file
    for row in csv.reader(qfile, delimiter=','):
        questions.append(row)
    # sort questions
    sortedquestions = sorted(questions, key=lambda s: int(s[1]))
    listquestions()
    newquestions = []
    f = open('questions.tmp', 'w')  # Clear temp file

    write = csv.writer(f)
    valid = True
    for line in sortedquestions:
        print(f'\nQuestion Number: {line[1]} is {line[2]}')
        # print(f'Question is:  {newquestion}')
        print(f"Do you wish to Correct (C) or Delete(D), or Keep (K)question  {line[1]} ? (C/D/K) ")
        while valid:
            choice = input()
            choice = choice.upper()
            if len(choice) > 1:
                valid = True
                print("Invalid answer! Needs (C/D/K) (too long)")
                choice = input()
                choice = choice.upper()

            if choice.find("C") > -1 or choice.find("D") > -1 or choice.find("K") > -1:
                valid = False

            else:
                print(f"Invalid answer {choice.upper()}must be C/D/K")
                choice = input()
                valid = True
        valid = True
        if choice.upper() == "C":
            print(f'Question Number: {line[1]} is {line[2]}\n')
            newquestion = check_question(input("Enter a new question:"))
            print(f"The new question is: {newquestion}")
            print("Thanks for the correction!")
            newquestions.append(line[0])
            newquestions.append(line[1])
            newquestions.append(newquestion)
            newquestions.append("False")
            csv_out = ",".join(newquestions)
            output = csv_out
            f.writelines(output + "\n")
            newquestions.clear()

        elif choice.upper() == "D":
            print(f'Question Number: {line[1]} is {line[2]}\n')
            print(f"Are you sure you want to delete? (y/n):")

            yn = input()
            yn = yn.upper
            if yn == "Y":
                newquestions.append(line[0])
                newquestions.append(line[1])
                newquestions.append(line[2])
                newquestions.append("True")
                csv_out = ",".join(newquestions)
                output = csv_out
                f.writelines(output + "\n")
                newquestions.clear()

        else:

            newquestion = check_question(line[2])
            print("keeping:", newquestion)
            newquestions.append(line[0])
            newquestions.append(line[1])
            newquestions.append(newquestion)
            newquestions.append("False")
            csv_out = ",".join(newquestions)
            output = csv_out
            f.writelines(output + "\n")
            newquestions.clear()

    f.close()
    # create tmp file and write new questions
    qfile.close()
    # remple question file with tmp file
    oldfile = r'questions.tmp'
    newfile = r'questions.csv'
    shutil.copyfile(oldfile, newfile)
#end


def check_question(ques):
    print(f"question is {ques} length is {len(ques)}")
    if len(ques) > 10 and len(ques) < 30:
        q = ques
        print("question is", q)

    if len(ques) < 10:
        print(f"ERROR: Length of {ques} is not between 10 and 30 in length, So Enter a new question:")
        q = input("Enter a new question Length between 10 and 30 in length:")
    elif len(ques) > 30:
        while True:
            q = input("Enter a new question Length between 10 and 30 in length:")
            if len(q) < 10:
                q = input("Enter a new question Length between 10 and 30 in length:")
                print("Thanks for the correction!")
                print(f"{q} length is {len(q)}")
            elif len(q) > 30:
                print(f"{q} length is {len(q)}")
                q = input("Enter a new question Length between 10 and 30 in length:")
            else:
                ques = q
                break

    return q
#end



def listquestions():
    qfile = open("questions.csv")
    questions = qfile.read().splitlines()
    print(f"the questions are\n")
    for line in questions:
        print(line)
    qfile.close()
    questions = []
    # listquestions()
    qfile = open("questions.csv")

    # Builf list of questions file file
    questions.clear()
    for row in csv.reader(qfile, delimiter=','):
        questions.append(row)
    # sort questions
    sortedquestions = sorted(questions, key=lambda s: int(s[1]))
    print("printing questions in order of sequence")
    for row in sortedquestions:
        if row[3] == "True":
            print(f'Question: {row[1]} is {row[2]} has been delted')
        else:
            print(f'Question: {row[1]} is {row[2]} ')
#end

if __name__ == '__main__':

    sortedquestions = sorted(questions, key=lambda s: int(s[1]))
    sortedanswers = sorted(answers, key=lambda s: int(s[1]))
    sortedsessions = sorted(sessions, key=lambda s: s[0])


    do = 0
    try:
        while True:
            print(">" * 20, "(1) Press 1 to list questions")  # listquestions()
            print(">" * 20, "(2) Press 2 to Delete questions")  # deletequestions()
            print(">" * 20, "(3) Press 3 to Review questions")  # validate_question()
            print(">" * 20, "(4) Press 4 to Print answers for all Students")  # search()
            print(">" * 20, "(5) Press 5 to Start Interview Registrant(s)")  # whowhat()
            do = input("What would you like to do? (1 - 5: ")
            try:
                do = int(do)  # convert to interger
                if do not in range(1, 7):
                    print(f'You chose {do}')
                    raise ValueError
            except ValueError:
                print("Input must be an integer between 1 and 5, try again. or Q for quit:")
                print(f'You chose {do}')
                xit = input("Do you want to Exit (y/n: ")
                if xit.upper() == 'Y':
                    exit()
                else:
                    continue

            if do == 1:
                listquestions()
            elif do == 2:
                deletequestions()
            elif do == 3:
                validate_question()
            elif do == 4:
                print("printing report")
                search()
            elif do == 5:
                while True:
                    StudentID = input("what is your name: ")
                    whowhat(StudentID)
                    validateansers(StudentID)
                    picksessions(StudentID)
                    #4validate_question(StudentID)
                    done = input("Are done, quit y/n?")
                    if done.upper() == "Y":
                        break


            else:
                xit = input("Do you want to Exit (y/n: ")
                if xit.upper() == 'Y':
                    exit()
                else:
                    continue

    except KeyboardInterrupt:
        xit = input("Do you want to Exit (y/n: ")
        if xit.upper() == 'Y':
            exit()


