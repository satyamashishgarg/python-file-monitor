import hashlib
import os
import time

def get_file_hash(file_path):
    """
    Calculates and returns the SHA-256 hash of a file.
    """
    with open(file_path, 'rb') as f:
        file_data = f.read()
    return hashlib.sha256(file_data).hexdigest()

def monitor_directory(directory_path):
    """
    Monitors the specified directory for any changes in the files.
    """
    file_hashes = {}
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)
        if os.path.isfile(file_path):
            file_hashes[file_path] = get_file_hash(file_path)
    
    while True:
        for filename in os.listdir(directory_path):
            file_path = os.path.join(directory_path, filename)
            if os.path.isfile(file_path):
                current_hash = get_file_hash(file_path)
                if file_hashes.get(file_path) != current_hash:
                    print(f"File '{filename}' has been modified!")
                    file_hashes[file_path] = current_hash
        
        time.sleep(5)

# Example usage:
monitor_directory('/path/to/directory/to/monitor')
