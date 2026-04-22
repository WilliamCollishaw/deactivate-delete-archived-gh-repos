import json
import sys


def write_json_to_file(data, file_path):
    """Write JSON data to a file."""
    try:
        with open(file_path, "w") as json_file:
            json.dump(data, json_file, indent=4)
        print(f"Data successfully written to {file_path}")
    except OSError as e:
        sys.exit(f"Error writing to {file_path}: {e}")
