# Maximum of 2 numbers. Function returns 0 for equal numbers.

def max(number1, number2):
    if number1 > number2:
        return number1
    elif number1 < number2:
        return number2
    else:
        return 0
        

if __name__ == "__main__":
    number1 = input('Digite um numero: ')
    number2 = input('Digite outro numero: ')
    print(max(number1, number2))
    input()