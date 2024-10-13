from birthday_palindrome import *

"""
unit tests
"""

def test_fill_iso_date():
    assert fill_iso_date(9, 9, 9) == ('0009', '09', '09') # inspired by chatGPT


def test_format_date():
    date = datetime.fromisoformat('2024-09-27')
    assert format_date(date) == ('2024-9-27', '27092024', '27.09.2024')


def test_check_birthday():
    date2 = datetime.fromisoformat('2024-09-27')
    date1 = datetime.fromisoformat('1971-09-27')
    date3 = datetime.fromisoformat('2024-09-28')

    assert check_birthday(date2, date1) == True
    assert check_birthday(date3, date1) == False


def test_check_given_date_today():

    date1 = datetime.fromisoformat('1971-09-27')
    today = datetime.today()

    assert check_given_date_today(today, date1) == False
    assert check_given_date_today(today, today) == True


def test_palindrome():
    assert palindrome('Anna') == True
    assert palindrome('Regallager') == True
    assert palindrome('Reliefpfeiler') == True
    assert palindrome('abcde') == False