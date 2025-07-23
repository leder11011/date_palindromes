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


from pynput import keyboard

def on_press(key):
    print(f"Key {key} pressed.")
    # Stop listener after the first key press
    return False




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
             '1-1': "Happy New Year!",
             '1-20': 'Inauguration Day (USA)',
             '2-2': 'Groundhog Day',
             '2-11': 'International Day of Women and Girls in Science',
             '2-14': "Valentine's Day",
             '2-27': 'Pokémon Day',
             '3-8': "Women's Day",
             '3-10': 'Mario Day (MAR10)',
             '3-14': 'Happy Pi Day!',
             '3-17': 'St. Patrick\'s Day',
             '3-20': 'International Day of Happiness',
             '4-1': 'April Fools\' Day',
             '4-2': 'World Autism Awareness Day',
             '4-7': 'World Health Day',
             '4-22': 'Earth Day!',
             '4-26': 'Alien Day (LV-426)',
             '5-1': 'International Workers\' Day',
             '5-2': 'Harry Potter Battle of Hogwarts Day',
             '5-3': 'Save Social Day',
             '5-4': 'May the Fourth be with you...',
             '5-8': 'Anniversary of the End of World War II',
             '5-9': 'Mother\'s Day (US)',
             '5-25': 'Geek Pride Day (also Towel Day)',
             '6-1': 'International Children\'s Day',
             '6-5': 'World Environment Day',
             '6-8': 'World Oceans Day',
             '6-18': 'Autistic Pride Day',
             '6-19': 'Juneteenth!',
             '6-20': 'Father\'s Day (US)',
             '6-21': 'First Day of Summer!',
             '6-23': 'Sonic the Hedgehog’s Birthday',
             '7-4': 'Independence Day!',
             '7-13': 'Embrace Your Geekness Day',
             '7-15': 'Gummi Worm Day',
             '7-20': 'Moon Landing Day',
             '7-30': 'International Friendship Day',
             '8-12': 'International Youth Day',
             '8-19': 'World Photography Day!',
             '8-29': 'Skynet Activation Day (Terminator)',
             '9-11': 'Patriot Day!',
             '9-13': 'Supernatural Day',
             '9-21': 'International Day of Peace',
             '9-22': 'First Day of Fall!',
             '9-25': 'One Piece Day (Japanese release anniversary)',
             '9-30': 'International Podcast Day',
             '10-3': 'Tag der deutschen Einheit!',
             '10-5': 'World Teachers\' Day',
             '10-10': 'World Mental Health Day',
             '10-16': 'World Food Day',
             '10-21': 'Back to the Future Day',
             '10-31': 'Happy Halloween!',
             '11-11': 'Veterans Day!',
             '11-13': 'World Kindness Day',
             '11-20': 'Universal Children\'s Day',
             '11-23': 'Doctor Who Day',
             '11-25': 'Thanksgiving Day (US)',
             '12-6': 'St. Nicholas Day',
             '12-10': 'Human Rights Day',
             '12-17': 'Wright Brothers Day / Simpsons Anniversary',
             '12-24': 'Christmas Eve',
             '12-25': 'Merry Christmas!',
             '12-31': 'Happy New Year\'s Eve!'

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

    print('\n')
    #print('Move outside of the terminal window and press a key to quit the app...')

    # Create a listener
    #with keyboard.Listener(on_press=on_press) as listener:
     #   listener.join()
      #  print('Done.')

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