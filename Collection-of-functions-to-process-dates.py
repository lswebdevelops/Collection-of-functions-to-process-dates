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
    if year > datetime.MINYEAR:   

      if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        days_of_month = 31
        return days_of_month
      elif month == 2:
        days_of_month = 28
        return days_of_month

      elif month == 4 or month == 6 or month == 9 or month == 11:
        days_of_month = 30
        return days_of_month

    return 0


# days_in_month(9998,1)


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
    if year > datetime.MINYEAR and year <datetime.MAXYEAR:
      if month > 0 and month <13:
        if (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12) and (day < 32 and day >0):
            
            return year,month, day
        elif(month ==2) and(day < 29 and day >0):
            year,month, day
            return year, month, day
        elif(month == 4 or month == 6 or month == 9 or month == 11) and (day < 31 and day >0):
            year,month, day
            return year, month, day
            
    
    return False 


print(is_valid_date(1999, 6, 30))

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
    return 0

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
    return 0
