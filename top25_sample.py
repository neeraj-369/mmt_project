import pandas as pd
import os
import pandas as pd

# Read the CSV file
df = pd.read_csv('/Users/akashvallamsetty/Desktop/mmt project/top_categories.csv')

# Extract column names excluding the first column
column_names = df.columns.tolist()[1:]

# Print column names
print(column_names)
# Define the path to the sample folders
sample_folder_path = '/Users/akashvallamsetty/Desktop/mmt project/data/calc'

# Loop over each sample folder
for folder_name in os.listdir(sample_folder_path):
    folder_path = os.path.join(sample_folder_path, folder_name)
    
    # Check if the folder contains an analysis.csv file
    analysis_file_path = os.path.join(folder_path, 'analysis.csv')
    if os.path.isfile(analysis_file_path):
        # Read the CSV file
        df = pd.read_csv(analysis_file_path)
        # Filter rows based on category attribute
        df_filtered = df[df['Category'].isin(column_names)]

        # Continue with the rest of the code using the filtered dataframe
        # Save the filtered dataframe as a CSV file
        filtered_file_path = os.path.join(folder_path, 'filteredanalysis.csv')
        df_filtered.to_csv(filtered_file_path, index=False)
