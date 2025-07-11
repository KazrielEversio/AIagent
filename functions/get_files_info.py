import os
from os.path import join

def get_files_info(working_directory, directory="."):
    try:
        full_path = os.path.abspath(join(working_directory, directory))
        if not full_path.startswith(os.path.abspath(working_directory)):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        if not os.path.isdir(full_path):
            return f'Error: "{directory}" is not a directory'
        lines = []
        for entry in os.listdir(full_path):
            entry_path = os.path.join(full_path, entry)
            line = f"- {entry}: file_size={os.path.getsize(entry_path)} bytes, is_dir={os.path.isdir(entry_path)}"
            lines.append(line)
        return "\n".join(lines)
    except Exception as e:
        return f"Error: {str(e)}"