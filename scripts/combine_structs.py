import os
import json

# Define the folder names
folders = ["structs"]

# Loop through each folder
for folder in folders:
    # Create an empty dictionary to store combined JSON data
    combined_data = {}

    # Get the list of JSON files in the folder
    json_files = [file for file in os.listdir(folder) if file.endswith(".json")]

    # Loop through each JSON file in the folder
    for json_file in json_files:
        file_path = os.path.join(folder, json_file)
        
        # Read the JSON data from the file
        with open(file_path, "r") as file:
            data = json.load(file)
        
        # Merge the data into the combined_data dictionary
        for key, value in data.items():
            if key in combined_data and isinstance(value, dict) and isinstance(combined_data[key], dict):
                # Merge dictionaries with the same key
                combined_data[key].update(value)
            else:
                # If the key is unique, add it to combined_data
                combined_data[key] = value

    # Define the output JSON file path for the folder
    output_file_path = os.path.join(folder, f"{folder}.json")

    # Write the combined JSON data to the output file
    with open(output_file_path, "w") as output_file:
        json.dump(combined_data, output_file, indent=4)

    print(f"Combined JSON file saved for {folder}: {output_file_path}")
