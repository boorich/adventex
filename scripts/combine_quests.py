import os
import json

# Define the folder names
folders = ["quests"]

# Specify the output folder
output_folder = "gpt-docs"

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Loop through each folder
for folder in folders:
    # Create an empty list to store combined quest JSON data
    combined_quest_data = []

    # Get the list of JSON files in the folder
    json_files = [file for file in os.listdir(folder) if file.endswith(".json")]

    # Loop through each JSON file in the folder
    for json_file in json_files:
        file_path = os.path.join(folder, json_file)

        # Read the JSON data from the file
        with open(file_path, "r") as file:
            data = json.load(file)

        # Check if the data is a dictionary with "quests" key
        if isinstance(data, dict) and "quests" in data:
            # Extract the list of quests
            quests = data["quests"]

            # Extend the combined_quest_data list with the quests
            combined_quest_data.extend(quests)
        else:
            # If the file doesn't have quests, print a warning
            print(f"Warning: File {file_path} does not contain quests and will be skipped.")

    # Define the output JSON file path in the "gpt-docs" folder
    output_file_path = os.path.join(output_folder, f"{folder}.json")

    # Write the combined quest JSON data to the output file
    with open(output_file_path, "w") as output_file:
        json.dump(combined_quest_data, output_file, indent=4)

    print(f"Combined JSON file saved for {folder}: {output_file_path}")
