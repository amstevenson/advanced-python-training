import re

test = "-------ABC------------"
pattern = r"\w+"
pattern = re.compile(pattern)

match = pattern.match(test)
print (match) # none

match = pattern.search(test)
print (match.group()) # ABC

##

pattern = re.compile(r"\s*;\s*")
text = "aaa  ; bbb ;ccc     ;        ddd ;  eee"
list = pattern.split(text)
print (list)

##

pattern = re.compile(r"\s*;\s*")
text = "aaa  ; bbb ;ccc     ;        ddd ;  eee"
newText = pattern.sub("---", text)
print (newText)

##

string = "AAAA1111BBBB2222CCCC3333DDDD";
pattern = r"""
    ^   # start of line
    (.*?)   # 0 or more characters
        # non greedy
    (\d+)   # 1 or more digits
    (.*)    # 0 or more characters
    $   # end of line
           """

compiledPattern = re.compile(pattern, re.VERBOSE)
result = compiledPattern.search(string)
print(result)

##


text = "---111122223333333333334444555566667777---"
pattern = "2+(3+)4+(5+)6+"

# search for pattern
pattern = re.compile(pattern)
result = pattern.search(text)

# print results
print ("full match: ", result.group(0))
print ("capture pattern 1: ", result.group(1))
print ("capture pattern 2: ", result.group(2))
print ("all captures: ", result.groups())

##


text = "AB12CD34EF56GH"
pattern = r"(\d+)"

# find all occurrences of pattern
matcher = re.findall(pattern, text)
print (matcher)

# iterate through finding the pattern
for matcher in re.finditer(pattern, text):
    print (matcher.groups(0))