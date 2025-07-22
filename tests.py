from functions.run_python import run_python_file

print("Result for current directory:")
print(run_python_file("calculator", "main.py")) ##Should be usage instructions

print("Result for current directory:")
print(run_python_file("calculator", "main.py", ["3 + 5"])) ##Bad render

print("Result for current directory:")
print(run_python_file("calculator", "tests.py"))

print("Result for current directory:")
print(run_python_file("calculator", "../main.py")) ##Should return error

print("Result for current directory:")
print(run_python_file("calculator", "nonexistent.py")) ##Should return error