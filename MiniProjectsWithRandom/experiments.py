nums = int(input())

command = ' '
add = 0

while not command == 'end':
    new_command = int(input())
    add += new_command

    command = input()

print(add)