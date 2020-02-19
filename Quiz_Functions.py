import pandas as pn 
import csv
## Converting csv file contents into a list
def data_parser(data_csv_file):

    ## counters
    day_dict = {}
    employee_dict = {}

    ## store the header and discard it so we only parse through actual data
    header_row = next(data_csv_file) 

    ## Populating empty day dictionary with dates and number of shifts
    for index,day in enumerate(header_row):
        if index != 0:
            day_dict.update({day : 0}) ## appending the day and the number of shifts (default 0)

    ## Populating empty employee dictionary with names and number of shifts
    for row in data_csv_file:
        employee_dict.update({row[0] : 0}) ## row[0] = name and number of shifts (default 0)


    ## building data frame
    

    ## make sure to append total at bottom

    return InitialDate_df

'''
## Going through initial data frame and finding optimal schedule
def Get_Schedule(InitialDate_df):
    ## keep track of names and dates (their shift constraints)

    return OptimalSchedule_df

'''