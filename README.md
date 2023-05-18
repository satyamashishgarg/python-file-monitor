# python-file-moonitor
Basic file integrity monitor coded in Python: Monitored a specific directory for any changes in the files
USAGE:
This code first defines a get_file_hash function that calculates the SHA-256 hash of a file. It then defines a monitor_directory function that initializes a dictionary of file hashes for all files in the specified directory, and then enters an infinite loop that checks for any changes in the files every 5 seconds. If a file's hash has changed, it prints a message indicating that the file has been modified.

To use this code, simply call the monitor_directory function with the path to the directory you want to monitor. Note that this code only monitors files within the specified directory and does not detect any changes to subdirectories.
