def add(a, b):
    return a + b


def substract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def division(a, b):
    return a / b


operation_dic = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": division
}


def calculator():
    continue_flag = True
    num1 = int(input("Enter the first number: "))

    for op_symbol in operation_dic:
        print(op_symbol)

    while continue_flag:
        symbol = input("pick the operation: ")
        num2 = int(input("Enter the second number: "))

        operation = operation_dic[symbol]
        output = operation(num1, num2)
        print(f"The result is: {output}")
        
        should_continue = input(f"Enter 'y' to continue with {output} or 'n' to start new calculation or 'x' to exit: ")

        if should_continue == 'y':
            num1 = output
        elif should_continue == 'n':
            continue_flag = False
            calculator()
        elif should_continue == 'x':
            continue_flag = False
            print("Bye")


calculator()
