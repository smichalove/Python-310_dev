"""Assignment 7
Steven Michalove

The application you are building will capture the following information:

Name of the customer.
Package description.
Are the contents dangerous? [Y/N]
Weight (kgs).
Volume (cubic meters).
Required delivery date (month/date/year).
International destination? [Y/N]
The application will then attempt to find the best way to route the package (air / ground / ocean).

The rules it will use are as follows:

Packages can only be shipped if they weigh less than 10Kg or are smaller than 5x5x5 meters (125 cubic meters).
If the package contains dangerous goods it cannot be routed via air.
'Urgent' means a package has to be delivered in less than 3 business days.
If the package is urgent it will be routed via air, if possible.
If the package is heavy or large (towards the maximum end of the boundaries set in 1 above),
and is not urgent, it can be routed via truck (or even ocean if it is for an international destination).
Air shipments cost $10 per kilogram or $20 per cubic meter, whichever is the highest.
Truck shipments cost a flat rate of $25, or $45 if urgent.
Ocean shipments costs a flat rate of $30.
CSV HEADERS ARE
customer, weight, heigth, width, international,dangerous, method, cost
"""
import time, sys
import csv
import shutil
import pathlib
cdw = pathlib.Path.cwd()
from datetime import datetime
from datetime import timedelta
from datetime import date

import operator
import os
import random
import pytest
from tabulate import tabulate


## test cases
def test_costs():
    method =["AIR","TRUCK","URGENTTRUCK","OCEAN"]

    for m in method:
        for x in range(255):
            cost = calculatecost(m,random.randint(1,120),random.randint(1,10))
            print(cost,m)
        assert cost  != ValueError

def test_canship():
    for x in range(100):
        y = random.randint(1,15)
        z = random.randint(1,200)
        shippable = canship(y,z)
        if y < 10 and z < 125:
            print(shippable)
            assert shippable
        if y > 10 and z > 125:
            print(shippable)
            assert not shippable

def test_calc_volume():
    for x in range(100):
        volume  = calculate_volume(random.randint(1,15),random.randint(1,5),random.randint(1,25))
        print(volume)
        assert volume != ValueError





### end tests

def Read_csv():
    shipments=[]
    shipments.clear()
    global shipfile
    shipfile = "booking_quotes.csv"
    count = 0
    try:

        with open("booking_quotes.csv", mode='r') as shipfile:

            count = 0
            for line in csv.reader(shipfile, delimiter=','):
                shipments.append(line)
                count = count + 1
            shipfile.close()
            return shipments

    except FileNotFoundError:
        print("ERROR: Couldn't find booking_quotes.csv")
        print(f"Current path is: {cdw} ")
    finally:
        shipfile = "booking_quotes.csv"
        if count != 0:
            print(f"Reading {str(shipfile)} in {cdw} lines counted {count}")
    shipfile.close()


def calculate_volume(length:float, height:float, width:float):
    try:
        volume = float(length) * float(height) * float(width)
        print(f"volume is: {volume}")
        return volume
    except ValueError:
        return ValueError

def canship(weight:float, area:float):
    if weight > 10:
        print(f"{weight}kgs is higher than 10kg so this package cannot be shipped!")
        return False
    elif area > 125:
        print(f"{area}m is higher than 125 m^3 so this package cannot be shipped!")
        return False
    else:
        print("Package is eligible for shipping")
        return True

def calculatecost(method:str, volume:float, weight:float):
    try:
        print(f"Calculating cost for method is {method}, Volume {volume} and weight {weight}")
        if method == "AIR":
            costperkilo = float(weight)* 10
            costpervolume = float(volume) * 20
            if costpervolume > costperkilo:
                print(f"Cost is {costpervolume}")
                return costpervolume
            else:
                print(f'Cost is {costperkilo}')
            return costperkilo
        elif method == "URGENTTRUCK":
            print("Cost is for urgent truck is $45")
            cost = 45
            return cost
        elif method == "TRUCK":
            cost = 25
            return cost
        elif method == "OCEAN":
            cost = 30
            return cost
        else:
            print("ship method is",method)
            print(f"{method} ERROR unknown type")
            raise ValueError
    except ValueError:
        return ValueError

def printrecord(record):
    count = 0
    print("Here is the new shipping record: \n")
    for cell in header:
        print(f"{cell} {shiprecord[count]}")
        count = count+1
    input("press ENTER to continue")



def calulatemethod(urgent:bool,dangerous:bool,international:bool,area:float):
    print("urgent",urgent)
    print("dangerous ",dangerous)
    print("international ",international)
    print("area ", area)
    if area > 125:
        print("Your package is too big to ship!")
        shipmethod = "NONE"
        return shipmethod
    if urgent and not dangerous and area <125:
        print("Qualifies for Air shipment")
        cost = calculatecost("AIR", area, weight)
        print(f"Cost will be {cost} with air!")
        p =input("Do you want AIR (y/n):")


        print(f"With Air, cost id {cost}")
        if p.upper() == "Y":
            shipmethod = "AIR"
            cost = calculatecost(shipmethod, area, weight)
            print("Ship method is Air!")
            print(f"Cost will be {cost} with air!")
            return shipmethod
        elif p.upper() == "N" and not international:
            print("Qualifies for Urgent Truck")
            shipmethod = "URGENTTRUCK"
            return shipmethod
        else:
            shipmethod = "OCEAN"
            print(f"Ship method is {shipmethod}")
            return shipmethod

    elif urgent and not international:
        print("Qualifies for Urgent Truck")
        shipmethod = "URGENTTRUCK"
        return shipmethod
    elif not international and dangerous and not urgent:
        shipmethod = "TRUCK"
        print("Qualifies for Truck")
        return shipmethod
    if international and dangerous:
        print("Qualifies for OCEAN shipment")
        shipmethod = "OCEAN"
        return shipmethod
    if not urgent and not international:
        shipmethod = "TRUCK"
        print("Qualifies for Truck")
        return shipmethod



def reportshipments(shipments):

    print(tabulate(shipments, headers=header, tablefmt="presto",
                   numalign="right", floatfmt=".2f"))

if __name__ == "__main__":
    print(f"Reading shipment.csv in {os.getcwd()} ")
    shipments = Read_csv()

    f = open("shipments.tmp", "w")
    oldfile = r'booking_quotes.csv'
    newfile = r'shipments.old'
    shutil.copyfile(oldfile, newfile)
    f.close()

    newrecord = []
    shiprecord = []
    shipments = []
    shipments = Read_csv()
    header = shipments[0]
    shipmentsnoheader = []
    records = len(shipments)






    while True:
        shipments.clear()
        shipments = Read_csv()
        records = len(shipments)
        shipmentsnoheader.clear()
        for x in range(records):
            if x != 0:
                shipmentsnoheader.append(shipments[x])

        reportshipments(shipmentsnoheader)
        shiprecord.clear()
        p = input("Do you wish to ship an item (Y/N or q for exit ")
        if p.upper() == "Y":
            while True:
                try:
                    customername = input("Customer name is? ")
                    if len(customername) <1:
                        print(f"{customername} not valid!")
                        raise ValueError
                except ValueError:
                        continue
                finally:
                    shiprecord.append(customername)
                    break
        elif p.upper() == "N":
            continue
        elif p.upper() == "Q":
            exit()
        try:
            weight = input("How much does your package weigh in kgs?: ")

            if len(weight) < 1:
                print("invalid answer")
                raise ValueError
            weight = float(weight)
            if weight > 10:
                print(f"At {weight}kgs! Dang, Your package is too heavy to ship!")
                input("Press any key to continue")
                raise ValueError
                continue
        except ValueError:
            print("Input error, your weight needs to be numbers!")
            continue
        shiprecord.append(weight)
        try:
            print("Your package is not to heavy to ship, so let's gather the size!")
            length = input("Input length in meters")
            if len(length) < 1:
                print("invalid answer")
                raise ValueError
            length = float(length)
        except ValueError:
            print("Input error, your length needs to be numbers!")
            continue
        shiprecord.append(length)
        try:
            height = input("Input height in meters")
            if len(height) < 1:
                print("invalid answer")
                raise ValueError
            height = float(height)
        except ValueError:
            print("Input error, your length needs to be numbers!")
            continue

        try:
            width = input("Input width in meters")
            if len(width) < 1:
                print("invalid answer")
                raise ValueError
            width = float(width)
        except ValueError:
            print("Input error, your length needs to be numbers!")
            continue
        shiprecord.append(height)
        volume = calculate_volume(height,length,width)
        if volume > 125:
            print(f"Volume is {volume}! Oops! To big to ship!")
            input("hit any key to continue")
            continue
        else:
            shiprecord.append(volume)
        p = input("Is your package Urgent (y/n")
        if p.upper() == "Y":
            print("OK, marked urgent!")
            urgent = True
            shiprecord.append(urgent)
        else:
            urgent = False
            shiprecord.append(urgent)
        p = input("Is your package International (y/n")
        if p.upper() == "Y":
            print("OK, marked International!")
            international = True
            shiprecord.append(international)
        else:
            international = False
            shiprecord.append(international)
        print(f"A hazardous material or dangerous good is defined as a substance or material that \n the Secretary of "
            f"Transportation has determined is capable of posing an unreasonable risk to health, safety, and property \n"
            f" when transported in commerce, and has designated as hazardous under section 5103 of Federal hazardous \n"
            f"materials transportation law ")
        p = input("Is your package Dangerous (y/n")
        if p.upper() == "Y":
            print("OK, marked dangerous!")
            dangerous = True
            shiprecord.append(dangerous)
        else:
            dangerous = False
            shiprecord.append(dangerous)
        method = calulatemethod(urgent,dangerous,international,volume)

        shiprecord.append(method)
        print(f"The best way to ship is by {method}")
        try:
            cost = calculatecost(method,volume, weight)
        except ValueError:
            print("unable to calculate cost!")
            continue
        shiprecord.append(cost)
        print(shiprecord)
        printrecord(shiprecord)
        with open('shipments.tmp', 'w', newline='') as tmp:
            write = csv.writer(tmp)
            write.writerow(header)
            write.writerow(shiprecord)  # new shipment record
            write.writerows(shipmentsnoheader) # Previous shipments
            print("writing file")
        f.close()

        print(f"writing to file in {os.getcwd()} ")
        oldfile = r'shipments.tmp'
        newfile = r'booking_quotes.csv'
        shutil.copyfile(oldfile, newfile)
        shipments = Read_csv()
        shipmentsnoheader.clear()
        continue
