import sys

try:
    file_1 = open(f"{sys.argv[1]}")
    file_2=  open(f"{sys.argv[2]}")

    if file_1.read() == file_2.read():
        print(f"{sys.argv[1]} and {sys.argv[2]} contain the same contents")
    else:
        print("They are different")


except FileNotFoundError:
    print("File not found")

