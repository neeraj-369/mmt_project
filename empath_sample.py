from empath import Empath
import codecs
import os
import csv

# Create an instance of Empath
lexicon = Empath()

# Function to read text from the file
def read_text_file(file_path):
    with codecs.open(file_path, "r", "utf-8") as file:
        return file.read()

# Function to analyze text with Empath
def analyze_text(text):
    # Analyze the text and store the results
    analysis = lexicon.analyze(text, normalize=True)
    return analysis

# Root directory path
base_directory_path = "/Users/akashvallamsetty/Desktop/mmt project/data/calc"

# Iterate through each sample folder
for i in range(1, 47):
    folder_name = f"sample{i}"
    directory_path = os.path.join(base_directory_path, folder_name)

    # Text file path in each folder
    text_file_path = os.path.join(directory_path, "all_lyrics.txt")
    if not os.path.exists(text_file_path):
        print(f"File not found: {text_file_path}")
        continue

    # Read and analyze text
    text = read_text_file(text_file_path)
    results = analyze_text(text)

    # CSV file to save the results in the same folder
    csv_file_path = os.path.join(directory_path, "analysis.csv")

    # Collect all unique categories from analysis results
    all_categories = sorted(results.keys())

    # Write analysis results to CSV
    with open(csv_file_path, mode='w', newline='', encoding='utf-8') as file:
        csv_writer = csv.writer(file)
        # Writing the header of the CSV
        csv_writer.writerow(['Category', 'Value'])
        # Write each category and its corresponding value
        for category in all_categories:
            csv_writer.writerow([category, results[category]])

    print(f"Analysis complete for {folder_name}. Results have been saved to: {csv_file_path}")
    
   