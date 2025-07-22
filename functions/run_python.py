import os
from os.path import join
import subprocess

def run_python_file(working_directory, file_path, args=[]):
    try:
        full_path = os.path.abspath(join(working_directory, file_path))
        if not full_path.startswith(os.path.abspath(working_directory)):
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(full_path):
            return f'File "{file_path}" not found.'
        if not full_path.endswith('.py'):
            return f'Error: "{file_path}" is not a Python file.'
        completed_process = subprocess.run(["python", full_path] + args, capture_output=True, timeout=30, cwd=working_directory)
        STDOUT_ERR = f'STDOUT: {completed_process.stdout.decode()}\nSTDERR: {completed_process.stderr.decode()}'
        if completed_process.returncode!=0:
            return f'{STDOUT_ERR}\nProcess exited with code {completed_process.returncode}'
        if completed_process.stdout.decode() == "" and completed_process.stderr.decode() == "":
            return "No output produced."
        return STDOUT_ERR
    except Exception as e:
        return f"Error: executing Python file: {str(e)}"