"""
Regular expression to allow format of:
    00 followed by 1 to 3 digits
    city code: 2 to 4 digits
    area and number: one group of 8 or two groups of 4
    all above can be separated by a space or a dash
"""
import re

test = '0044 4635 8977-5366'

pattern = '[0]{2}[0-9]{1,3}[\s-]+[0-9]{2,4}[\s-]+(?:\d{4}[\s-]+\d{4}|\d{8})'
pattern = re.compile(pattern)
match = pattern.findall(test)
print(match)

"""
Test that international codes are allowed (Russia and USA)
"""

test2 = '007-4653-2312-3212'
match = pattern.findall(test2)
print(match)

test3 = '001-4653-2312-3212'
match = pattern.findall(test3)
print(match)

"""
Capture the four components into variables
"""
test4 = '0044-4635 8977-5366'
pattern = re.compile(r"\s*[\s-]+\s*")
country, city, area, number = pattern.split(test4)
print("country {}, city {}, area {}, number {}".format(country, city, area, number))

"""
Using re sub to replace spaces with dashes
"""
match = pattern.sub(" ", test4)
print(match)
