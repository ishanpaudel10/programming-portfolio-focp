import sys
arg=sys.argv[1:]
arg_sort=min(arg, key=len)
print(f'Shortest argument is:{arg_sort}')       

