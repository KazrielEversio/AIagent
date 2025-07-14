from functions.get_file_content import get_file_content

print("Result for current directory:")
print(get_file_content("calculator", "main.py"))

print("Result for current directory:")
print(get_file_content("calculator", "pkg/calculator.py"))

print("Result for current directory:")
print(get_file_content("calculator", "/bin/cat"))