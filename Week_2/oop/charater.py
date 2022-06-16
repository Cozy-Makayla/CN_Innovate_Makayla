class Hero():
    def __init__(self, name: str, power: str, alias: str, weakness: str):
        self.name = name
        self.power = power
        self.alias = alias
        self.weakness = weakness

superman = Hero('Superman', 'immortallity', 'Clark Kent', 'Kriptonite')
spiderman = Hero('Spiderman', 'spidey powers', 'Peter Parker', 'Nieve')
batman = Hero('Batman', 'Money and Intelligence', 'Bruce Wayne', 'Childhood Trauma')

superhero_list = []
superhero_list.append(superman)
superhero_list.append(spiderman)
superhero_list.append(batman)

def superhero_info(name, passin_list):
    for obj in passin_list:
        if name == obj.name:
            print(f'''
{obj.name}
{obj.power}
{obj.alias}
{obj.weakness}
            ''')



def user_selector():
    for obj in superhero_list:
        print(obj.name)
    user_choice = input('Please enter the name of the superhero you wish to view\n').title()
    superhero_info(user_choice, superhero_list)