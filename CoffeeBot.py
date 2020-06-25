# Prototype CoffeeBot : A very rudamentary ChatBot

def CoffeeBot():
    print("Welcome to the cafe! \n")
    size = getSize()
    drinkType = getDrinkType()
    print("Alright, that's a", size, drinkType)
    name = input("Can I get your name please? : ")
    print("Thanks,", name + "! Your drink will be ready shortly.")

def printMessage():
    print("I'm sorry, I did not understand your selection. Please enter the corresponding letter for your response.")

def getSize():
    res = input("What size drink can I get for you? \n[a] Small \n[b] Medium \n[c] Large \n")
    if (res == 'a') or (res == 'A'):
        return "small"
    elif (res == 'b') or (res == 'B'):
        return "medium"
    elif (res == 'c') or (res == 'C'):
        return "large"
    else:
        printMessage()
        return getSize()

def getDrinkType():
    res = input("What type of drink would you like? \n[a] Brewed Coffee \n[b] Mocha \n[c] Latte \n")
    if (res == 'a') or (res == 'A'):
        return "brewed coffee"
    elif (res == 'b') or (res == 'B'):
        return "mocha"
    elif (res == 'c') or (res == 'C'):
        return orderLatte()
    else:
        printMessage()
        return getDrinkType()

def orderLatte():
    res = input("And what kind of milk for your latte? \n[a] 2% milk \n[b] Non-fat milk \n[c] Soy milk \n")
    if (res == 'a') or (res == 'A'):
        return "latte"
    elif (res == 'b') or (res == 'B'):
        return "non-fat latte"
    elif (res == 'c') or (res == 'C'):
        return "soy latte"
    else:
        printMessage()
        return orderLatte


CoffeeBot()
