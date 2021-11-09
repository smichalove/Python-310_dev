#!/usr/bin/env python3
"""
Assignment 04
Steven Michalove
Now to the answers file:

Add code to make sure that the email address is provided and that it is in a valid email format.
Make sure that if the email fails any validation that the incorrect value is displayed, and that the
user is asked to provide the email address again.
Verify that answers have been provided to each question. If an answer is missing, reprompt the user
and save the answer.
Make sure you delete any "dangling" answers; that is, answers that no longer have a question because
the question was deleted.
HINT: take care to make sure that you identifty the answer that corresponds to its associated
question. Give some thought as to how you can do this.

When all validation is done, produce a report that shows the number of questions that were validated
successfuly, the number of answers that were validated successfully,
 the number of questions that failed validation, and the before and after values for each (that is,
 the invlaid and corrected values),
the number of answers that failed validation, and the before and after values for each (that is, the inv

"""
import csv

def listquestions():
    qfile=open("questions.csv")
    #questions = qfile.read().splitlines()
    questionslist= csv.reader(qfile)
    print(f"the questions are\n")
    for line in questionslist:
        print(line)
    qfile.close()

def sessions(ID): # register for classes
    qfile = open("sessions.txt")
    sessions = qfile.read().splitlines()
    #output sessions chosen to answers.txt
    answerfile = open("sessions.csv", "a")
    print("Select which of the following sessions you wish to attend – enter y or n:")
    choice = []
    for x in sessions:

        print(x)
        n=1
        inp=input()
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
            


def whowhat(ID): #who are you and what conference
    import csv
    # Read questions from questions.txt and output input to answers.txt
    questions = []
    answers = []
    #listquestions()
    qfile = open("questions.csv")
    answerfile = open("answers.csv", "a")
    for row in csv.reader(qfile, delimiter=','):
        questions.append(row)
    sortedquestions = sorted(questions, key=lambda s: s[1])
    answer = []
    for x in sortedquestions:
        # add logic to omit delete questions
        if x[3] == "False":
            print (f'Question: {x[2]} ?')
            line = input()
            if x[2].find("Email") > 0:
                while line.find("@") == -1:
                    print("Invalid input for email!")
                    line = input()
            print(f'{x[2]} is:  { line}')
            answers.append(ID)
            s.append(x[0])
            answers.append(line)
            csv_out = ",".join(answer)
            print(f"added {answer[2]}")
            output = csv_out
            answerfile.writelines(output + "\n")
            answers.clear()
    answerfile.close()



    




if __name__ == '__main__':

    print("running assigment3")
    done = "n"
    try:
        while True:
            StudentID = input("what is your name: ")
            whowhat(StudentID)
            sessions(StudentID)
            done = input("Are done, quit y/n?")
            if done.upper() == "Y":
                break

    except KeyboardInterrupt:
        answerfile= open("answers.txt")
        answerfile.close()
        print("Thank you for registering!")

    finally:
        answerfile= open("answers.txt")
        answerfile.close()
        print("Thank you for registering!")