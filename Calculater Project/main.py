from art import logo

def add(n1,n2):
    return n1+n2

def subtract(n1,n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2

def divided(n1,n2):
    return n1 / n2

operation = {
    "+": add,
    "*": multiply,
    "-": subtract,
    "/": divided
}

def calculator():
    print(logo)
    num1 = float(input("What is your first number? : "))
    for symbole in operation:
        print(symbole)
    should_continue = True

    while should_continue :
        operation_symbol = input("Pick an operation:")
        num2 = float(input("What is your second number? :"))

        Calculation_function = operation[operation_symbol]
        answer = Calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer} ")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to Start new calculator : ") == 'y':
            num1 = answer
        else:
            should_contonue = False
            calculator()
          
calculator()