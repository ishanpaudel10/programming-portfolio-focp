def to_binary(num):
    if num>0:
        return bin (num)[2:]
    else:
        print("Enter positive value")

print(to_binary(10))

