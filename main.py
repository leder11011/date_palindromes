from datetime import datetime, time

import time

from birthday_palindrome import open_birthday_file, format_date, check_birthday, check_date, fill_iso_date, \
    check_given_date_today, get_all_palindrome_dates, get_all_ISO_palindrome_dates, check_ISO_palindrome_date
from birthday_palindrome import check_palindrome_date

"""
input/output
"""


def is_special_day(label, given_datetime, birthday_m_d, birthdate_datetime, dates):
    key = str(given_datetime.month) + '-' + str(given_datetime.day)

    salut = dates.get(key, f'No special day {label}...')

    print(salut)

    if key == birthday_m_d:
        print(f'It is your {given_datetime.year - birthdate_datetime.year}. birthday {label}!')


def is_today(input_datetime, current_datetime):
    # debug
    #print('current: ' + str(current_datetime))
    #print('given: ' + str(input_datetime))
    #########

    if (input_datetime.year == current_datetime.year and input_datetime.month == current_datetime.month and input_datetime.day == current_datetime.day):
        print('Given day is today!')


"""
sequential control and input/output
"""

def main():
    birthdate = open_birthday_file()
    birthdate_datetime = datetime.fromisoformat(birthdate)

    current_datetime = datetime.now()
    my_date_iso_filled, my_date_iso_hyphen_filled, my_date_german, my_date_german_dots = format_date(current_datetime)

    birthday_m_d = str(birthdate_datetime.month) + '-' + str(birthdate_datetime.day)
    dates = {birthday_m_d: 'HAPPY BIRTHDAY!!!',
         '5-4': 'may the fourth be with you...',
         '3-14': 'Happy Pi-day!',
         '7-4': 'Independence day!',
         '10-3': 'Tag der deutschen Einheit!',
         '3-8' : "Woman's day",
         '2-14': "Valentine's day",
         '1-1': "Happy New Year!",
         '12-24': 'Christmas Eve',
         '12-25': 'Merry Christmas!',
         '10-31': 'Happy Halloween!',
         '11-11': 'Veterans Day!',
         '12-31': 'Happy New Year\'s Eve!',
         '4-22': 'Earth Day!',
         '6-21': 'First Day of Summer!',
         '9-22': 'First Day of Fall!',
         '6-19': 'Juneteenth!',
         '8-19': 'World Photography Day!',
         '9-11': 'Patriot Day!',
         '11-25': 'Thanksgiving Day (US)',
         '1-20': 'Inauguration Day (USA)',
         '2-2': 'Groundhog Day',
         '4-1': 'April Fools\' Day',
         '5-9': 'Mother\'s Day (US)',
         '6-20': 'Father\'s Day (US)',
         '7-20': 'Moon Landing Day',
         '5-3': 'Save Social Day',
         '5-8': ' Anniversary of the End of World War II'
         }

    is_special_day('today', current_datetime, birthday_m_d, birthdate_datetime, dates)

    print(f'Today is: {my_date_iso_hyphen_filled}')

    check_ISO_palindrome_date('today', my_date_iso_filled)

    check_palindrome_date('today', my_date_german, my_date_german_dots)

    # if check_birthday(current_datetime, birthdate_datetime):
    #     print(f'HAPPY BIRTHDAY!!!')

    # is_birthday_today(birthdate_datetime, current_datetime, current_datetime)
    #
    # check_date(current_datetime, my_date_iso_filled, my_date_german, my_date_german_dots, 'today')


    while True:
        print("\nPlease tell me a date (yyyy-mm-dd): ")
        print("(enter 'q' at any time to quit)")


        date_txt = input("date: ")


        if date_txt == 'q':
          break

        date_list = date_txt.split('-')

        date_str = ''

        try:
            year_str, month_str, day_str = fill_iso_date(int(date_list[0]), int(date_list[1]), int(date_list[2]))

            date_str = year_str + '-' + month_str + '-' + day_str

            # print(date_str)


            input_datetime = datetime.fromisoformat(date_str)

            # print(input_datetime)

        except IndexError:
            print(f'No valid ISO format given! {date_txt}')
        except ValueError:
            print(f'No valid date given! {date_str}')
        else:
            is_today(input_datetime, current_datetime)

            is_special_day('given', input_datetime, birthday_m_d, birthdate_datetime, dates)

            # is_birthday_today(birthdate_datetime, current_datetime, input_datetime)

            my_date_iso_filled, my_date_iso_hyphen_filled, my_date_german, my_date_german_dots = format_date(input_datetime)

            check_ISO_palindrome_date('given', my_date_iso_filled)

            check_palindrome_date('given', my_date_german, my_date_german_dots)

            # check_date(input_datetime, my_date_iso_filled, my_date_german, my_date_german_dots, 'given')





    #year='2001'
    #month='09'
    #day='27'

    #date=datetime.fromisoformat(str(year)+'-'+str(month)+'-'+str(day))

    #print(date)

    print('\nAll palindrome dates between 01.01.2001 and 31.12.2192: ')

    palindrome_dates = get_all_palindrome_dates()
    print(palindrome_dates)

    palindrome_dates_list = palindrome_dates.split()

    print(f'\n#{len(palindrome_dates_list)}')



    print('\n\nAll ISO palindrome dates between 2001-01-01 and 2292-12-31: ')

    iso_palindrome_dates = get_all_ISO_palindrome_dates()
    print(iso_palindrome_dates)

    iso_palindrome_dates_list = iso_palindrome_dates.split()

    print(f'\n#{len(iso_palindrome_dates_list)}')

    time.sleep(10)

"""
input/output
"""

def is_birthday_today(birthdate_datetime, current_datetime, input_datetime):
    if check_birthday(input_datetime, birthdate_datetime):
        if check_given_date_today(current_datetime, input_datetime):
            print('HAPPY BIRTHDAY!!!')
        else:
            print(f'Given date is your {input_datetime.year - birthdate_datetime.year}. birthday!')
    elif check_given_date_today(current_datetime, input_datetime):
        print(f'Given date is today!')


if __name__ == "__main__":
    main()