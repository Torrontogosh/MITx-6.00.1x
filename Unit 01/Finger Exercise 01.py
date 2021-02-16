#   This exercise was written with the assumption that none of the variables defined at the top would be over 1000. It simply tries to place the lowest odd number into the variable "lowest_number", and either prints that number out or prints a message that there are no odd numbers.

x = 10
y = 30
z = 14
lowest_number = 1000

if x%2 != 0:
    lowest_number = x

if y%2 != 0 and y < lowest_number:
    lowest_number = y

if z%2 != 0 and z < lowest_number:
    lowest_number = z


if x%2 == 0 and y%2 == 0 and z%2 == 0:
    print('There are no odd numbers.')
else:
    print(lowest_number)
