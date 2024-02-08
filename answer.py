""""
Q3 Sentence Palindrome
"""

import re

def is_palindrome(sentence):
  return sentence == sentence[::-1]
  
string_default = input()

# if is_palindrome(re.sub('\W+','', string_default).lower()):
if is_palindrome(re.sub('\W+','', string_default)):
  print(string_default + " is a palindrome")
else:
  print(string_default + " is not a palindrome")
