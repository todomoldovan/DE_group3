import json
objects = 500000
# Function to read the first 15 JSON objects from a file
def read_first_json_objects(file_path, objects):
    json_objects = []
    with open(file_path, 'r') as file:
        for i, line in enumerate(file):
            if i >= objects:  # Stop after reading 15 lines
                break
            try:
                json_object = json.loads(line)
                json_objects.append(json_object)
            except json.JSONDecodeError:
                continue  # Handle possible JSON decode error (malformed JSON)
    return json_objects

# Replace '/path/to/your/json/file.json' with the actual path to your JSON file
json_file_path = 'corpus-webis-tldr-17.json'
first_objects = read_first_json_objects(json_file_path)

# Assuming you have the list of first 15 JSON objects in 'first_15_objects'
def write_json_objects_to_file(json_objects, output_file_path):
    with open(output_file_path, 'w') as outfile:
        for obj in json_objects:
            json.dump(obj, outfile)
            outfile.write('\n')  # Write each JSON object on a new line

# Example usage:
output_file_path = 'objects.json'  # Specify your output file path here
# first_15_objects = read_first_15_json_objects('/path/to/your/json/file.json')  # Load your objects
write_json_objects_to_file(first_objects, output_file_path)

