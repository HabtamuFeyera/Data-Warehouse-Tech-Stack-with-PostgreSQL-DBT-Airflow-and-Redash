import os

# Get the current working directory
current_directory = os.getcwd()

# Specify the name of the output directory
output_directory_name = "data_output"

# Create the full path for the output directory
save_dag_path = os.path.join(current_directory, output_directory_name)

# Ensure the output directory exists; if not, create it
os.makedirs(save_dag_path, exist_ok=True)
