import json
import pandas as pd
import random
import os
import shutil

# Read test.csv
dataset = pd.read_csv('test.csv')

# Create dictionary to map types to row indices
type_row_dict = {}

# For each row in dataset, append the row number to type_row_dict[type]
for idx, row in dataset.iterrows():
    row_type = row['type']
    if row_type not in type_row_dict:
        type_row_dict[row_type] = []
    type_row_dict[row_type].append(idx)

# Construct subset: randomly sample 200 QAs per type
sampled_indices = []
for row_type, indices in type_row_dict.items():
    # If there are fewer than 200 rows of this type, take all of them
    # Otherwise, randomly sample 200
    if len(indices) <= 200:
        sampled_indices.extend(indices)
    else:
        sampled_indices.extend(random.sample(indices, 200))

random.shuffle(sampled_indices)

# Create the subset dataframe
subset = dataset.iloc[sampled_indices].reset_index(drop=True)

# Save the subset to NExTVideo.csv
subset.to_csv('NExTVideo.csv', index=False)
print(f"Saved subset with {len(subset)} rows to NExTVideo.csv")

# Load the mapping dictionary
with open('map_vid_vidorID.json', 'r') as fp:
    map_dict = json.load(fp)

# Extract video_ids from the "video" field of the dataset
# Ensure they are strings
video_ids = [str(video_id) for video_id in subset['video'].tolist()]

# Get corresponding files from mapping
files = []
for vid in video_ids:
    if vid in map_dict:
        files.append(map_dict[vid])
    else:
        print(f"Warning: Video ID {vid} not found in mapping dictionary")

# Create output directory if it doesn't exist
os.makedirs('videos', exist_ok=True)

# Copy files from source to destination with new names
for i in range(len(files)):
    source_path = os.path.join('NExTVideo', files[i] + '.mp4')
    dest_path = os.path.join('videos', f"{video_ids[i]}.mp4")
    
    try:
        shutil.copy2(source_path, dest_path)
        print(f"Copied {source_path} to {dest_path}")
    except FileNotFoundError:
        print(f"Error: Could not find source file {source_path}")
    except Exception as e:
        print(f"Error copying {source_path} to {dest_path}: {str(e)}")

print("Processing complete")