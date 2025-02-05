import re

amounts = r'thousand|million|billion'   # If 'thousands', 'millions', and 'billions' will still match
number = r"\d+(,\d{3})*\.*\d*"

word_re = rf'\${number}(-|\sto\s)?({number})?\s({amounts})'   # Takes the lower value when presented a range
value_re = rf'\${number}'
# word_syntax


# Convert word to numberical value using a dictionary
def word_to_value(word):
    value_dict = {'thousand':1000, 'million':1000000, 'billion':1000000000, 'trillion':1000000000000}
    return value_dict[word]


# Capture the word part of the dollar value
def parse_word_syntax(string):
    value_string = re.search(number, string).group()   # Getting the number part
    value = float(value_string.replace(',', ''))
    word = re.search(amounts, string, flags=re.I).group().lower()
    word_value = word_to_value(word)
    return value * word_value

# Clean up the numberical and strip comma
def parse_value_syntax(string):
    value_string = re.search(number, string).group()
    value = float(value_string.replace(',', ''))
    return value

'''
money_conversion("$12.2 million") --> 12200000
money_conversion("$790,000") --> 790000
'''
def money_conversion(money):

    if money == 'N/A':
        return None

    # If a list, just take the first element
    if isinstance(money, list):
        money = money[0]

    word_syntax = re.search(word_re, money, flags=re.I)
    value_syntax = re.search(value_re, money)  # f-string

    if word_syntax:
        return parse_word_syntax(word_syntax.group())
        
    elif value_syntax: # Value syntax is a subset of the word syntax, thus it is important to have the word syntax first.
        return parse_value_syntax(value_syntax.group())

    else:
        return None
    
print(money_conversion('$790 Millions'))