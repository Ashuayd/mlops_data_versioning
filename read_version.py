import argparse
import pandas as pd
import dvc.api

def main(version):
    path = 'data/wine_original.csv'
    repo = r'C:\Users\DELL\dsti-mlops-2024-spring\data_versioning'

    # Construct the URL for the specified version
    data_url = dvc.api.get_url(
        path=path,
        repo=repo,
        rev=version  # Specify the version here
    )

    data = pd.read_csv(data_url, sep=";")
    print(data)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Access a specific version of the dataset.')
    parser.add_argument('version', type=str, help='Version of the dataset to access (e.g., v2)')
    args = parser.parse_args()

    main(args.version)
