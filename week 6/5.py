import random

def encrypt_with_random_intervals(message):
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    encrypted_message = []
    intervals = []  
    for char in message:
        
        interval = random.randint(2, 20)
        intervals.append(interval)

        for i in range(interval):
            encrypted_message.append(random.choice(chars))        
        encrypted_message.append(char)
          
    return ''.join(encrypted_message), intervals


message = input("Enter the message you would like to encrypt: ")
encrypted_message, intervals = encrypt_with_random_intervals(message)

print(f"Encrypted message: {encrypted_message}")
print(f"Intervals used: {intervals}")
