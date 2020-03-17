import pandas as pd

"""
Phase1  Phase2  Phase3  Phase4
0   5   10  15  20
1   25  30  40  45
2   50  55  60  65
"""

df = pd.DataFrame([[5, 10, 15, 20], [25, 30, 40, 45], [50, 55, 60, 65]],
                  columns=['Phase1', 'Phase2', 'Phase3', 'Phase4'])

if 'Phase1' in df.columns:
    print("column exists")
else:
    print("column doesn't exist")

# Test whether every element in the set is in other using issubset
if {'Phase1', 'Phase5'}.issubset(df.columns):
    print("all columns are present")
else:
    print("all columns are not present")