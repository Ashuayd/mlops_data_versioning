

import pandas as pd
import dvc.api

path = 'data/wine_original.csv'
repo = r'C:\Users\DELL\dsti-mlops-2024-spring\data_versioning'

data_url = dvc.api.get_url(
    path=path,
    repo=repo
)

data = pd.read_csv(data_url, sep=";")
print(data)
