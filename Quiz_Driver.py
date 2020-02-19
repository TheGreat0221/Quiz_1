'''
## Problem
    13 days at museum require 3 shifts a day = 39 shifts
    20 people who work 2 shifts (max) = 40 shifts
    Each person has given preferenecs on days they'd like to work (1-13, 1 being most-desired)
    Create a schedule with names and days working via and report to an excel spreadsheet

## Constraints
    Must use panda dataframes 
    no worker can work more than 2 days

## Process
    load data from excel into a dataframe || function returning a dataframe with total at bottom
    take dataframe and iterate through it, starting with hardest day to fill first || function returning a dataframe of names and days working
        formula to use in iteration:
            keep track of shifts per day (once it reaches three, ignore) --> dictionary perhaps? key: date, value: # shifts
            keep track of shifts per person (once it reaches 2, ignore) --> dictionary perhaps? key: name, value: # shifts
            start with hardest days; pick 3 lowest numbers in the day (ignore ties)
            append corresponding dictionaries
        return a dataframe with the names as row headers and the dates as column headers with an x at their respective shifts
            
    display finished dataframe to the screen and save results into an excel spreadsheet
'''

## Driver
import Quiz_Functions as fn 
import csv
import pandas as pn

# import file
data_open_file = open("Holiday Schedule Ranking 2019.csv", "r")
data_csv_file = csv.reader(data_open_file, delimiter=",")

# Send data_csv_file to ____function for parsing (we want to convert a list to a dataframe)
InitialDate_df = fn.data_parser(data_csv_file)

'''
# Send dataframe to ___function for parsing (figure out optimal shift schedule)
OptimalSchedule_df = Get_Schedule(InitialDate_df)

# Reporting Results


## End
'''