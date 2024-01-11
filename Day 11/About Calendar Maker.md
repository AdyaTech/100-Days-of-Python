# Introduction
Dates and calendars are a tricky topic in programming because there are so many different rules for determining the number of days in a month, which years are leap years, and which day of the week a particular date falls on. Fortunately, Python’s datetime module handles these details for you. This program focuses on generating the multiline string for the monthly calendar page 

# How Does the Calendar Maker Work?
This program generates printable text files of monthly calendars for the month and year you enter. 
Note that the getCalendarFor() function returns a giant multiline string of the calendar for the given month and year. In this function, the calText variable stores this string, which adds the lines, spaces and dates to it. 

To track the date, the currentDate variable holds a datetime.date() object, which gets set to the next or previous date by adding or subtracting datetime.timedelta() objects.

# What did we learn?
Calendar Maker helps us to understand about:

1. Functions
2. Objects

