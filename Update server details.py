def update_server_config(file_path, key, value):
    """
    Update a specific configuration key in the server.conf file.

    :param file_path: Path to the configuration file
    :param key: Configuration key to update (e.g., MAX_CONNECTIONS)
    :param value: New value to set for the key
    """
    
    # Read all lines from the configuration file
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Open the file again in write mode to update content
    with open(file_path, 'w') as file:
        for line in lines:
            # Strip whitespace for accurate comparison
            stripped_line = line.strip()

            # Check if the line starts with the exact key followed by '='
            if stripped_line.startswith(f"{key}="):
                # Replace with updated key-value pair
                file.write(f"{key}={value}\n")
            else:
                # Write the original line if it doesn't match
                file.write(line)


# Path to the server configuration file
server_config_file = 'server.conf'

# Key and new value for updating the server configuration
key_to_update = 'MAX_CONNECTIONS'
new_value = '600'  # Updated maximum connections

# Call the function to update the config file
update_server_config(server_config_file, key_to_update, new_value)
