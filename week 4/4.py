#4.
def val():
    str=input('Enter any text you want: ')
    return str

def slice(str):
    str2=str[0:-1]
    return str2

def display(str,str2):
    if len(str)<=1:
        print(f'This is the text you entered: {str} and last character wont be removed')
    else:
        print(f'This is the text you entered: {str2} with last character removed')
    
str=val()
str2=slice(str)
d=display(str,str2)
