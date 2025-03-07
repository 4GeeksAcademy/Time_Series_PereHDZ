import pandas as pd

url = "https://raw.githubusercontent.com/4GeeksAcademy/alternative-time-series-project/main/sales.csv"

df = pd.read_csv(url)

df.to_csv('sales.csv', index=False)
print("Dataset saved as 'sales.csv'")