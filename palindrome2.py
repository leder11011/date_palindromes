
"""
library function for testing a string if it is a palindrome
"""

def palindrome(test):
    test = test.lower()
    palindrome=True
    last_index = len(test)
    for value in range(1, (last_index//2)+1):
        if test[value-1]!=test[last_index-value]: palindrome=False #last_index-value==last_index-1-(value-1)

    return palindrome

