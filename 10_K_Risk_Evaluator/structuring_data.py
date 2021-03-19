#Authors: Nicholas Mosca, Evie Wan, Eric South


''' Steps for this Script 

1. generate lists of file paths for 2019 and 2020 versions

2. extract ticker from each path for dict key (list)

3. run list through html parser and save outputs to list for sort_values

4. Create Dict of Ticker: html parser result  for 2019 and 2020 versions

5. Convert to pandas DF

6. Write to csv 

''' 

from pathlib import Path
import pandas as pd
from html_parser import *
from bulk_10k_extraction import local_location # Example: /Users/nick/Documents/cs506/project
from path_mover import file_paths 

# list of file paths as strings 

Paths_2019 = file_paths(2019) # 170
Paths_2020 = file_paths(2020) # 111

#extracting tickers to list 

Ticker_2019 = []
Ticker_2020 = []

for p19 in Paths_2019:
    Ticker_2019.append(p19[54:58])

for p20 in Paths_2020:
    Ticker_2020.append(p20[54:58])


# grabbing html parser outputs new function = main_path

#2019
Risk_2019 = []

for x in Paths_2019:
    Risk_2019.append(main_path((x)))


#2020

Risk_2020 = []

for x2 in Paths_2020:
    Risk_2020.append(main_path(x2))


#converting to Dictionary

Dict_2019 = dict(zip(Ticker_2019,Risk_2019))
Dict_2020 = dict(zip(Ticker_2020,Risk_2020))


DF_2019 = pd.DataFrame.from_dict(Dict_2019,orient= 'index', columns= ['Risk Text'])
DF_2020 = pd.DataFrame.from_dict(Dict_2020, orient= 'index', columns = ['Risk Text'])

#write to csv

DF_2019.to_csv('10k_2019.csv')
DF_2020.to_csv('10k_2020.csv')