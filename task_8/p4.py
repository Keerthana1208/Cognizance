import pandas as pd
ser = pd.Series(['amrita', 'school', 'of', 'engineering', 'chennai', 'campus'])
for i in ser:
    x = i
    y= x.capitalize()
    print(y , end = " ")


