#3.
std=int(input('How many students: '))
group=int(input('Required group size: '))
req= std // group
lf= std % group
print(f'There will be {req} groups with {lf} students left over')