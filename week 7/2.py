def letters_atleast_in_one(w1,w2):
    lt=sorted(set(w1) | set(w2))
    return lt

def letters_in_both(w1,w2):
    lt=sorted(set(w1) & set(w2))
    return lt

def letters_in_one_word_but_not_in_both(w1,w2):
    lt=sorted(set(w1) ^ set(w2))
    return lt

w1=input("Enter a word: ")
w2=input("Enter another word: ")
    
print(f"Letters at least in one {letters_atleast_in_one(w1,w2)}")
print(f"Letters in both {letters_in_both(w1,w2)}")
print(f"Letters at least in one but not both {letters_in_one_word_but_not_in_both(w1,w2)}")
    
