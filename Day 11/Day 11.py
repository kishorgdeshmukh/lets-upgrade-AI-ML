

import pandas as pd 




data = pd.read_csv("general_data.csv")

data.Attrition[data.Attrition == 'Yes'] = 1
__main__:1: SettingWithCopyWarning: 
A value is trying to be set on a copy of a slice from a DataFrame

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

data.Attrition[data.Attrition == 'No'] = 0
__main__:1: SettingWithCopyWarning: 
A value is trying to be set on a copy of a slice from a DataFrame

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

print(data)
      Age Attrition  ... YearsSinceLastPromotion YearsWithCurrManager
0      51         0  ...                       0                    0
1      31         1  ...                       1                    4
2      32         0  ...                       0                    3
3      38         0  ...                       7                    5
4      32         0  ...                       0                    4
  ...       ...  ...                     ...                  ...
4405   42         0  ...                       0                    2
4406   29         0  ...                       0                    2
4407   25         0  ...                       1                    2
4408   42         0  ...                       7                    8
4409   40         0  ...                       3                    9

[4410 rows x 24 columns]

data.columns
Out[8]: 
Index(['Age', 'Attrition', 'BusinessTravel', 'Department', 'DistanceFromHome',
       'Education', 'EducationField', 'EmployeeCount', 'EmployeeID', 'Gender',
       'JobLevel', 'JobRole', 'MaritalStatus', 'MonthlyIncome',
       'NumCompaniesWorked', 'Over18', 'PercentSalaryHike', 'StandardHours',
       'StockOptionLevel', 'TotalWorkingYears', 'TrainingTimesLastYear',
       'YearsAtCompany', 'YearsSinceLastPromotion', 'YearsWithCurrManager'],
      dtype='object')



from scipy.stats import pearsonr

s,p= pearsonr(data.Attrition,data.Education)

print(s,p)
-0.015111167710968711 0.3157293177118575

s,p= pearsonr(data.Attrition,data.DistanceFromHome)

print(s,p)
-0.00973014101017966 0.5182860428050771


s,p= pearsonr(data.Attrition,data.EmployeeID)

print(s,p)
-0.004729122995066087 0.7535487401886252

s,p= pearsonr(data.Attrition,data.JobLevel)

print(s,p)
-0.010289713287495035 0.49451717271828405

s,p= pearsonr(data.Attrition,data.MonthlyIncome)

print(s,p)
-0.031176281698115007 0.03842748490600132

s,p= pearsonr(data.Attrition,data.PercentSalaryHike)

print(s,p)
0.03253259489105351 0.030743386433355353

s,p= pearsonr(data.Attrition,data.StockOptionLevel)

print(s,p)
-0.006838852403261521 0.6498072937475723

s,p= pearsonr(data.Attrition,data.TrainingTimesLastYear)

print(s,p)
-0.04943057624425501 0.0010247061915362814

s,p= pearsonr(data.Attrition,data.YearsAtCompany)

print(s,p)
-0.1343922139899772 3.1638831224877484e-19

s,p= pearsonr(data.Attrition,data.YearsSinceLastPromotion)

print(s,p)
-0.03301877514258434 0.028330336189396753

s,p= pearsonr(data.Attrition,data.YearsWithCurrManager)

print(s,p)
-0.15619931590162842 1.7339322652900218e-25