from functions.write_file import write_file

print("Result for current directory:")
print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))

print("Result for current directory:")
print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))

print("Result for current directory:")
print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))