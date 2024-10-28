# dirty data 

## info() 
 
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 125718 entries, 0 to 125717
Data columns (total 5 columns):
 #   Column         Non-Null Count   Dtype  
---  ------         --------------   -----  
 0   income_groups  119412 non-null  object 
 1   age            119495 non-null  float64
 2   gender         119811 non-null  float64
 3   year           119516 non-null  float64
 4   population     119378 non-null  float64
dtypes: float64(4), object(1)
memory usage: 4.8+ MB
None 

## describe() 
                  age         gender           year    population
count  119495.000000  119811.000000  119516.000000  1.193780e+05
mean       50.007038       1.578578    2025.068049  1.112983e+08
std        29.154144       0.590559      43.584951  1.265205e+09
min         0.000000       1.000000    1950.000000  2.100000e+01
25%        25.000000       1.000000    1987.000000  2.316023e+06
50%        50.000000       2.000000    2025.000000  7.145754e+06
75%        75.000000       2.000000    2063.000000  1.466388e+07
max       100.000000       3.000000    2119.000000  3.293043e+10 

## head() 
   income_groups  age  gender    year  population
0   high_income  0.0     1.0  1950.0   7798286.0
1   high_income  0.0     1.0  1951.0   7739711.0
2   high_income  0.0     3.0  1952.0   7713905.0
3   high_income  0.0     1.0  1953.0   7722053.0
4   high_income  0.0     1.0  1954.0   7756149.0

## na nubmer: 
 income_groups    6306
age              6223
gender           5907
year             6202
population       6340
dtype: int64

## duplicated: 
 2950

## value_counts: 

income_groups
low_income                  28433
upper_middle_income         28354
high_income                 28343
lower_middle_income         28323
lower_middle_income_typo     1517
low_income_typo              1505
high_income_typo             1475
upper_middle_income_typo     1462
Name: count, dtype: int64
age
31.0    1211
12.0    1205
30.0    1202
91.0    1202
53.0    1201
        ... 
42.0    1167
71.0    1167
78.0    1164
21.0    1163
58.0    1160
Name: count, Length: 101, dtype: int64
gender
1.0    56777
2.0    56748
3.0     6286
Name: count, dtype: int64
year
2002.0    808
2054.0    808
1974.0    808
2057.0    807
2055.0    807
         ... 
2101.0      2
2108.0      2
2117.0      1
2102.0      1
2118.0      1
Name: count, Length: 169, dtype: int64
population
104.0        6
546.0        5
454.0        5
105.0        5
143.0        5
            ..
2187279.0    1
2115967.0    1
2087208.0    1
2072039.0    1
7775405.0    1
Name: count, Length: 114925, dtype: int64



z_scores out of 3:  293 

# clean data 

## info() 
 
<class 'pandas.core.frame.DataFrame'>
Index: 46373 entries, 0 to 95380
Data columns (total 5 columns):
 #   Column         Non-Null Count  Dtype         
---  ------         --------------  -----         
 0   income_groups  46373 non-null  object        
 1   age            46373 non-null  float64       
 2   gender         46373 non-null  float64       
 3   year           46373 non-null  datetime64[ns]
 4   population     46373 non-null  float64       
dtypes: datetime64[ns](1), float64(3), object(1)
memory usage: 2.1+ MB
None 

## describe() 
                 age        gender                           year    population
count  46373.000000  46373.000000                          46373  4.637300e+04
mean      50.105686      1.580467  1986-07-17 01:38:26.195415360  1.684849e+07
min        0.000000      1.000000            1950-01-01 00:00:00  2.200000e+01
25%       25.000000      1.000000            1968-01-01 00:00:00  8.361420e+05
50%       50.000000      2.000000            1987-01-01 00:00:00  4.333649e+06
75%       75.000000      2.000000            2005-01-01 00:00:00  8.283864e+06
max      100.000000      3.000000            2023-01-01 00:00:00  3.173332e+09
std       29.191482      0.591477                            NaN  1.302569e+08 

## head() 
   income_groups  age  gender       year  population
0   high_income  0.0     1.0 1950-01-01   7798286.0
1   high_income  0.0     1.0 1951-01-01   7739711.0
2   high_income  0.0     3.0 1952-01-01   7713905.0
3   high_income  0.0     1.0 1953-01-01   7722053.0
4   high_income  0.0     1.0 1954-01-01   7756149.0

## na nubmer: 
 income_groups    0
age              0
gender           0
year             0
population       0
dtype: int64

## duplicated: 
 0

## value_counts: 

income_groups
low_income                  11092
upper_middle_income         10990
lower_middle_income         10947
high_income                 10938
upper_middle_income_typo      621
low_income_typo               609
lower_middle_income_typo      589
high_income_typo              587
Name: count, dtype: int64
age
34.0    482
93.0    481
45.0    481
73.0    481
94.0    480
       ... 
55.0    441
35.0    439
71.0    438
51.0    434
18.0    432
Name: count, Length: 101, dtype: int64
gender
2.0    21988
1.0    21920
3.0     2465
Name: count, dtype: int64
year
1988-01-01    654
1999-01-01    654
2013-01-01    650
2014-01-01    647
1981-01-01    645
             ... 
2015-01-01    610
2008-01-01    604
1963-01-01    602
1972-01-01    601
1958-01-01    596
Name: count, Length: 74, dtype: int64
population
104.0        5
143.0        5
546.0        5
189.0        5
454.0        4
            ..
852494.0     1
871684.0     1
891783.0     1
912499.0     1
7775405.0    1
Name: count, Length: 45626, dtype: int64


