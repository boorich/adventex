import os
import json

# Define the folder names
folders = ["player_actions"]

# Specify the output folder
output_folder = "gpt-docs"

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Loop through each folder
for folder in folders:
    # Create an empty list to store combined JSON data
    combined_data = []

    # Get the list of JSON files in the folder
    json_files = [file for file in os.listdir(folder) if file.endswith(".json")]

    # Loop through each JSON file in the folder
    for json_file in json_files:
        file_path = os.path.join(folder, json_file)

        # Read the JSON data from the file
        with open(file_path, "r") as file:
            data = json.load(file)

        # Append the data to the combined_data list
        combined_data.append(data)

    # Define the output JSON file path in the "gpt-docs" folder
    output_file_path = os.path.join(output_folder, f"{folder}.json")

    # Write the combined JSON data to the output file as an array of standalone objects
    with open(output_file_path, "w") as output_file:
        json.dump(combined_data, output_file, indent=4)

    print(f"Combined JSON file saved for {folder}: {output_file_path}")
