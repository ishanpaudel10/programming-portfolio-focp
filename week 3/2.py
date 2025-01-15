#2.
while True:
    pw1=input('Enter your password: ')
    pw2=input('Re-enter your password again: ')
    if pw1 ==pw2:
        print('Password is set')
        break
    else:
        print('Passwords do not match!')