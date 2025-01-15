#2.
def func(str):
    upper=0
    lower=0
    for char in str:
        if char.isupper():
            upper+=1
        elif char.islower():
            lower+=1
    
    print(f'Lowercase letters: {lower}')
    print(f'Uppercase letters: {upper}')

func('IsHAnPoAj')