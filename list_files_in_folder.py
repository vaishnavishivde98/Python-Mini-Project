import os  # Importing os module to interact with the file system

# Function to list files in a given folder
def list_files_in_folder(folder_path):
    try:
        # os.listdir() returns a list of all files and folders in the given path
        files = os.listdir(folder_path)
        return files, None  # Return files and no error
    except FileNotFoundError:
        # If the folder path does not exist
        return None, "Folder not found"
    except PermissionError:
        # If the program does not have permission to access the folder
        return None, "Permission denied"

# Main function where program execution starts
def main():
    # Taking input from user: multiple folder paths separated by spaces
    folder_paths = input("Enter a list of folder paths separated by spaces: ").split()
    
    # Loop through each folder path entered by the user
    for folder_path in folder_paths:
        # Call the function to get files or error
        files, error_message = list_files_in_folder(folder_path)
        
        if files:
            # If files are found, print them
            print(f"Files in {folder_path}:")
            for file in files:
                print(file)
        else:
            # If there is an error, print the error message
            print(f"Error in {folder_path}: {error_message}")

# This ensures the script runs only when executed directly (not when imported)
if __name__ == "__main__":
    main()
