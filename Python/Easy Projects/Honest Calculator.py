# write your code here
running = True
Memory = 0

def GetEquation():
    global x
    global y
    global operator
    equation = input("Enter an equation\n")
    equation_list = equation.split()
    if 'M' in equation_list:
        if equation_list[0] == 'M':
            x = Memory
            y = equation_list[2]
            operator = equation_list[1]
        elif equation_list[2] == 'M':
            x = equation_list[0]
            y = Memory
            operator = equation_list[1]
    else:
        x = equation_list[0]
        operator = equation_list[1]
        y = equation_list[2]
    return x, y, operator

def PerformEquation(x, operator, y):
    try:
        float(x) and float(y)
        x = float(x)
        y = float(y)
        if operator == '+':
            result = (x + y)
            StoreResult(result)
        elif operator == '-':
            result = (x - y)
            StoreResult(result)
        elif operator == '*':
            result = (x * y)
            StoreResult(result)
        elif operator == '/':
            try:
                y != 0
                result = (x / y)
                StoreResult(result)
            except:
                print("Yeah... division by zero. Smart move...")
        else:
            print("Yes ... an interesting math operation. You've slept through all classes, haven't you?")
    except:
        print("Do you even know what numbers are? Stay focused!")

def StoreResult(result):
    global running
    global Memory
    print(result)
    store_input = input("Do you want to store the result? (y / n):\n")
    if store_input == 'y':
        resultLength = GetAnswerLength(result)
        saveBool = ShameUser(resultLength)
        continue_input = input("Do you want to continue calculations? (y / n):\n")
        if continue_input == 'y':
            if saveBool == True:
                Memory = result
                return Memory
        elif continue_input == 'n':
            running = False
    elif store_input == 'n':
        continue_input = input("Do you want to continue calculations? (y / n):\n")
        if continue_input == 'y':
            running = True
        elif continue_input == 'n':
            running = False

def IsOneDigit(x):
    try:
        x = int(x)
        if x == int(x):
            return -10 < x < 10
    except ValueError:
        return False

def CheckNumbers(x, operator, y):
    message = ""
    if IsOneDigit(x) and IsOneDigit(y):
        message = " ... lazy"
    x = float(x)
    y = float(y)
    if operator == "*" and (x == 1 or y == 1):
        message = message + " ... very lazy"
    if (x == 0 or y == 0) and (operator != "/"):
        message = message + " ... very, very lazy"
    if len(message) >= 1:
        print("You are" + message)

def GetAnswerLength(result):
    resultString = str(result)
    resultLength = len(resultString)
    return resultLength

def ShameUser(resultLength):
    if resultLength == 1:
        shameInput = input("Are you sure? It is only one digit! (y / n)\n")
        if shameInput == 'y':
            shameInput = input("Don't be silly! It's just one number! Add to memory? (y / n)\n")
            if shameInput == 'y':
                shameInput = input("Last chance! Do you really want to embarrass yourself? (y / n)\n")
                if shameInput == 'y':
                    shameBool = True
    elif resultLength > 1:
        saveBool = True
        return saveBool
    if shameBool == True:
        saveBool = True
        return saveBool

while running:
    GetEquation()
    CheckNumbers(x, operator, y)
    PerformEquation(x, operator, y)
