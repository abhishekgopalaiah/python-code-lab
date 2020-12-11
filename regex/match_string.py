"""
output :
Number of matches : 1
"""
import re

Regex_Pattern = r'Hello'
Test_String = 'Hello Tech Jaala viewers'

match = re.findall(Regex_Pattern, Test_String)

print("Number of matches :", len(match))

