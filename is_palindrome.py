# Define a procedure is_palindrome, that takes as input a string, and returns a
# Boolean indicating if the input string is a palindrome.

# Base Case: '' => True
# Recursive Case: if first and last characters don't match => False
# if they do match, is the middle a palindrome?

# Recursive
def is_palindrome(s):
    if s == '':
        return True
    else:
        if s[0] == s[-1]:
            return is_palindrome(s[1:-1])
        else:
            return False


# Iterative
def is_palindrome(s):
    if s == '': return True
    i = 0
    while i <= len(s) // 2:
        if s[i] != s[-(i + 1)]: return False
        i += 1
    return True



####################
#      TESTS       #
####################
print(is_palindrome(''))
print(is_palindrome('abab'))
print(is_palindrome('abba'))