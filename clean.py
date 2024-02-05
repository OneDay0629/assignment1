import numpy as np
import pandas as pd
def clean(input1, input2,output):
    contact = pd.read_csv(input1)
    other = pd.read_csv(input2)
    combine = pd.merge(contact, other, left_on='respondent_id', right_on='id').drop('respondent_id', axis=1)
    combine = combine.dropna()
    check_job = combine['job'].str.contains('insurance|Insurance')
    combine = combine[~check_job]
    print(combine.shape)

    return combine


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('input1', help='Data file (CSV)')
    parser.add_argument('input2', help='Data file (CSV)')
    parser.add_argument('output', help='Cleaned data file (CSV)')
    args = parser.parse_args()

    cleaned = clean(args.input1,args.input2,args.output)
    cleaned.to_csv(args.output, index=False)