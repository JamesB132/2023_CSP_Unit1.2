#Stage 1

def pyramid1():
    spacer = str("xxxxx")
    x = 5
    for string in range(5):
        print(spacer[:x])
        x -= 1
pyramid1()

#Stage 2

def pyramid2():
    dot = str("xxxxx")
    x = 5
    space = str("")
    for loop in range(5):
        print(space, dot[:x])
        space += " "
        x -= 1

pyramid2()
