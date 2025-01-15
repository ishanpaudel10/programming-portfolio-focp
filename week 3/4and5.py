#4 and 5.
BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber'] 
print(['password', 'letmein', 'sesame', 'hello', 'justinbieber'] )
while True:
    print('Your password should be between 8 and 12 characters inclusive and the passwords cannot be of bad passwords')
    pw1=input('Enter your password: ')
    pw2=input('Re-enter your password again: ')
    if pw1 ==pw2 and (8<=len(pw1)<=12) and (pw1 not in BAD_PASSWORDS ):
        print('Password is set')
        break
    else:
        print('Passwords do not match!')