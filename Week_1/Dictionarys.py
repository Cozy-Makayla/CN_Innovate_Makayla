weapons_sword = {
    'name' : 'Short Sword',
    'length' : 5,
    'damage' : 10,
    'weight' : 10.5,
    'value' : 500
}

weapons_spear = {
    'name' : 'Spear',
    'length' : 15,
    'damage' : 15,
    'weight' : 15.0,
    'value' : 1500
}

def dict_inspect(item:dict):
    print('#######################')
    for x in item:
        print(f'|{x :6} > {item[x]:12}|')
    print('#######################')

def item_select():
    pcontinue = True
    while pcontinue == True: 
        pchoice = input('Please choose (1)sword or (2)spear: ')
        match pchoice.capitalize():
            case '1':
                dict_inspect(weapons_sword)
            case '2': 
                dict_inspect(weapons_spear)
            case _: 
                print(f'{pchoice} Not found try again')
        pchoice = input('Select another item? Y/N')
        match pchoice.capitalize():
            case 'Y' | 'YES': pcontinue = True
            case 'N' | 'NO': pcontinue = False
            case _: print(f'{pchoice} Not found returning to item select...')

# item_select()

# Activity 2

countries = {
    "country_1" : {'name': 'england', 'capital' : "manchester",},
    "country_2" : {'name': 'fance', 'capital' : "paris",},
    "country_3" : {'name': 'germany', 'capital' : "berlin",},
    "country_4" : {'name': 'spain', 'capital' : "madrid",},
    "country_5" : {'name': 'italy', 'capital' : "rome",},
}

languages = [
    'english',
    'french',
    'german',
    'spannish',
    'italian',
    'English',
    'Japanese'
]

def add_country(country: str, capital: str):
    countries.setdefault(country, capital)

def dict_inspect(item:dict):
    print('#######################')
    print(item)
    # for x in item:
        # print(f'|{x :6} > {item[x]:12}|')
    print('#######################')

def refactor_dict(item:dict):
    for x in item:
        item[x].pop('capital')
    return item

def define_new_country(countries: dict):
    # user_adding = True
    # while user_adding:
    #     user_add_country = input('Please type the name of the contry you wish to add: ')
    #     user_add_capital = input('Please type the name of the capital for that contry: ')
    #     add_country(user_add_country, user_add_capital)
    #     continue_query = input('would you like to add another? Y|N \n')
    #     match continue_query.capitalize():
    #         case 'Y' | 'YES': print('returning ...')
    #         case 'N' | 'NO': user_adding = False
    countries.setdefault(country, capital)
    dict_inspect(countries)
    countries = refactor_dict(countries)
    dict_inspect(countries)

define_new_country(countries)

#ACT 3

fav_songs = [
    {
        'artist' : 'lady gaga',
        'song name': 'sour candy',
        'genre' : 'pop',
        'year' : '2020'
    },
    {
        'artist' : 'the midnight',
        'song name': 'change your heart or die',
        'genre' : 'synthwave',
        'year' : '2022'
    },
    {
        'artist' : 'dua lipa',
        'song name': 'hallucinate',
        'genre' : 'pop',
        'year' : '2020'
    },
    {
        'artist' : 'charli',
        'song name': 'you used to know me',
        'genre' : 'dance',
        'year' : '2022'
    }
]
def print_list_dict(choice_list: list):
    i = 0
    for x in fav_songs:
        print(fav_songs[i])
        i += 1

#print_list_dict(fav_songs)