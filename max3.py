# Maximum of 3 numbers. 

def max_of_three(num1, num2, num3):
    maior = 0
    if num1 > num2 and num1 > num3:
        maior = num1
    elif num2 > num1 and num2 > num3:
        maior = num2
    else:
        maior = num3
    return maior



if __name__ == "__main__":
    number1 = input('Digite um numero: ')
    number2 = input('Digite outro numero: ')
    number3 = input('Digite o terceiro numero: ')
    print(max_of_three(number1, number2, number3))
    input()