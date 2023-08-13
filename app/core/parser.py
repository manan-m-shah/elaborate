import os
from app.utils.storage import get_new_temp_dir
from app.utils.ignore import IGNORED_PATTERNS, IGNORED_FILES, IGNORED_FOLDERS

def parseFile(repo_owner, repo_name, temp_folder):
    # Reading the repository files
    output_folder = get_new_temp_dir()
    output_file_path = os.path.join(output_folder, f"{repo_owner}_{repo_name}.txt")
    with open(output_file_path, "w") as output_file:
        # Add instructions for GPT
        instructions = (
            "### LANGUAGE MODEL INSTRUCTIONS ###\n"
            "This document contains parsed content from the repository. "
            "Each file's structure starts with the file path from the root directory, followed by code or text, "
            "and is marked by ================================================== at the end. After that, a new file's structure begins.\n"
            "Please note that this content may include code, text, and other data.\n"
            "#########################\n\n"
        )
        output_file.write(instructions)
        for root, dirs, files in os.walk(temp_folder):
            # Filter ignored folders
            dirs[:] = [d for d in dirs if d not in IGNORED_FOLDERS]
            for file_name in files:
                file_path = os.path.join(root, file_name)
                relative_file_path = os.path.relpath(file_path, temp_folder)
                if any(pattern in file_path for pattern in IGNORED_FILES):
                    continue  # Skip ignored patterns
                try:
                    with open(file_path, "r") as file:
                        content = file.read()
                        output_file.write(f"File: {relative_file_path}\n")
                        output_file.write("File Contents:\n")
                        output_file.write(content)
                        output_file.write("\n" + "=" * 50 + "\n")
                except:
                    print("Error reading file: ", file_path)

    return output_file_path

