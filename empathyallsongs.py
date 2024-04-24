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

# Directory containing all the song files
directory_path = "/Users/akashvallamsetty/Desktop/mmt project/allsongs"

# List all files in the directory
files = [f for f in os.listdir(directory_path) if f.endswith('.txt')]

# Collect all unique categories from all files for headers
all_categories = set()
for filename in files:
    file_path = os.path.join(directory_path, filename)
    text = read_text_file(file_path)
    results = analyze_text(text)
    all_categories.update(results.keys())

# Convert set to sorted list
all_categories = sorted(all_categories)

# CSV file to store the results
csv_file_path = "/Users/akashvallamsetty/Desktop/mmt project/empath_results.csv"

# Open the CSV file for writing
with open(csv_file_path, mode='w', newline='', encoding='utf-8') as file:
    csv_writer = csv.writer(file)
    # Writing the header of the CSV
    csv_writer.writerow(['Filename'] + all_categories)

    # Iterate over each file in the directory and write analysis results
    for filename in files:
        file_path = os.path.join(directory_path, filename)
        text = read_text_file(file_path)
        results = analyze_text(text)

        # Create a row with filename and then category values
        row = [filename] + [results.get(category, 0) for category in all_categories]
        csv_writer.writerow(row)

print("Analysis complete. Results have been saved to:", csv_file_path)
