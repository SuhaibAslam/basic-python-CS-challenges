# Question 5: Date Converter

# Write a procedure date_converter which takes two inputs. The first is
# a dictionary and the second a string. The string is a valid date in
# the format month/day/year. The procedure should return
# the date written in the form <day> <name of month> <year>.
# For example , if the
# dictionary is in English,

english = {1:"January", 2:"February", 3:"March", 4:"April", 5:"May",
6:"June", 7:"July", 8:"August", 9:"September",10:"October",
11:"November", 12:"December"}

# then  "5/11/2012" should be converted to "11 May 2012".
# If the dictionary is in Swedish

swedish = {1:"januari", 2:"februari", 3:"mars", 4:"april", 5:"maj",
6:"juni", 7:"juli", 8:"augusti", 9:"september",10:"oktober",
11:"november", 12:"december"}

# then "5/11/2012" should be converted to "11 maj 2012".


def date_converter(month_dict, date):
    day = date.split('/')[1]
    month = month_dict[int(date.split('/')[0])]
    year = date.split('/')[2]
    converted_date = day+' '+month+' '+year
    return converted_date


####################
#      TESTS       #
####################

print(date_converter(english, '5/11/2012'))
print(date_converter(swedish, '5/11/2012'))
print(date_converter(swedish, '12/5/1791'))

