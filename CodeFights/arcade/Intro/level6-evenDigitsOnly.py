"""
Check if all digits of the given integer are even.

Example

For n = 248622, the output should be
evenDigitsOnly(n) = true;
For n = 642386, the output should be
evenDigitsOnly(n) = false.
"""


def evenDigitsOnly(n):
    for nChar in str(n):
        if int(nChar) % 2 == 1:
            return False

    return True


""" TESTS """
n = 248622
evenDigitsOnly(n)
