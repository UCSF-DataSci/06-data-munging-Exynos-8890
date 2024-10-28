# Data Cleaning Project: Population Dataset

## 1. Initial State Analysis

### Dataset Overview
- **Name**: messy_population_data.csv
- **Rows**: 125718
- **Columns**: 5

### Column Details

| #   | Column         | Non-Null Count | NA Count | Dtype   |
| --- | -------------- | ---------------| -------- | ------- |
| 0   | income_groups  | 119412         | 6306     | object  |
| 1   | age            | 119495         | 6223     | float64 |
| 2   | gender         | 119811         | 5907     | float64 |
| 3   | year           | 119516         | 6202     | float64 |
| 4   | population     | 119378         | 6340     | float64 |

### Summary Statistics

|       | age       | gender    | year    | population  |
|-------|-----------|-----------|---------|-------------|
| count | 119495    | 119811    | 119516  | 119378      |
| mean  | 50.007    | 1.579     | 2025.068| 111298300   |
| std   | 29.154    | 0.591     | 43.585  | 1265205000  |
| min   | 0         | 1         | 1950    | 21          |
| 25%   | 25        | 1         | 1987    | 2316023     |
| 50%   | 50        | 2         | 2025    | 7145754     |
| 75%   | 75        | 2         | 2063    | 14663880    |
| max   | 100       | 3         | 2119    | 32930430000 |

### Identified Issues

- missing values in all columns
- duplicated rows
- incorrect data types in year column
- outliers in population and year columns

## 2. Data Cleaning Process

Issue 1: Duplicate Records
- Cleaning Method: Remove duplicate rows using drop_duplicates()
- Implementation: `clean = clean.drop_duplicates()`
- Justification: Duplicate records can skew analysis and statistics. Since there's no indication that duplicates serve any purpose in this dataset, complete removal is the safest approach.
- Impact:
  - Rows affected: Number shown in `dirty.duplicated().sum()`
  - Data distribution change: No change to data distribution as duplicates are exact copies

Issue 2: Missing Values
- Cleaning Method: Remove rows with any null values using dropna()
- Implementation: `clean = clean.dropna()`
- Justification: Given the small number of columns and importance of each feature for population analysis, rows with missing data would be incomplete for any meaningful analysis
- Impact:
  - Rows affected: Sum of missing values shown in `dirty.isna().sum()`
  - Data distribution change: Potential slight change in distribution depending on pattern of missing values

Issue 3: Future Year Data
- Cleaning Method: Filter out records with years beyond 2024
- Implementation: `clean = clean[clean['year'] <= 2024]`
- Justification: Since current year is 2024, any population data for future years would be projections rather than actual data and should be excluded for accurate historical analysis
- Impact:
  - Rows affected: Records with year > 2024
  - Data distribution change: Removes potential speculative future data

Issue 4: Outlier Detection and Removal
- Cleaning Method: Remove statistical outliers using z-score method
- Implementation: `z_scores = np.abs(stats.zscore(clean['population']))` and `clean = clean[(z_scores < 3)]`
- Justification: 
  - Uses 3 standard deviations as threshold (99.7% of normal distribution)
  - Z-score method is appropriate for population data which often follows roughly normal distribution
  - Helps remove extreme values that could be data entry errors
- Impact:
  - Rows affected: Shown in `(z_scores > 3).sum()`
  - Data distribution change: More normalized population distribution with extreme values removed

Issue 5: Date Format Standardization
- Cleaning Method: Convert year column to datetime format
- Implementation: `clean['year'] = pd.to_datetime(clean['year'], format='%Y')`
- Justification: Standardizing date format ensures proper chronological ordering and enables time-based operations
- Impact:
  - Rows affected: All rows
  - Data distribution change: No change to distribution, only format standardization

## 3. Final State Analysis

### Dataset Overview
- **Name**: cleaned_population_data.csv
- **Rows**: 46990
- **Columns**: 5

### Column Details

| #   | Column         | Non-Null Count | Dtype          |
| --- | -------------- | -------------- | -------------- |
| 0   | income_groups  | 46990          | object         |
| 1   | age            | 46990          | float64        |
| 2   | gender         | 46990          | float64        |
| 3   | year           | 46990          | datetime64[ns] |
| 4   | population     | 46990          | float64        |

### Summary statistics

| Statistic | Age | Gender | Year | Population |
|-----------|-----|--------|------|------------|
| count | 46,990.000000 | 46,990.000000 | 46,990 | 4.699000e+04 |
| mean | 50.115705 | 1.580570 | 1987-01-12 17:14:23.111300224 | 1.676369e+07 |
| min | 0.000000 | 1.000000 | 1950-01-01 00:00:00 | 2.200000e+01 |
| 25% | 25.000000 | 1.000000 | 1968-01-01 00:00:00 | 8.480102e+05 |
| 50% | 50.000000 | 2.000000 | 1987-01-01 00:00:00 | 4.374134e+06 |
| 75% | 75.000000 | 2.000000 | 2006-01-01 00:00:00 | 8.324320e+06 |
| max | 100.000000 | 3.000000 | 2024-01-01 00:00:00 | 3.173332e+09 |
| std | 29.185784 | 0.591614 | NaN | 1.294103e+08 |