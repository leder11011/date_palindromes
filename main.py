from datetime import datetime


from birthday_palindrome import open_birthday_file, format_date, check_birthday, check_date, fill_iso_date, \
    check_given_date_today, get_all_palindrome_dates
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
    if input_datetime.year == current_datetime.year and input_datetime.month == current_datetime.month and input_datetime.day == input_datetime.day:
        print('Given day is today!')


"""
sequential control and input/output
"""

def main():
    birthdate = open_birthday_file()
    birthdate_datetime = datetime.fromisoformat(birthdate)

    current_datetime = datetime.now()
    my_date_iso, my_date_german, my_date_german_dots = format_date(current_datetime)

    birthday_m_d = str(birthdate_datetime.month) + '-' + str(birthdate_datetime.day)
    dates = {birthday_m_d: 'HAPPY BIRTHDAY!!!',
         '5-4': 'may the fourth be with you...',
         '3-14': 'Happy Pi-day!',
         '7-4': 'Independence day!',
         '10-3': 'Tag der deutschen Einheit!'
         }

    is_special_day('today', current_datetime, birthday_m_d, birthdate_datetime, dates)

    print(f'Today is: {my_date_iso}')

    check_palindrome_date('today', my_date_german, my_date_german_dots)

    # if check_birthday(current_datetime, birthdate_datetime):
    #     print(f'HAPPY BIRTHDAY!!!')

    # is_birthday_today(birthdate_datetime, current_datetime, current_datetime)
    #
    # check_date(current_datetime, my_date_iso, my_date_german, my_date_german_dots, 'today')


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

            my_date_iso, my_date_german, my_date_german_dots = format_date(input_datetime)

            check_palindrome_date('given', my_date_german, my_date_german_dots)

            # check_date(input_datetime, my_date_iso, my_date_german, my_date_german_dots, 'given')





    #year='2001'
    #month='09'
    #day='27'

    #date=datetime.fromisoformat(str(year)+'-'+str(month)+'-'+str(day))

    #print(date)

    print('\nAll palindrome dates between 01.01.2001 and 31.12.2192: ')

    palindrome_dates = get_all_palindrome_dates()
    print(palindrome_dates)

    palindrome_dates_list = palindrome_dates.split()

    print(f'#{len(palindrome_dates_list)}')

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