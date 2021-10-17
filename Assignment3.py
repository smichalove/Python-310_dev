#!/usr/bin/env python3
'''
Our app is now quite useful. We can manage and amend the questions easily. 
But now we need to be able to add features to save and load data. 
First we will deal with the questions.

Each question that we need to get answered will be stored in a file, 
and reloaded from the file when the program starts running.

We will build a new program to prompt for the questions, 
and store them in the file. Later, we will work on having the 
automated interviewer program read the questions from this file.

The file will store the question, a question id number that identifies 
the question throughout its life (creation to delete), 
a sequence number, indicating the order in which each question should
 be asked, and finally a flag that indicates if the questions is no 
longer to be used (a “deleted” flag which is True if the question 
is not to be used. For now that will default to False).

The file will look something like this:

questionid, sequencenumber, question,deletedflag

10,1,”What is your email”, False

Write the new program to capture the questions.

Now we will allow Automated Interviewer to load the questions from the question file so it can display and use them. Automated Interviewer must not assume the questions are in the correct sequence, so it needs to sort them before starting to use them. Run Automated Interviewer and make sure it works. Change the order of the questions, delete some and add some and check it all works as intended.

Finally we are going to modify Automated Interviewer to store the answers to the questions, and then write a new program print them.

The file will look something like this:

questionid,nameofpersoninterviewed,answer

2,”Andy”,”akmiles@uw.edu”

When the file is stored successfully create a new py file that 
will create a clearly formatted report that shows the name of the 
interviewee, and each question followed by its respective answe'''


def sessions(): # register for classes
    #output sessions chosen to answers.txt
    answerfile = open("answers.txt", "a")
    print("Select which of the following sessions you wish to attend – enter y or n:")
    sessions = ["Python for beginners",
                "Database development with Python",
                "Python for data science",
                "Advanced Python for application developers"]
    choice=[]
    for x in sessions:
        print(x)       
        n=1
        inp=input()
        if inp == "y":
            choice.append(x)

    print(f"you have chosen:{choice}")
    print(choice)
    csv =  ",".join(choice)
    #print(type(csv))
    print(csv) 
    output=csv
    answerfile.write(output + "\n")  
    answerfile.close()
            


def whowhat(ID): #who are you and what conference
    # Read questions from questions.txt and output input to answers.txt
    qfile=open("questions.txt")
    answerfile = open("answers.txt", "a")
    #questions = [x for x in qfile.readlines() if x != "\n"]
    questions= qfile.read().splitlines()

    print ("the questions are",questions)
    answer=[str(ID)]
    for x in questions:
        print (x)
        line=input()
        valid=True
        if x.find("email") > 0:
            while line.find("@") == -1:
                print("Invalid input for email!")
                line=input()         
        answer.append(line)

    #answerfile.write(answer)
    print ("number of anseers:",len(answer))  
    n=0
    
    print(answer)
    
    csv =  ",".join(answer)
    print(type(csv))
    print(csv) 
    output=csv+","
    answerfile.write(output)  
    answerfile.close()
    #print(questions,len(questions))
    




if __name__ == '__main__':
    print("running assigment3")
    done = "n"
    answerfile= open("answers.txt")
    numrows = answerfile.read().splitlines()
    StudentID=len(numrows)+1 ## increment student id from number of rows
    answerfile.close()
    try:
        while not done == "y":
            whowhat(StudentID)  
            sessions()
            StudentID=StudentID+1
            done=input("Are done, quit y/n?")

    except KeyboardInterrupt:   
        answerfile= open("answers.txt")
        answerfile.close()
        print("Thank you for registering!")

    finally:
        answerfile= open("answers.txt")
        answerfile.close()
        print("Thank you for registering!")