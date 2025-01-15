def prime(num):
    if num<0:
        print('Enter positive value')
    else:
        for i in range (2,num):
            if(num%i==0):
                print("Number is not prime")
            else:
                print("Its prime")
            break
    
prime(19)
prime(18)