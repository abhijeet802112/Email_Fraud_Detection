import pandas as pd


data = pd.read_csv('data/emails.csv')


print("Dataset Preview:")
print(data.head())


print("\nLabel Count:")
print(data['label'].value_counts())
