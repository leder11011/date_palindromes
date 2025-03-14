
"""
Check for current date and given date if it's:
- your birthday
- fourth of may
- 14. of march
- fourth of july
- a german date format palindrome date
- third of October
"""

from palindrome2 import palindrome
from datetime import datetime

from myError import MyError

# import sys
# print(sys.path)

'''
is today same as given date?
'''
def check_given_date_today(current_dateTime, given_dateTime):
    if current_dateTime.day == given_dateTime.day and current_dateTime.month == given_dateTime.month and current_dateTime.year == given_dateTime.year:
        return True
    else: return False

'''
is today your birthday?
'''
def check_birthday(current_dateTime, birthdate_datetime):
    if current_dateTime.day == birthdate_datetime.day and current_dateTime.month == birthdate_datetime.month:
        return True
    else: return False

'''
return a string with all palindrome dates from 2001 until 2192
'''
def get_all_palindrome_dates():
    result=''
    for year in range(2001, 2193):
        for month in range(1,13):
            for day in range (1, 32):
                try:

                    # raise ValueError('An example error') #inspired by chatGPT

                    year_str, month_str, day_str = fill_iso_date(year, month, day)

                    date=datetime.fromisoformat(year_str + '-' + month_str + '-' + day_str) #ValueError: day is out of range for month
                    my_date_iso,my_date_iso_hyphen, my_date_german, my_date_german_dots=format_date(date)
                    if palindrome(my_date_german):
                        result += (my_date_german_dots + ' ')



                except ValueError as e:
                    try:
                        raise MyError() #inspired by chatGPT
                    # pass
                    except MyError as e:
                        #Exception for class MyError for descriptive reasons
                        pass


    return result


'''
return a string with all ISO palindrome dates from 2001 until 2192
'''
def get_all_ISO_palindrome_dates():
    result=''
    for year in range(2001, 2193):
        for month in range(1,13):
            for day in range (1, 32):
                try:

                    # raise ValueError('An example error') #inspired by chatGPT

                    year_str, month_str, day_str = fill_iso_date(year, month, day)

                    date=datetime.fromisoformat(year_str + '-' + month_str + '-' + day_str) #ValueError: day is out of range for month
                    my_date_iso_filled,my_date_iso_hyphen, my_date_german, my_date_german_dots=format_date(date)
                    if palindrome(my_date_iso_filled):
                        result += (my_date_iso_hyphen + ' ')



                except ValueError as e:
                    try:
                        raise MyError() #inspired by chatGPT
                    # pass
                    except MyError as e:
                        #Exception for class MyError for descriptive reasons
                        pass


    return result


'''
checks:
- fourth of may
- 14. of march
- fourth of july
- a german date format palindrome date
'''
def check_date(my_dateTime, my_date_ISO, my_date_german, my_date_german_dots, date_label):
    # Define the special dates and their corresponding messages in a dictionary
    special_dates = {
        (5, 4): 'May the fourth be with you...',
        (3, 14): 'Happy Pi day!',
        (7, 4): 'Independence Day!',
        (10, 3): 'Tag der deutschen Einheit!'
    }

    # Print the date label
    print(f'{date_label.title()} is: ', my_date_ISO)

    # Check if the current date is in the dictionary and print the corresponding message
    date_key = (my_dateTime.month, my_dateTime.day)
    if date_key in special_dates:
        print(special_dates[date_key])

    # Check for palindrome date (keep the original check_palindrome_date function)
    check_palindrome_date(date_label, my_date_german, my_date_german_dots)


def check_palindrome_date(date_label, my_date_german, my_date_german_dots):
    print(f'German date {date_label} is: ', my_date_german_dots)
    if palindrome(my_date_german) == True:
        print(f'{date_label.title()} is palindrome day!')


'''
convert module datetime to
- ISO format str
- german format with dots str
- german format without dots str
'''
def format_date(my_dateTime):

    year, month, day = fill_iso_date(my_dateTime.year, my_dateTime.month, my_dateTime.day)

    my_date_ISO_hyphen = str(my_dateTime.year) + '-' + str(my_dateTime.month) + '-' + str(my_dateTime.day)

    my_date_ISO_hyphen_filled = str(year) + '-' + str(month) + '-' + str(day)


    day = my_dateTime.day
    month = my_dateTime.month
    year = my_dateTime.year

    year_str, month_str, day_str = fill_iso_date(year, month, day)

    my_date_german_dots = (day_str + '.' + month_str + '.' + year_str)
    my_date_german_list = []

    for c in my_date_german_dots:
        my_date_german_list.append(c)
    while '.' in my_date_german_list:
        my_date_german_list.remove('.')
    my_date_german = ''.join(my_date_german_list)

    my_date_ISO_list = []

    for c in my_date_ISO_hyphen_filled:
        my_date_ISO_list.append(c)
    while '-' in my_date_ISO_list:
        my_date_ISO_list.remove('-')
    my_date_ISO_filled = ''.join(my_date_ISO_list)

    # my_date_german = str(my_dateTime.day) + str(my_dateTime.month) + str(my_dateTime.year)
    return my_date_ISO_filled, my_date_ISO_hyphen_filled, my_date_german, my_date_german_dots


def fill_iso_date(year, month, day):

    if (day > 0 and day < 10):
        day_str = '0' + str(day)
    else:
        day_str = str(day)
    if (month > 0 and month < 10):
        month_str = '0' + str(month)
    else:
        month_str = str(month)
    if (year > 0 and year < 10):
        year_str = '000' + str(year)
    elif (year >= 10 and year < 100):
        year_str = '00' + str(year)
    elif (year >= 100 and year < 1000):
        year_str = '0' + str(year)
    else:
        year_str = str(year)
    return year_str, month_str, day_str


'''
file i/o
'''
def open_birthday_file():
    try:
        f = open('birthday.txt', 'r')

    except FileNotFoundError:
        birthdate = input('Please tell me your birthday (yyyy-mm-dd): ')
        f = open('birthday.txt', 'w')
        f.write(birthdate)
        f.close()
    else: birthdate = f.readline()
    return birthdate

