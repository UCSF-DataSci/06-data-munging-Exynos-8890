import pandas as pd
import numpy as np
from scipy import stats

def print_info(dirty: pd.DataFrame):
    print("## info() \n ")
    print(dirty.info(),"\n")
    print("## describe() \n", dirty.describe(),"\n")
    print("## head() \n",dirty.head())
    print()
    print("## na nubmer: \n",dirty.isna().sum())
    print()
    print("## duplicated: \n",dirty.duplicated().sum())
    print()
    # value_counts() for each column
    print("## value_counts: \n")
    for col in dirty.columns:
        print(dirty[col].value_counts())
    print("\n\n")

dirty = pd.read_csv('messy_population_data.csv')
print("# dirty data \n")
print_info(dirty)

clean = dirty.copy()
clean = clean.drop_duplicates().dropna().reset_index(drop=True)
clean = clean[clean['year'] < 2024]

z_scores = np.abs(stats.zscore(clean['population']))
print("z_scores out of 3: ", (z_scores > 3).sum(),"\n")
clean = clean[(z_scores < 3)]

clean['year'] = pd.to_datetime(clean['year'], format='%Y')

print("# clean data \n")
print_info(clean)
