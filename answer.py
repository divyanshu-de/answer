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





""""
Q4 Blood Pressure Status
"""


def generate_status (BP_level):
  [Systolic, Diastolic] = list(map(int,BP_level.split("/")))
  if Systolic < 90 and Diastolic < 60:
    return "Low BP"
  elif Systolic >= 90 and Systolic <= 120 and Diastolic >= 60 and Diastolic <= 80:
    return "Normal"
  elif Systolic >= 120 and Systolic <= 140 and Diastolic >= 81 and Diastolic <= 90:
    return "Pre-High BP"
  elif Systolic >= 141 and Systolic <= 190 and Diastolic >= 91 and Diastolic <= 100:
    return "High BP"
  elif Systolic > 190 and Diastolic > 100:
    return "Hyper Tension"
  else:
    return "Invalid Input"
  
string_default = input()

print(generate_status(string_default))
