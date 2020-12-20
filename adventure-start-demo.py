'''Version 1.0 Of My Python Adventure Game'''

import time

def story1():
    print('')

def story2():
    print('')

def story3():
    print('')

def story4():
    print('')

def story5():
    print('')

def opening():
    nes = input('Would you like to go on a adventure? Yes or no: ')
    while True:
        print('')
        if nes == 'yes':
            print('Fantastic! ', end='')
            time.sleep(1)
            print('Lets begin!')
            time.sleep(1)
            print('-~-')
            break
        elif nes == 'no':
            print('Ok Then. Goodbye!')
            time.sleep(2)
            break
        else:
            print('I would like to know if you want to go on an adventure. Say yes if you want to, and no if you dont')
            print('-~-')
            nes = input('Would you like to go on a adventure? ')
opening()

def selection():
    print('I have five stories for you right now and below is a breif descripion of each.')
    time.sleep(3)
    print('Just type which number is in front of the story you want to hear on the prompt below.')
    time.sleep(3)
    print('')
    print('-~-')
    print('1. Life. A simulator of life on Earth.')
    print('2. W.I.P.')
    print('3. W.I.P.')
    print('4. W.I.P.')
    print('5. W.I.P.')
    print('-~-')
    print('')
    storychoice = input('Which story would you like to hear? (1/2/3/4/5): ')
    while True:
        print('-~-')
        if storychoice == '1':
            print('Alright! ', end='')
            time.sleep(1)
            print('Ive always thought as a program, ', end='')
            time.sleep(2)
            print('it would be interesting to see human life unravel in a simulation.')
            time.sleep(3)
            print('Lets go!')
            print('-~-')
            story1()
            break
        elif storychoice == '2':
            print('Alright! ', end='')
            time.sleep(1)
            print('')
            time.sleep(1)
            print('Lets go!')
            print('-~-')
            story2()
            break
        elif storychoice == '3':
            print('Alright! ', end='')
            time.sleep(1)
            print('')
            time.sleep(1)
            print('Lets go!')
            print('-~-')
            story3()
            break
        elif storychoice == '4':
            print('Alright! ', end='')
            time.sleep(1)
            print('')
            time.sleep(1)
            print('Lets go!')
            print('-~-')
            story4()
            break
        elif storychoice == '5':
            print('Alright! ', end='')
            time.sleep(1)
            print('')
            time.sleep(1)
            print('Lets go!')
            print('-~-')
            story5()
            break
        else:
            print('Please enter 1, 2, 3, 4, or 5 to start one of my stories.')
            print('-~-')
            storychoice = int(input('Which story would you like to hear? '))
selection()

print('Thank you for playing the begining demo of An Adventure')
time.sleep(5)