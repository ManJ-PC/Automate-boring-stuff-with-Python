def collatz(number):
    if number % 2 == 0:
        result = number // 2
    else:
        result = 3 * number + 1
    return result

def collatz2(number, steps):
    if number == 1:
        return number, steps
    steps += 1
    if number % 2 == 0:
        print(number)
        return collatz2(number//2, steps)
    else:
        print(number)
        return collatz2(3*number+1, steps)


def interativo():
    print('Versão  interativa\n')
    steps = 0
    try:
        number = int(input('Digite um número: '))
        while number != 1:
            number = collatz(number)
            print(number)
            steps = steps + 1
    except ValueError: #Exception as e:  #ValueError:
        # print(e) # invalid literal for int() with base 10: 'ty'
        print('Write a integer value!')
    print('\n You reach the termination number!\n The number of steps was:', steps, '\n')


def recursive():
    steps=0
    print('Versão  recursiva\n')
    try:
        number = int(input('Digite um número: '))
        number, steps = collatz2(number, steps)
    except ValueError: #Exception as e:  #ValueError:
        # print(e) # invalid literal for int() with base 10: 'ty'
        print('Write a integer value!')
    print('\n You reach the termination number!\n The number of steps was:', steps, '\n')


interativo()
print('___________________\n')
recursive()       
    
