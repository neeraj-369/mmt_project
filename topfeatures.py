import pandas as pd
csv_file_path = '/Users/akashvallamsetty/Desktop/mmtproject/empath_results.csv'
df = pd.read_csv(csv_file_path)

category_data = df.drop('Filename', axis=1)
category_means = category_data.mean()

sorted_categories = category_means.sort_values(ascending=False)

top_categories = sorted_categories.head(25)
print("Top 25 Categories:")
print(top_categories)
