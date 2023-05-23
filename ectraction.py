import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def try01():
    # Read in the CSV file
    df = pd.read_csv('data1.csv')

    count = df.groupby('Entity')['Entity'].count()
    print(count)

if __name__ == '__main__':
    try01()
    print("manos")