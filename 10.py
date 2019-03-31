# http://www.pythonchallenge.com/pc/return/bull.html

def look_and_say_next_number(number):
    number = str(number) + ' '
    next_number = str()
    previous, count = '0', 0
    for n in number:
        if previous == n or previous == '0':
            previous = n
        else:
            next_number += str(count) + previous
            previous, count = n, 0
        count += 1
    return int(next_number)

def look_and_say_nth_number(nth):
    number = 1
    for i in range(nth):
        number = look_and_say_next_number(number)
    return number

print(len(str(look_and_say_nth_number(30))))
