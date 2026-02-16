import nbformat
import os

def clean_notebook_for_github(file_name):
    # Get the directory where THIS script is saved (MATLAB pwd/which equivalent)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Create the full path to the notebook
    file_path = os.path.join(script_dir, file_name)
    
    if not os.path.exists(file_path):
        print(f"Error: Could not find {file_name} in {script_dir}")
        return

    # Read the notebook
    with open(file_path, 'r', encoding='utf-8') as f:
        nb = nbformat.read(f, as_version=4)
    
    # Remove the problematic widgets metadata
    if 'widgets' in nb.metadata:
        del nb.metadata['widgets']
        print(f"Success: Removed widgets from {file_path}")
    else:
        print(f"Notice: No widgets found in {file_name}")

    # Write the cleaned notebook back
    with open(file_path, 'w', encoding='utf-8') as f:
        nbformat.write(nb, f)

# Usage - just provide the filename
clean_notebook_for_github('Pedretti_HW1.ipynb')