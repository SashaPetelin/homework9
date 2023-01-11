def complex_num(num1,num2,sign):
    complex_num1 = complex(num1)
    complex_num2 = complex(num2)
    if sign == '+':
        result = complex_num1 + complex_num2
    elif sign == '-':
        result = complex_num1 - complex_num2
    elif sign == '*':
        result = complex_num1 * complex_num2
    elif sign == '/':
        result = complex_num1 / complex_num2
    else:
        print(f"Ошибка! Знака {sign} нет в списке '+,-,*,/'")
    return result