import pandas as pd

data = pd.read_excel("3. Descriptive Statistics.xlsx",sheet_name=0)

data.head()
Out[3]: 
   ID Gender           Birth Date  ...  Job Time  Prev Exep  Minority
0   3      f           07/26/1929  ...        98        381         0
1   4      f           04/15/1947  ...        98        190         0
2   8      f  1966-06-05 00:00:00  ...        98          0         0
3   9      f           01/23/1946  ...        98        115         0
4  10      f           02/13/1946  ...        98        244         0

[5 rows x 11 columns]

data.tail
Out[4]: 
<bound method NDFrame.tail of       ID Gender           Birth Date  ...  Job Time  Prev Exep  Minority
0      3      f           07/26/1929  ...        98        381         0
1      4      f           04/15/1947  ...        98        190         0
2      8      f  1966-06-05 00:00:00  ...        98          0         0
3      9      f           01/23/1946  ...        98        115         0
4     10      f           02/13/1946  ...        98        244         0
..   ...    ...                  ...  ...       ...        ...       ...
469  464      m           03/20/1962  ...        64         27         0
470  465      m           07/20/1962  ...        64        106         0
471  470      m           01/22/1964  ...        64         69         1
472  471      m  1966-03-08 00:00:00  ...        64         32         1
473  472      m           02/21/1966  ...        63         46         0

[474 rows x 11 columns]>

data.tail()
Out[5]: 
      ID Gender           Birth Date  ...  Job Time  Prev Exep  Minority
469  464      m           03/20/1962  ...        64         27         0
470  465      m           07/20/1962  ...        64        106         0
471  470      m           01/22/1964  ...        64         69         1
472  471      m  1966-03-08 00:00:00  ...        64         32         1
473  472      m           02/21/1966  ...        63         46         0

[5 rows x 11 columns]

data.column
Traceback (most recent call last):

  File "<ipython-input-6-57997220efc1>", line 1, in <module>
    data.column

  File "D:\Coding SoftWare\lib\site-packages\pandas\core\generic.py", line 5274, in __getattr__
    return object.__getattribute__(self, name)

AttributeError: 'DataFrame' object has no attribute 'column'


data.columns
Out[7]: 
Index(['ID', 'Gender', 'Birth Date', 'Education', 'JobCategory',
       'CurrentSalary', 'After6Months', 'SalBegin', 'Job Time', 'Prev Exep',
       'Minority'],
      dtype='object')

data.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 474 entries, 0 to 473
Data columns (total 11 columns):
 #   Column         Non-Null Count  Dtype  
---  ------         --------------  -----  
 0   ID             474 non-null    int64  
 1   Gender         474 non-null    object 
 2   Birth Date     473 non-null    object 
 3   Education      474 non-null    int64  
 4   JobCategory    474 non-null    int64  
 5   CurrentSalary  474 non-null    int64  
 6   After6Months   474 non-null    float64
 7   SalBegin       474 non-null    int64  
 8   Job Time       474 non-null    int64  
 9   Prev Exep      474 non-null    int64  
 10  Minority       474 non-null    int64  
dtypes: float64(1), int64(8), object(2)
memory usage: 40.9+ KB

data["ID"].mean
Out[9]: 
<bound method Series.mean of 0        3
1        4
2        8
3        9
4       10

469    464
470    465
471    470
472    471
473    472
Name: ID, Length: 474, dtype: int64>

data.["ID"].mean()
  File "<ipython-input-10-78e4e19bb40d>", line 1
    data.["ID"].mean()
         ^
SyntaxError: invalid syntax


data["ID"].mean()
Out[11]: 237.5

data[['CurrentSalary', 'After6Months']].median()
Out[12]: 
CurrentSalary    28875.0
After6Months     21900.0
dtype: float64

data[['CurrentSalary', 'After6Months']].mode()
Out[13]: 
   CurrentSalary  After6Months
0          30750       22875.0

data[['CurrentSalary', 'After6Months']].var()
Out[14]: 
CurrentSalary    2.915782e+08
After6Months     1.475236e+08
dtype: float64

data[['CurrentSalary', 'After6Months']].std()
Out[15]: 
CurrentSalary    17075.661465
After6Months     12145.928474
dtype: float64

data.describe()
Out[16]: 
               ID   Education  JobCategory  ...    Job Time   Prev Exep    Minority
count  474.000000  474.000000   474.000000  ...  474.000000  474.000000  474.000000
mean   237.500000   13.491561     1.411392  ...   81.109705   95.860759    0.219409
std    136.976275    2.884846     0.773201  ...   10.060945  104.586236    0.414284
min      1.000000    8.000000     1.000000  ...   63.000000    0.000000    0.000000
25%    119.250000   12.000000     1.000000  ...   72.000000   19.250000    0.000000
50%    237.500000   12.000000     1.000000  ...   81.000000   55.000000    0.000000
75%    355.750000   15.000000     1.000000  ...   90.000000  138.750000    0.000000
max    474.000000   21.000000     3.000000  ...   98.000000  476.000000    1.000000

[8 rows x 9 columns]

data.sum()
Out[17]: 
ID                                                          112575
Gender           ffffffffffffffffffffffffffffffffffffffffffffff...
Education                                                     6395
JobCategory                                                    669
CurrentSalary                                             16314875
After6Months                                           1.21902e+07
SalBegin                                                   8065625
Job Time                                                     38446
Prev Exep                                                    45438
Minority                                                       104
dtype: object

data.skew()
Out[18]: 
ID               0.000000
Education       -0.114107
JobCategory      1.455978
CurrentSalary    2.124606
After6Months     2.267649
SalBegin         2.852856
Job Time        -0.052570
Prev Exep        1.509984
Minority         1.360322
dtype: float64

data.kurt()
Out[19]: 
ID               -1.200000
Education        -0.265000
JobCategory       0.267547
CurrentSalary     5.377822
After6Months      6.823250
SalBegin         12.390215
Job Time         -1.152594
Prev Exep         1.695953
Minority         -0.150174
dtype: float64