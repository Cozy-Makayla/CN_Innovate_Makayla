class Person():
    def __init__(self, name :str, age: int, eye_color: str, hair_color: str):
        self.name = name
        self.age = age
        self.eye = eye_color
        self.hair = hair_color

    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = int(age)

    def set_eye(self, eye):
        self.eye = eye

    def set_hair(self, hair):
        self.hair = hair

    def set_profession(self, profession):
        self.profession = profession

npc_list = []
player = Person("default", 1, 'eye-color', 'hair-color')
npc1 = Person("Jude", 22, 'emerald green', 'strawberry')
npc2 = Person("Jake", 52, 'crimson red', 'gremmish')
npc3 = Person("Berkley", 24, 'skinny green', 'custard')
npc4 = Person("Trevor", 66, 'sunlit blue', 'low pink')
npc5 = Person("Oscar", 101, 'musk yellow', 'viscount mint')
npc6 = Person("Gunther", 23, 'gremlin brown', 'no')

npc_list.append(npc1)
npc_list.append(npc2)
npc_list.append(npc3)
npc_list.append(npc4)
npc_list.append(npc5)
npc_list.append(npc6)

def player_info(obj):
    print(f'''
    Hello! {obj.name}
    your profession is {obj.profession}
    you have loverly {obj.eye} eyes, and {obj.hair} hair
    You are {obj.age} years old
    ''')

def npc_info(name: str, npc_list):
    for obj in npc_list:
        if name.title() == obj.name:
            print(f"Their name:{obj.name}, they have {obj.eye} eyes, and {obj.hair} hair. they are {obj.age} years old")

def person_inspect():
    player_choice = input("Who do you want to inspect? [M]e // [O]ther \n")
    match player_choice.upper():
        case 'M' | 'ME': player_info(player)
        case 'O' | 'OTHER':
            print('avalible choices:')
            for obj in npc_list:
                print(obj.name)
            name_query = input('Enter their name >: ')
            npc_info(name_query, npc_list)

def chara_creation():
    player_name = input('Please enter your NAME: \n')
    player_age = int(input('Please enter your AGE: \n'))
    player_eye = input('Please enter your EYE color: \n')
    player_hair = input('Please enter your HAIR color: \n')
    player_profession = input('Please enter your PROFESSION: \n')
    player.set_name(player_name.title())
    player.set_age(player_age)
    player.set_eye(player_eye.title())
    player.set_hair(player_hair.title())
    player.set_profession(player_profession.title())

chara_creation()
person_inspect()