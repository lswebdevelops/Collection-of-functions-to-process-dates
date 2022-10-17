
#URL> https://py3.codeskulptor.org/#user307_CuOkpWmMv25mXNJ_1.py
#     https://py3.codeskulptor.org/#user307_NN14DDcOfPLxGiW.py

"""
Project for Week 4 of "Python Programming Essentials".
Collection of functions to process dates.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""

import datetime

def days_in_month(year, month):
    """
    Inputs:
      year  - an integer between datetime.MINYEAR and datetime.MAXYEAR
              representing the year
      month - an integer between 1 and 12 representing the month

    Returns:
      The number of days in the input month.
    """
    if year >= datetime.MINYEAR:   

      if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        days_of_month = 31
        print(days_of_month)
        
      elif month == 2:
        days_of_month = 28
        print(days_of_month)
        

      elif month == 4 or month == 6 or month == 9 or month == 11:
        days_of_month = 30
        print(days_of_month)

    return 0



days_in_month(1986,1)


def is_valid_date(year, month, day):
    """
    Inputs:
      year  - an integer representing the year
      month - an integer representing the month
      day   - an integer representing the day

    Returns:
      True if year-month-day is a valid date and
      False otherwise
    """
    
    #checking if the year is valid
    if year >= datetime.MINYEAR and year <datetime.MAXYEAR:
      if month > 0 and month <13:
        if (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12) and (day < 32 and day >0):
            
            return True
        elif(month ==2) and(day < 29 and day >0):
            year,month, day
            return True
            
        elif(month == 4 or month == 6 or month == 9 or month == 11) and (day < 31 and day >0):
            year,month, day
            return True
            
            
    
    return False 




def days_between(year1, month1, day1, year2, month2, day2):
    """
    Inputs:
      year1  - an integer representing the year of the first date
      month1 - an integer representing the month of the first date
      day1   - an integer representing the day of the first date
      year2  - an integer representing the year of the second date
      month2 - an integer representing the month of the second date
      day2   - an integer representing the day of the second date

    Returns:
      The number of days from the first date to the second date.
      Returns 0 if either date is invalid or the second date is
      before the first date.
    """
    if is_valid_date(year1, month1, day1) and is_valid_date(year2, month2, day2) != False:
      oldest_date = datetime.date(year1, month1, day1)
      newest_date = datetime.date(year2, month2, day2)
      number_of_days = newest_date - oldest_date 
      number_days = number_of_days.days
      # checks if the first date is greater than the second
      if number_days > 0:
        print("\nThe number of days between " + str(year1) + "-" + str(month1) + "-" + str(day1) + " and " + str(year2) + "-" + str(month2) + "-" + str(day2) + " is: " +  str(number_days) + ".\n")


    return 0
days_between(1985, 5, 19,2022,10,17)
days_between(2014, 5, 5, 2014, 5, 6)



def age_in_days(year, month, day):
    """
    Inputs:
      year  - an integer representing the birthday year
      month - an integer representing the birthday month
      day   - an integer representing the birthday day

    Returns:
      The age of a person with the input birthday as of today.
      Returns 0 if the input date is invalid or if the input
      date is in the future.
    """
    if is_valid_date(year, month, day) != False:
      birthday = datetime.date(year, month, day)
      today = datetime.date.today()
      number_of_days = today - birthday 
      number_days = number_of_days.days
      # checks if the first date is greater than the second
      if number_days > 0:
        print("\nYour age in days is: " + str(number_days) + " days.\n")

    return 0



age_in_days(2017, 1, 1)