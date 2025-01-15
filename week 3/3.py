#3.
while True:
    print('Your password should be between 8 and 12 characters inclusive')
    pw1=input('Enter your password: ')
    pw2=input('Re-enter your password again: ')
    if pw1 ==pw2 and (8<=len(pw1)<=12):
        print('Password is set')
        break
    else:
        print('Passwords do not match!')