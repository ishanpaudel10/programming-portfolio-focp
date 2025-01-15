import sys

try:
    f=open(f"{sys.argv[1]}")
    for line_num,line in enumerate(f,start=1):
        print(f'{line_num}: {line}')

except FileNotFoundError:
    print("File is not there")


