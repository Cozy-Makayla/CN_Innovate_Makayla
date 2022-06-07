#ACT 1
message_var = 'Welcome to Code Nation!'

def isEven(str1):
    str_mod = (len(str1) % 2)
    if str_mod == 0:
        print(f'{str1} has an even number of chars, {len(str1)}')
    else:
        print(f'{str1} has an odd number of chars, {len(str1)}')

isEven(message_var)

#ACT 2
alpha = [
    'a','b','c',
    'd','e','f',
    'g','h','i',
    'j','k','l',
    'm','n','o',
    'p','q','r',
    's','t','u',
    'v','w','x',
    'y','z'
]
def iteration(list_selected):
    for x in list_selected:
        print(x)


def user_selection_list(list_selected):
    user_input = int(input('Please select a number: '))
    print(f'Number {user_input} is {list_selected[user_input -1]}')

iteration(alpha)
user_selection_list(alpha)