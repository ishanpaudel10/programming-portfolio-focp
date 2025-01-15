#5 and 6
def cel_to_far(cel):
    fa=(cel*9/5)+32 
    return fa

def far_to_cel(fa):
    cel=((fa-32)*5/9)
    return cel

print('Temperature conversion')
print('1.Celsius to Faranheit')
print('2.Faranheit to Celsius')
print('3.Exit')

while True:
    choice=int(input('Enter your choice (1/2/3): '))
    if choice in (1,2,3):
        if choice==1:
            c=float(input('Enter the temperature of celsius: '))
            print(f'The temperature from {c}C to faranheit is: {cel_to_far(c)}')
        
        elif choice==2:
            f=float(input('Enter temperature in faranheit: '))
            print(f'The temperature from {f}F to celsius is: {far_to_cel(c)}')
        
        elif choice==3:
            print("Exiting the program")
            break
    else:
        print('Please enter the valid choice from (1/2/3)')