#4.
sweets=int(input('How many sweets does teacher brought: '))
std=int(input('How many pupils attended that day: '))
give= sweets//std
lf= sweets % std
print(f'You should give {sweets} number of sweets to {std} number of pupils and {lf} sweets will be left over')