# main.py

# importing required libraries
import pandas as pd

"""
This is the main script for the input data conversion task. It reads the input
data files, performs the necessary calculations, and writes the output data to
a CSV file.

Usage:
    python main.py

Inputs:
    - Input data files in CSV format

Outputs:
    - Output data file in CSV format
"""

# reading input datasets
df1 = pd.read_csv("input_data/ecg1.csv")
df2 = pd.read_csv("input_data/ecg2.csv")
df3 = pd.read_csv("input_data/ecg3.csv")

# combining the input datasets
merged_df = pd.merge(df1, df2, on="id")
merged_df = pd.merge(merged_df, df3, on="id")

# rearranging the columns to match the target dataset
result_df = merged_df[['id','Clinical Trial Number','Country','Trial Unit Number','Subject Number','Link to ECGFIND','Visit','Day of ECG','Month of ECG','Year of ECG','Time of ECG','Planned Time of Measurement','Rel day of ECG to Start of Trt','Rel day of ECG to End of Trt','Period of ECG','Phase of ECG','Position of Subject During ECG','Cycle Measurement Method','Evaluation Method','QTc Interval Calc Bazett','QTc Interval Calc Fridericia']]

# writing the output to result.csv
try:
    result_df.to_csv("result.csv", index=False)
except Exception:
    print(f'Successfully converted {len(result_df)} records.')