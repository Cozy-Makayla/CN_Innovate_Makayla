light = False

def light_switch():
    if light:
        print('On!')
        light = False
    else:
        print('off')
        light = True

light_switch()
light_switch()