import pandas as pd



d = pd.read_excel("general_data.xlsx",sheet_name=0)

d.head()
Out[27]: 
   Age Attrition  ... YearsSinceLastPromotion YearsWithCurrManager
0   51        No  ...                       0                    0
1   31       Yes  ...                       1                    4
2   32        No  ...                       0                    3
3   38        No  ...                       7                    5
4   32        No  ...                       0                    4

[5 rows x 24 columns]

d.columns
Out[28]: 
Index(['Age', 'Attrition', 'BusinessTravel', 'Department', 'DistanceFromHome',
       'Education', 'EducationField', 'EmployeeCount', 'EmployeeID', 'Gender',
       'JobLevel', 'JobRole', 'MaritalStatus', 'MonthlyIncome',
       'NumCompaniesWorked', 'Over18', 'PercentSalaryHike', 'StandardHours',
       'StockOptionLevel', 'TotalWorkingYears', 'TrainingTimesLastYear',
       'YearsAtCompany', 'YearsSinceLastPromotion', 'YearsWithCurrManager'],
      dtype='object')

d.isnull
Out[29]: 
<bound method DataFrame.isnull of       Age Attrition  ... YearsSinceLastPromotion YearsWithCurrManager
0      51        No  ...                       0                    0
1      31       Yes  ...                       1                    4
2      32        No  ...                       0                    3
3      38        No  ...                       7                    5
4      32        No  ...                       0                    4
  ...       ...  ...                     ...                  ...
4405   42        No  ...                       0                    2
4406   29        No  ...                       0                    2
4407   25        No  ...                       1                    2
4408   42        No  ...                       7                    8
4409   40        No  ...                       3                    9

[4410 rows x 24 columns]>

d.isnull()
Out[30]: 
        Age  Attrition  ...  YearsSinceLastPromotion  YearsWithCurrManager
0     False      False  ...                    False                 False
1     False      False  ...                    False                 False
2     False      False  ...                    False                 False
3     False      False  ...                    False                 False
4     False      False  ...                    False                 False
    ...        ...  ...                      ...                   ...
4405  False      False  ...                    False                 False
4406  False      False  ...                    False                 False
4407  False      False  ...                    False                 False
4408  False      False  ...                    False                 False
4409  False      False  ...                    False                 False

[4410 rows x 24 columns]

d.duplicated()
Out[31]: 
0       False
1       False
2       False
3       False
4       False
 
4405    False
4406    False
4407    False
4408    False
4409    False
Length: 4410, dtype: bool




d.drop_duplicates()
Out[33]: 
      Age Attrition  ... YearsSinceLastPromotion YearsWithCurrManager
0      51        No  ...                       0                    0
1      31       Yes  ...                       1                    4
2      32        No  ...                       0                    3
3      38        No  ...                       7                    5
4      32        No  ...                       0                    4
  ...       ...  ...                     ...                  ...
4405   42        No  ...                       0                    2
4406   29        No  ...                       0                    2
4407   25        No  ...                       1                    2
4408   42        No  ...                       7                    8
4409   40        No  ...                       3                    9

[4410 rows x 24 columns]

d.columns
Out[34]: 
Index(['Age', 'Attrition', 'BusinessTravel', 'Department', 'DistanceFromHome',
       'Education', 'EducationField', 'EmployeeCount', 'EmployeeID', 'Gender',
       'JobLevel', 'JobRole', 'MaritalStatus', 'MonthlyIncome',
       'NumCompaniesWorked', 'Over18', 'PercentSalaryHike', 'StandardHours',
       'StockOptionLevel', 'TotalWorkingYears', 'TrainingTimesLastYear',
       'YearsAtCompany', 'YearsSinceLastPromotion', 'YearsWithCurrManager'],
      dtype='object')


SyntaxError: invalid syntax


 d[['Age', 'Attrition', 'BusinessTravel', 'Department', 'DistanceFromHome',
       'Education', 'EducationField', 'EmployeeCount', 'EmployeeID', 'Gender',
       'JobLevel', 'JobRole', 'MaritalStatus', 'MonthlyIncome',
       'NumCompaniesWorked', 'Over18', 'PercentSalaryHike', 'StandardHours',
       'StockOptionLevel', 'TotalWorkingYears', 'TrainingTimesLastYear',
       'YearsAtCompany', 'YearsSinceLastPromotion', 'YearsWithCurrManager']].describe()
Out[38]: 
               Age  ...  YearsWithCurrManager
count  4410.000000  ...           4410.000000
mean     36.923810  ...              4.123129
std       9.133301  ...              3.567327
min      18.000000  ...              0.000000
25%      30.000000  ...              2.000000
50%      36.000000  ...              3.000000
75%      43.000000  ...              7.000000
max      60.000000  ...             17.000000

[8 rows x 16 columns]

d.describe()
Out[39]: 
               Age  ...  YearsWithCurrManager
count  4410.000000  ...           4410.000000
mean     36.923810  ...              4.123129
std       9.133301  ...              3.567327
min      18.000000  ...              0.000000
25%      30.000000  ...              2.000000
50%      36.000000  ...              3.000000
75%      43.000000  ...              7.000000
max      60.000000  ...             17.000000

[8 rows x 16 columns]

d.mode()
Out[40]: 
       Age Attrition  ... YearsSinceLastPromotion YearsWithCurrManager
0     35.0        No  ...                     0.0                  2.0
1      NaN       NaN  ...                     NaN                  NaN
2      NaN       NaN  ...                     NaN                  NaN
3      NaN       NaN  ...                     NaN                  NaN
4      NaN       NaN  ...                     NaN                  NaN
   ...       ...  ...                     ...                  ...
4405   NaN       NaN  ...                     NaN                  NaN
4406   NaN       NaN  ...                     NaN                  NaN
4407   NaN       NaN  ...                     NaN                  NaN
4408   NaN       NaN  ...                     NaN                  NaN
4409   NaN       NaN  ...                     NaN                  NaN

[4410 rows x 24 columns]

d.median()
Out[41]: 
Age                           36.0
DistanceFromHome               7.0
Education                      3.0
EmployeeCount                  1.0
EmployeeID                  2205.5
JobLevel                       2.0
MonthlyIncome              49190.0
NumCompaniesWorked             2.0
PercentSalaryHike             14.0
StandardHours                  8.0
StockOptionLevel               1.0
TotalWorkingYears             10.0
TrainingTimesLastYear          3.0
YearsAtCompany                 5.0
YearsSinceLastPromotion        1.0
YearsWithCurrManager           3.0
dtype: float64

d.mean()
Out[42]: 
Age                           36.923810
DistanceFromHome               9.192517
Education                      2.912925
EmployeeCount                  1.000000
EmployeeID                  2205.500000
JobLevel                       2.063946
MonthlyIncome              65029.312925
NumCompaniesWorked             2.694830
PercentSalaryHike             15.209524
StandardHours                  8.000000
StockOptionLevel               0.793878
TotalWorkingYears             11.279936
TrainingTimesLastYear          2.799320
YearsAtCompany                 7.008163
YearsSinceLastPromotion        2.187755
YearsWithCurrManager           4.123129
dtype: float64

d.skew()
Out[43]: 
Age                        0.413005
DistanceFromHome           0.957466
Education                 -0.289484
EmployeeCount              0.000000
EmployeeID                 0.000000
JobLevel                   1.024703
MonthlyIncome              1.368884
NumCompaniesWorked         1.026767
PercentSalaryHike          0.820569
StandardHours              0.000000
StockOptionLevel           0.968321
TotalWorkingYears          1.116832
TrainingTimesLastYear      0.552748
YearsAtCompany             1.763328
YearsSinceLastPromotion    1.982939
YearsWithCurrManager       0.832884
dtype: float64

d.kurt()
Out[44]: 
Age                       -0.405951
DistanceFromHome          -0.227045
Education                 -0.560569
EmployeeCount              0.000000
EmployeeID                -1.200000
JobLevel                   0.395525
MonthlyIncome              1.000232
NumCompaniesWorked         0.007287
PercentSalaryHike         -0.302638
StandardHours              0.000000
StockOptionLevel           0.361086
TotalWorkingYears          0.912936
TrainingTimesLastYear      0.491149
YearsAtCompany             3.923864
YearsSinceLastPromotion    3.601761
YearsWithCurrManager       0.167949
dtype: float64

import matplotlib.pyplot as plt

plt.boxplot(d.Age)
Out[46]: 
{'whiskers': [<matplotlib.lines.Line2D at 0x1b734644148>,
  <matplotlib.lines.Line2D at 0x1b7350b1dc8>],
 'caps': [<matplotlib.lines.Line2D at 0x1b7350cc148>,
  <matplotlib.lines.Line2D at 0x1b7350c31c8>],
 'boxes': [<matplotlib.lines.Line2D at 0x1b7350b7608>],
 'medians': [<matplotlib.lines.Line2D at 0x1b7350e8348>],
 'fliers': [<matplotlib.lines.Line2D at 0x1b734aa1a08>],
 'means': []}


Figures now render in the Plots pane by default. To make them also appear inline in the Console, uncheck "Mute Inline Plotting" under the Plots pane options menu. 


 

box_plot = d.MonthlyIncome

plt.boxplot(box_plot)
Out[48]: 
{'whiskers': [<matplotlib.lines.Line2D at 0x1b73513bd88>,
  <matplotlib.lines.Line2D at 0x1b73513bf08>],
 'caps': [<matplotlib.lines.Line2D at 0x1b735154f48>,
  <matplotlib.lines.Line2D at 0x1b735154ec8>],
 'boxes': [<matplotlib.lines.Line2D at 0x1b734cd6c08>],
 'medians': [<matplotlib.lines.Line2D at 0x1b735158348>],
 'fliers': [<matplotlib.lines.Line2D at 0x1b735158d88>],
 'means': []}

plt.boxplot(d.MonthlyIncome)
Out[49]: 
{'whiskers': [<matplotlib.lines.Line2D at 0x1b7363f1c88>,
  <matplotlib.lines.Line2D at 0x1b7363e4d88>],
 'caps': [<matplotlib.lines.Line2D at 0x1b7363e17c8>,
  <matplotlib.lines.Line2D at 0x1b7363e1d08>],
 'boxes': [<matplotlib.lines.Line2D at 0x1b7350e5bc8>],
 'medians': [<matplotlib.lines.Line2D at 0x1b7363e1e08>],
 'fliers': [<matplotlib.lines.Line2D at 0x1b7363da808>],
 'means': []}



plt.scatter(d.Age,d.TotalWorkingYears)
Out[53]: <matplotlib.collections.PathCollection at 0x1b736a8f448>

plt.hist(d.Age)
Out[54]: 
(array([171., 315., 672., 795., 765., 651., 393., 276., 231., 141.]),
 array([18. , 22.2, 26.4, 30.6, 34.8, 39. , 43.2, 47.4, 51.6, 55.8, 60. ]),
 <a list of 10 Patch objects>)
