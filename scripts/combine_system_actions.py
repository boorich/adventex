import os
import json

# Define the folder containing JSON files
folder_path = "./system_actions"

# Initialize an empty dictionary to store the merged data
merged_data = {}

# Loop through all files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith(".json"):
        file_path = os.path.join(folder_path, filename)

        # Read the JSON data from the file
        with open(file_path, "r") as file:
            json_data = json.load(file)

        # Merge the data into the merged_data dictionary, eliminating duplicates
        for key, value in json_data.items():
            if key not in merged_data:
                merged_data[key] = value
            elif isinstance(value, list) and isinstance(merged_data[key], list):
                # Merge lists of dictionaries based on the "name" field
                for item in value:
                    if item not in merged_data[key]:
                        merged_data[key].append(item)

# Convert the merged_data dictionary to a JSON string
merged_json = json.dumps(merged_data, indent=2)

# Save the merged JSON to a file
output_file = "merged_output.json"
with open(output_file, "w") as outfile:
    outfile.write(merged_json)

print(f"Merged JSON data saved to {output_file}")
