
while True:
    i = input('Choose the operation : ' )
    if i in ('+', '-', '*', '/'):
        x = float(input('Write first number: '))
        y = float(input('Write second number: '))
        if i == '+':
            addition = x + y
            print(addition)
            with open('result.txt', 'a') as file:
                file.write(str(f'{x} {i} {y} = {addition}' + '\n'))
        elif i == '-':
            subtraction = x - y
            print(subtraction)
            with open('result.txt', 'a') as file:
                file.write(str(f'{x} {i} {y} = {subtraction}' + '\n'))
        elif i == '*':
            multiplication = x * y
            print(multiplication)
            with open('result.txt', 'a') as file:
                file.write(str(f'{x} {i} {y} = {multiplication}' + '\n'))
        elif i == '/':
            if y != 0:
                print('division by zero is not possible')
                division = x / y
                print(division)
                with open('result.txt', 'a') as file:
                    file.write(str(f'\n {x} {i} {y} = {division}'))
        else:
            print('incorrect operation sign')

        print()
