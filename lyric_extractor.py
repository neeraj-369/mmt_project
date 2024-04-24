import csv
import re
import os
from lyrics_extractor import SongLyrics

# Function to clean lyrics
def clean_lyrics(lyrics):
    clean_lyrics = re.sub(r'\\', '', lyrics)  # Remove \
    clean_lyrics = re.sub(r'\[.*?\]', '', clean_lyrics)  # Remove [words]
    clean_lyrics = re.sub(r'\(.*?\)', '', clean_lyrics)  # Remove (words)
    clean_lyrics = re.sub(r'\n', ' ', clean_lyrics)  # Replace \n with space
    clean_lyrics = re.sub(r'-', ' ', clean_lyrics)  # Replace - with space
    clean_lyrics = re.sub(r'[",?]', '', clean_lyrics)  # Remove quotations, commas, and question marks
    clean_lyrics = re.sub(r'[!@#$%^&*]', '', clean_lyrics)  # Remove symbols like &, @, #, $, !, *, &
    return clean_lyrics

# API credentials
GCS_API_KEY = 'AIzaSyBZXK8xuBIpz7-FIVHSnKwUBWYd0SW418o'
GCS_ENGINE_ID = '435b5ae2d51ff4a50'
extract_lyrics = SongLyrics(GCS_API_KEY, GCS_ENGINE_ID)

# Open CSV file and iterate over each song
# Define a function to process lyrics for a given CSV file
def process_lyrics(csv_path, output_path):
    with open(csv_path, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip header row
        with open(output_path, "w") as all_lyrics_file:
            for row in csv_reader:
                song_name = row[0]  # Assuming the song name is in the first column of the CSV
                data = extract_lyrics.get_lyrics(song_name)
                if data:
                    lyrics = data["lyrics"]
                    clean_lyrics_str = clean_lyrics(lyrics)
                    all_lyrics_file.write(f"{clean_lyrics_str}\n")
                    print(f"Lyrics for '{song_name}' appended to '{output_path}'")

# Iterate over directories sample1 to sample46
for i in range(1, 47):
    directory_name = f"sample{i}"
    csv_path = os.path.join(directory_name, "songs.csv")
    output_path = os.path.join(directory_name, "all_lyrics.txt")
    
    # Check if the directory and CSV file exist
    if os.path.exists(csv_path):
        print(f"Processing {csv_path}...")
        process_lyrics(csv_path, output_path)
    else:
        print(f"Directory or CSV file not found: {csv_path}")