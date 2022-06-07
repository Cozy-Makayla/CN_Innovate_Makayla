def Addup():
    num1 = input('Please enter number 1: \n')
    num2 = input('Please enter number 2: \n')
    try:
        print(f'{num1} + {num2} = {(int(num1) + int(num2))}')
    except:
        print('Error these are not numbers')

Addup()