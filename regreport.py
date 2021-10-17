#!/usr/bin/env python3
"""This program reads from output file from Assignment3.py  and reports/prints 
on answers from answers.txt that is a csv file that has no header of column"""
import csv
qfile=open("questions.txt")
answerfile = open("answers.txt")
questions= qfile.read().splitlines()
numofquestions=len(questions)

csvreader = csv.reader(answerfile)

rows = []
for row in csvreader:
        rows.append(row)
        StudentID=row[0]
        name=row[1]
        conf=row[2]
        org=row[3]
        email=row[4]
        food=row[5]
        sessions=row[numofquestions+1:len(row)]
        print(f'Student ID: {StudentID}\n')       
        print(f'\t{name}\n\tConfID:{conf}\n\t{org}\n\t{email}\n\tFood Preference:{food}\n')
        print(f'\tSessions:\n')
        for i in sessions:
            print(f'\t\t{i}\n' )
#print(rows)

#print(f'Name: {name}\n')