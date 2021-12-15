#!/usr/bin/env python3
""" Assignment 6
Steven Michalove
Employee record:
    Employee ID "string or int"
    Name
    Address
    Social Security Number
    Date of Birth "%m-%d-%Y"
    Job Title
    Start Date "%m-%d-%Y"
    End Date "%m-%d-%Y"
    date of last review "%m-%d-%Y"
    date left is "%m-%d-%Y" or employed


"""
import time, sys
import csv
import shutil
from datetime import datetime
from datetime import timedelta
from datetime import date
from tabulate import tabulate
import operator
import os
import random
import pytest
from faker import Faker
fake = Faker(['en-US', 'en_US', 'en_US', 'en-US'])




# used for testing


def test_randomedates():
    import random
    from datetime import datetime, timedelta

    min_year = 1980
    max_year = datetime.now().year

    start = datetime(min_year, 1, 1, 00, 00, 00)
    years = max_year - min_year + 1
    end = start + timedelta(days=365 * years)

    for i in range(100):
        random_date = start + (end - start) * random.random()
        random_date.strftime("%m-%d-%Y")
        date = random_date.strftime("%m-%d-%Y")

        print(random_date.strftime("%m-%d-%Y"), checkdate(date))
        assert checkdate(date) == True


def test_ssn():
    Faker.seed(0)
    for _ in range(5):
        ssn = fake.ssn()
        assert checkssn(ssn) == True

#end tests


def checkemail(email):
    import re
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    # pass the regular expression
    # and the string into the fullmatch() method
    if (re.fullmatch(regex, email)):
        return True
    else:
        return False


#^(0[1-9]|[12][0-9]|3[01])[- /.](0[1-9]|1[012])[- /.](19|20)\d\d$

def checkID(ID,sortedemployees):

    for row in sortedemployees:
         if row[0].find(ID) == 0:
            print(ID," Employee ID is not unique" )
            return False

    return True


def checkdate(date):
    import re
    regex = r'^(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])-(19|20)\d\d$'
    # pass the regular expression
    # and the string into the fullmatch() method
    if re.fullmatch(regex, str(date)):
        return True
    else:
        return False
    try:
        datetime.strptime(date, "%m-%d-%Y")
    except ValueError:
        return False
        raise ValueError("Incorrect data format, should be %m-%d-%Y")

def checkssn(ssn):
    import re
    regex = r'^(?!(000|666|9))\d{3}-(?!00)\d{2}-(?!0000)\d{4}$'
    # pass the regular expression
    # and the string into the fullmatch() method
    if (re.fullmatch(regex, ssn)):

        return True
    else:

        return False

def Read_csv():
    global employees
    employees=[]
    global employeefile
    count = 0
    try:

        with open("employees.csv", mode='r') as employeefile:

            count = 0
            for line in csv.reader(employeefile, delimiter=','):
                employees.append(line)
                count = count + 1
            employeefile.close()
            print(f"Reading employees.csv in {os.getcwd()} lines counted {count}")
            return employees


    except FileNotFoundError:
        print("ERROR: Couldn't find employees.csv")
        print(f"Current path is: {os.getcwd()}")
    finally:
        if count == 0:
            print(f"Reading employees.csv in {os.getcwd()} lines counted {count}")



def edit_employees():
    oldfile = r'employees.csv'
    newfile = r'employees.old'
    shutil.copyfile(oldfile, newfile)  # make a copy before any changes
    list_employees()
    f = open("employees.tmp", "w")
    newrecord =[]
    employeesnoheader = []
    numemployees = 0
    length = len(employees)
    print("NOTE: This is case sensitive and must be an exact match, if not found returns to main menu!")
    fname = input("First Name of employee: ")
    mi = input("Middel Initial: ")
    lname = input("Last Name: ")

    for field in header: # rebuild header
        newrecord.append(field)
        csv_out = ",".join(newrecord)
        output = csv_out
    newrecord.append("\n")
    f.writelines(output + "\n")

    newrecord.clear()
    print("CAUTION: Changing an employee record cannot be undone")
    for x in range(length):

        # print(x,employees[x])
        if x != 0:
            employeesnoheader.append(employees[x])
            numemployees = numemployees + 1
    sortedemployees = sorted(employeesnoheader, key=operator.itemgetter(0))

    for record in sortedemployees:

        if record[1] == fname and record[2] == mi and record[3] == lname:
            print("employee found!")

            index = 0
            for field in header:
                print(header[index].upper(),"  is currently: ",record[index])
                #print(field)
                prompt = "New value for or ENTER to keep old value "+ header[index].upper()+": "
                new = input(prompt)

                if len(new) == 0:
                    print(f"You pressed Enter so keeping {record[index]}")
                    new = record[index]

                if header[index].upper().find("MAIL") > 0:
                    valid = False
                    while not valid:
                        # print(checkemail(new))
                        if checkemail(new):
                            valid = True

                        else:
                            valid = False
                            print(f"ERROR:Invalid input ,{prompt} :")
                            new = input(prompt)
                if header[index].upper().find("SSN") > 0:
                    valid = False
                    while not valid:
                        if checkssn(new):
                            valid = True

                        else:
                            valid = False
                            print(f"ERROR:Invalid input for !,{prompt} :")
                            new = input(prompt)
                if header[index].upper().find("DATE") > 0 and prompt.upper().find("LEFT") == 0:
                    valid = False
                    if checkdate(new):
                        valid = True

                    else:
                        valid = False
                    print(f"ERROR: Invalid input for !,{prompt} mm-dd-yyyy :")
                    new = input(prompt)

                newrecord.append(new)
                index = index+1
            csv_out = ",".join(newrecord)
            output = csv_out
            newrecord.append("\n")
            f.writelines(output + "\n")
            newrecord.clear()


        else: # save unchanged record
            newrecord.append(record)
            csv_out = ",".join(record)
            output = csv_out
            newrecord.append("\n")
            f.writelines(output + "\n")

            newrecord.clear()
    f.close()
    oldfile = r'employees.tmp'
    newfile = r'employees.csv'
    employeefile.close()
    shutil.copyfile(oldfile, newfile)


    print("I did not write this yet")

def list_employee(employee):

    try:
        print(tabulate([employee], headers=header,
                       numalign="right", floatfmt=".2f"))
    except ValueError:
        print ("Employee record currupted!")
        raise ValueError("Incorrect data format, should be %m-%d-%Y")

def add_employee():
    oldfile = r'employees.csv'
    newfile = r'employees.old'
    shutil.copyfile(oldfile, newfile)  # make a copy before any changes

    f = open("employees.tmp", "w")
    newrecord = []
    employeesnoheader = []
    numemployees = 0
    length = len(employees)
    index = 0
    print("CAUTION: Adding an employee record cannot be undone")
    for field in header: # rebuild header
        newrecord.append(field)
        csv_out = ",".join(newrecord)
        output = csv_out
    newrecord.append("\n")
    f.writelines(output + "\n")
    newrecord.clear()
    for x in range(length):

        # print(x,employees[x])
        if x != 0:
            employeesnoheader.append(employees[x])
            numemployees = numemployees + 1
    sortedemployees = sorted(employeesnoheader, key=operator.itemgetter(0))
    recordnum = 0
    a = input("Do you want to add a new user (y/n): ")
    if a.upper() == "Y":
        print("OK, Let's add a new employee!")
        #print(header)
        for field in header:
            # print(field)
            prompt = "Enter " + header[index] + ": "
            new = input(prompt)
            if prompt.upper().find("ID") > 0:
                valid = False
                while not valid:
                    #print(sortedemployees)
                    if checkID(new,sortedemployees):
                        valid = True

                    else:
                        valid = False
                        print(f"ERROR:Invalid input ,{prompt} :")
                        new = input(prompt)


            if prompt.upper().find("MAIL") > 0:
                valid = False
                while not valid:
                    #print(checkemail(new))
                    if checkemail(new):
                        valid = True

                    else:
                        valid = False
                        print(f"ERROR:Invalid input ,{prompt} :")
                        new = input(prompt)
            if prompt.upper().find("SSN") > 0:
                valid = False
                while not valid:
                    if checkssn(new):
                        valid = True

                    else:
                        valid = False
                        print(f"ERROR:Invalid input for !,{prompt} :")
                        new = input(prompt)
            if prompt.upper().find("DATE") > 0 and prompt.upper().find("LEFT") == 0:
                valid = False
                if checkdate(new):
                    valid = True

                else:
                    valid = False
                print(f"ERROR: Invalid input for !,{prompt} mm-dd-yyyy :")
                new = input(prompt)
                if prompt.upper().find("LEFT") > 0:
                    new = "Employed"

            index = index + 1
            newrecord.append(new)
            csv_out = ",".join(newrecord)
        output = csv_out
        newrecord.append("\n")
        f.writelines(output + "\n")
        newrecord.clear()

    for record in sortedemployees: # save unchanged record
            newrecord.append(record)
            csv_out = ",".join(record)
            output = csv_out
            newrecord.append("\n")
            f.writelines(output + "\n")
            newrecord.clear()

    f.close()
    oldfile = r'employees.tmp'
    newfile = r'employees.csv'
    employeefile.close()
    shutil.copyfile(oldfile, newfile)


def list_employees():

    try:
        employeesnoheader =[]
        numemployees = 0
        length = len(employees)
        for x in range(length):

            #print(x,employees[x])
            if x != 0:
                employeesnoheader.append(employees[x])
                numemployees = numemployees+1

        sortedemployees = sorted(employeesnoheader, key=operator.itemgetter(0))

        print(tabulate(sortedemployees, headers=header, tablefmt="presto",
                       numalign="right", floatfmt=".2f"))
        print("Number of employees:",numemployees)
    except ValueError:
        print ("Employee record currupted!")
        raise ValueError("Incorrect data format, should be %m-%d-%Y")

def current_employees():
    try:
        employeesnoheader =[]

        currentemployees = []
        length = len(employees)
        employeesnoheader = []
        length = len(employees)
        for x in range(length):

            # print(x,employees[x])
            if x != 0:
                employeesnoheader.append(employees[x])
        for employee in employeesnoheader:
            if employee[15] == "Employed":
                currentemployees.append(employee)


        sortedemployees = sorted(currentemployees, key=operator.itemgetter(0))
        print(tabulate(sortedemployees, headers=header, tablefmt="presto",
                       numalign="right", floatfmt=".2f"))
        print("Number of Current employees:",len(currentemployees))
    except ValueError:
        print ("Employee record currupted!")
        raise ValueError("Incorrect data format, should be %m-%d-%Y")

def list_justleft():
    try:
        dateformat = "%m-%d-%Y"
        employeesnoheader = []

        justleft = []
        length = len(employees)
        for x in range(length):

            #print(x,employees[x])
            if x != 0:
                employeesnoheader.append(employees[x])
        for employee in employeesnoheader:
            if employee[15] != "Employed":

                today = date.today().strftime(dateformat)
                today = datetime.strptime(today, dateformat).date()
                left =  datetime.strptime(employee[15], dateformat).date()
                delta = (today-left)
                #print(delta.days)
                if delta.days < 32:
                    justleft.append(employee)


        sortedemployees = sorted(justleft, key=operator.itemgetter(15))
        print(tabulate(sortedemployees, headers=header, tablefmt="presto",
                       numalign="right", floatfmt=".2f"))
        print("Number of employees who just left: ", len(sortedemployees))
    except ValueError:
        print ("Employee record currupted!")
        raise ValueError("Incorrect data format, should be %m-%d-%Y")


def review_reminders():
    try:
        dateformat = "%m-%d-%Y"
        employeesnoheader = []
        currentemployees =[]
        today = date.today().strftime(dateformat)
        today = datetime.strptime(today, dateformat).date()

        length = len(employees)
        for x in range(length):

            # print(x,employees[x])
            if x != 0:
                employeesnoheader.append(employees[x])
        sortedemployees = sorted(employeesnoheader, key=operator.itemgetter(14))
        for employee in sortedemployees:
            if employee[15] == "Employed":
                currentemployees.append(employee)
                lastreview = datetime.strptime(employee[14], dateformat).date()
                delta = (today - lastreview)
                reviewdue = lastreview + timedelta(days=365)
                delta = (today - lastreview)
                daysdue = (reviewdue - today)
                if daysdue.days > 365:
                    print(f"\nNext review is OVERDUE!: {reviewdue}")
                    print("*"*80)
                    list_employee(employee)
                    print("*" * 80)
                elif daysdue.days < 90:
                    print(f"\nnext review is approaching! {daysdue.days} days on {reviewdue}")
                    list_employee(employee)
    except ValueError:
        print ("Employee record currupted!")
        raise ValueError("Incorrect data format, should be %m-%d-%Y")


    sortedemployees = sorted(currentemployees, key=operator.itemgetter(0))

    sortedemployees = sorted(employeesnoheader, key=operator.itemgetter(0))





def prompt_user():
    try:


        while True:
            Read_csv()
            print(">" * 20, "(1) Press 1 to list ALL employees")
            print(">" * 20, "(2) Press 2 to list Current employees")  #
            print(">" * 20, "(3) Press 3 to list employees that just left")
            print(">" * 20, "(4) Press 4 to Print review reminders")
            print(">" * 15, "(5) Press 5 to Change employee record")
            print(">" * 15, "(6) Press 6 to Add employee record")
            do = input("What would you like to do? (1 - 6:) anything else to quit ")
            try:
                do = int(do)  # convert to int
                if do not in range(1, 7):
                    print(f'You chose {do}')
                    raise ValueError
            except ValueError:
                print("Input must be an integer between 1 and 6, try again. or Q for quit:")
                print(f'You chose {do}')
                xit = input("Do you want to Exit (y/n:) ")
                if xit.upper() == 'Y':
                    exit()
                else:
                    continue

            except KeyboardInterrupt:
                xit = input("Do you want to Exit (y/n: ")
                if xit.upper() == 'Y':
                    exit()

            if do == 1:
                list_employees()
            elif do == 2:
                current_employees()
            elif do == 3:
                list_justleft()
            elif do == 4:
                print("printing reminders")
                review_reminders()
            elif do == 5:
                edit_employees()
            elif do == 6:
                add_employee()
            else:
                xit = input("Do you want to Exit (y/n:) ")
                if xit.upper() == 'Y':
                    exit()
                else:
                    continue
    except ValueError:
        print("Input must be an integer between 1 and 5, try again. or Q for quit:")
        print(f'You chose {do}')
        xit = input("Do you want to Exit (y/n: ")
        if xit.upper() == 'Y':
            exit()

    except KeyboardInterrupt:
        xit = input("Do you want to Exit (y/n: ")
        if xit.upper() == 'Y':
            exit()



if __name__ == '__main__':

    employees = Read_csv()
    header = employees[0]
    prompt_user()



