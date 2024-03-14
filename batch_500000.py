import json
import os

def process_json_objects_in_batches(file_path, output_file_path, batch_size=10000, total_limit=500000):
    batch = []
    last_processed_index = 0
    
    # Check if a checkpoint exists to resume from
    if os.path.exists(output_file_path):
        with open(output_file_path, 'r') as outfile:
            for i, line in enumerate(outfile):
                pass
            last_processed_index = i + 1  # Assuming one JSON object per line in the output file

    with open(file_path, 'r') as file:
        for i, line in enumerate(file):
            if i < last_processed_index:
                continue  # Skip already processed lines
            if i >= total_limit:  # Stop after processing total_limit lines
                break
            
            try:
                json_object = json.loads(line)
                batch.append(json_object)
            except json.JSONDecodeError:
                continue  # Handle possible JSON decode error (malformed JSON)
            
            # If the batch size is reached, write the batch to the output file
            if len(batch) == batch_size:
                write_json_objects_to_file(batch, output_file_path, mode='a')  # Append mode
                batch = []  # Reset the batch
                
                print(f"Processed and wrote batch ending at index {i}")
    
    # Write any remaining objects after the loop finishes
    if batch:
        write_json_objects_to_file(batch, output_file_path, mode='a')  # Append mode
        print(f"Processed and wrote final batch ending at index {i}")

def write_json_objects_to_file(json_objects, output_file_path, mode='w'):
    with open(output_file_path, mode) as outfile:
        for obj in json_objects:
            json.dump(obj, outfile)
            outfile.write('\n')  # Write each JSON object on a new line

json_file_path = 'corpus-webis-tldr-17.json'
output_file_path = 'processed_objects40k.json'

# Start processing in batches with a specified total limit
process_json_objects_in_batches(json_file_path, output_file_path, batch_size=10000, total_limit=40000)

