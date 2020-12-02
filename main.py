#Matthew Resendez
#1431242
parts = input().split()
name = parts[0]
while name != '-1':
    try:
        age = int(parts[1]) + 1
    except ValueError:
        age = 0
    print(name, age)
    parts = input().split()
    name = parts[0]