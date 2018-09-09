import pandas as pd

df = pd.DataFrame({'value': range(1, 32, 2)},
                  index=pd.date_range('2018-01-01', '2018-01-31', freq='2D'))

print(df)
#             value
# 2018-01-01      1
# 2018-01-03      3
# 2018-01-05      5
# 2018-01-07      7
# 2018-01-09      9
# 2018-01-11     11
# 2018-01-13     13
# 2018-01-15     15
# 2018-01-17     17
# 2018-01-19     19
# 2018-01-21     21
# 2018-01-23     23
# 2018-01-25     25
# 2018-01-27     27
# 2018-01-29     29
# 2018-01-31     31

print(df.rolling(5).mean())
#             value
# 2018-01-01    NaN
# 2018-01-03    NaN
# 2018-01-05    NaN
# 2018-01-07    NaN
# 2018-01-09    5.0
# 2018-01-11    7.0
# 2018-01-13    9.0
# 2018-01-15   11.0
# 2018-01-17   13.0
# 2018-01-19   15.0
# 2018-01-21   17.0
# 2018-01-23   19.0
# 2018-01-25   21.0
# 2018-01-27   23.0
# 2018-01-29   25.0
# 2018-01-31   27.0

print(df.rolling('5D').mean())
#             value
# 2018-01-01    1.0
# 2018-01-03    2.0
# 2018-01-05    3.0
# 2018-01-07    5.0
# 2018-01-09    7.0
# 2018-01-11    9.0
# 2018-01-13   11.0
# 2018-01-15   13.0
# 2018-01-17   15.0
# 2018-01-19   17.0
# 2018-01-21   19.0
# 2018-01-23   21.0
# 2018-01-25   23.0
# 2018-01-27   25.0
# 2018-01-29   27.0
# 2018-01-31   29.0

print(df.resample('5D').mean())
#             value
# 2018-01-01      3
# 2018-01-06      8
# 2018-01-11     13
# 2018-01-16     18
# 2018-01-21     23
# 2018-01-26     28
# 2018-01-31     31