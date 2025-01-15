#8.
while True:
    i=12
    j=0
    n=int(input('Enter a number: '))
    if n<0:
        while i>=0:
            print(f'{n}*{i}={n*i}')
            i=i-1
        
    elif n>0:
        while j<=12:
            print(f'{n}*{j}={n*j}')
            j=j+1
    break
