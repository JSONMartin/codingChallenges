"""
Write a function that accepts a string, and returns true if it is in the form of a phone number.
Assume that any integer from 0-9 in any of the spots will produce a valid phone number.

Only worry about the following format:
(123) 456-7890 (don't forget the space after the close parentheses)

Examples:

validPhoneNumber("(123) 456-7890")  =>  returns true
validPhoneNumber("(1111)555 2345")  => returns false
validPhoneNumber("(098) 123 4567")  => returns false
"""
import re
from Test.Test import Test

def validPhoneNumber(phoneNumber):
    match = re.match('\(\d{3}\) \d{3}-\d{4}', phoneNumber)
    return match != None and len(match.group(0)) == len(phoneNumber)

### TESTING

test = Test()

Test.assert_equals(validPhoneNumber("(123) 456-7890"), True)
Test.assert_equals(validPhoneNumber("(1111)555 2345"), False)