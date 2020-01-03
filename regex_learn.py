import re


pattern = '^a...s$'
test_string = "abyss"


result = re.match(pattern,test_string)
if result:
    print('match found!')
else:
    print('match not found')





## metacharacters = [] . ^ $ * + ? {} () \ |

# 1. square brackets it specifies a set of characters you wish to match

    #[a-e] is the same as [abcde].
    #[1-4] is the same as [1234].
    #[0-39] is the same as [01239].


#2. .: Period-A period matches any single character

#3. ^:Caret-The caret symbol is used to check if a string starts with a certain character
#4. $:Dollar-The Dollar symbol is used to check if a string ends with a certain character

#5. *:Star-The star symbol matches zero or more occurences of the pattern left to it
####  for e.g:
####  ma*n will match with man, maan, woman and not with main, maine because is not followed by n

#6. +: Plus-The plus symbol matches one or more occurences of the pattern left to it.

#7. ?: Question Mark-The question mark symbol matches zero or one of the pattern left to it.

#8. {}:Braces-Consider this code {n,m},This means at least n and at most m repititions of the pattern left to it

#9.  |:Alternation-Verical Bar or Pipe '|' is used as 'or' operator

#10. (): Group-Parentheses is used to group sub patterns. For Example, (a|b|c)xz match any string that matches either a or b or c followed by xz

#11 \:Backlash- is used to escape various characters including all metacharacters. For example \$a match if a string contains $ followed by a. here ,$ is not interpretd a RegEx engine


'''
Special Sequences

\A - Matches if the specified characters are at thestart of a string

\b - Matches if the specified characters are at the beigning or end of a word.
\B - Opposite of \b . Matches if the specified characters are not at the beigning or end of a word.

\d- Matches any non-decimal digit.Equivalent to [^0-9]

\s - matches where a string contains any whitespace character.equivalent to [\t\n\r\f\v].
\S - matches where a string contain s any non-whitespace character. Equivalent to [^ \t\tn\r\f\v].

\w - matches any alphanumeric character. Equivalent to [a-zA-Z0-9_]
\W - Matches any non-alphanumeric character. same as not[a-zA-Z0-9_].

\Z -matches if the specified characters are at the end of a string
'''



## re.findall()

string = 'hello 21 hi 889. Howdy 34'
pattern = '\d+'

result = re.findall(pattern,string)
print(result)


## re.split()

string = 'Twelve:12 Eighty nine:89.'
pattern = '\d+'

result = re.split(pattern,string)
print(result)

## re.sub()
string = 'abc 12\ de 23 \n f45 6'
# we are going to match all white space characters
pattern = '\s+'

replace = ''

new_string = re.sub(pattern,replace,string)
print(new_string)



## re.subn()

new_string = re.subn(pattern,replace,string)
print(new_string)




## re.search()

string = 'Python is fun'

match = re.search('\APython',string)

if match:
    print('pattern found inside the string!')
else:
    print('match not found')



## match.group()
    
string = '39875 345, 7864 4434, 0099 0000'
pattern = '(\d{3}) (\d{2})'

match = re.search(pattern,string)

if match:
    print(match.group())
else:
    print('pattern not found')

    
