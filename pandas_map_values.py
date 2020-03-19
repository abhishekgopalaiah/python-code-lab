import pandas as pd

"""
# change the values in Marks column, Pass as Passed and Fail and Failed
"""

df = pd.DataFrame([['Uma', 'Science', 'Pass'], ['Priya', 'Maths', 'Fail'], ['Abhi', 'Social', 'Fail']],
                  columns=['Name', 'Subject', 'Marks'])
print(f'before changing values : \n{df}')

df['Marks'] = df['Marks'].map({'Pass': 'Passed', 'Fail': 'Failed'})
print(f'after changing values : \n{df}')

"""
output:
before changing values : 
    Name  Subject Marks
0    Uma  Science  Pass
1  Priya    Maths  Fail
2   Abhi   Social  Fail
after changing values : 
    Name  Subject   Marks
0    Uma  Science  Passed
1  Priya    Maths  Failed
2   Abhi   Social  Failed
"""