#7.
while True:
    i=1
    n=int(input('Enter the number for the timetable: '))
    if n>=0 and n<=12:
        while i<=10:
            print(f'{n}*{i}={n*i}')
            i=i+1
        break
    else:
        print('Please enter the number from 1 to 12 only')