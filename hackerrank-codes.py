#matrix-script

#!/bin/python3

import math
import os
import random
import re
import sys




first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)
matrix = list(zip(*matrix))

sample = str()

for words in matrix:
    for char in words:
        sample += char
                   
print(re.sub(r'(?<=\w)([^\w\d]+)(?=\w)', ' ', sample))

-------------------------------------------------------------------------------------------------------------------------

#Matching {x} Repetitions

Regex_Pattern = r'^[a-zA-Z24680]{40}[13579\s]{5}$'	# Do not delete 'r'.

---------------------------------------------------------------------------------------------------------------------------

#Alternative Matching

Regex_Pattern = r'^(Mr?s|[MDE]r)\.[a-zA-Z]+$'	# Do not delete 'r'.

----------------------------------------------------------------------------------------------------------------------------

#Matching Specific String

Regex_Pattern = r'hackerrank'	# Do not delete 'r'.

----------------------------------------------------------------------------------------------------------------------------

#Matching Start & End

Regex_Pattern = r"^\d\w{4}\.$"	# Do not delete 'r'

----------------------------------------------------------------------------------------------------------------------------

#Matching Word & Non-Word Character

Regex_Pattern = r"\w{3}\W\w{10}\W\w{3}"	# Do not delete 'r'.

----------------------------------------------------------------------------------------------------------------------------

#Detect HTML links

import re

if __name__ == '__main__':
    n = int(input())
    Regex = r'<a href="(.*?)".*?>([\w ,./]*)(?=</)'
    for _ in range(n):
        s = input()
        links = re.findall(Regex, s)
        for link, att in links:
            print('%s,%s' % (link, att.strip()))


------------------------------------------------------------------------------------------------------------------------------

#Building a Smart IDE: Programming Language Detection

import re
import sys

class Main:
    def __init__(self):
        self.s = ''.join(sys.stdin.readlines())
                    
    def output(self):
        if 'java' in self.s:
            print("Java")
        elif '#include' in self.s:
            print("C")
        else:
            print("Python")
                                                                                            
if __name__ == '__main__':
    obj = Main()
    obj.output()


------------------------------------------------------------------------------------------------------------------------------------

Detect the Domain Name

import re
pattern = '(http|https)\\://(www.|ww2.|)([a-zA-Z0-9\\-\\.]+)(\\.[a-zA-Z]+)(/\\S*)?'
regex = re.compile(pattern)
s = set()
for i in range(int(input())):
    string = input()
    iterator = regex.finditer(string)
    if iterator:
        for match in iterator:
            s.add(match.group(3)+match.group(4))
print(';'.join(t for t in sorted(s)))


