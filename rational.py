from fractions import Fraction

def fract(num1,num2,sign):
    x1 = num1.split('/')
    y1 = num2.split('/')
    fract_num1 = Fraction(int(x1[0]), int(x1[1]))
    fract_num2 = Fraction(int(y1[0]), int(y1[1]))
    if sign == '+':
        result = fract_num1 + fract_num2
    elif sign == '-':
        result = fract_num1 - fract_num2
    elif sign == '*':
        result = fract_num1 * fract_num2
    elif sign == '/':
        result = fract_num1 / fract_num2
    # else:
    #     print(f"Ошибка! Знака {sign} нет в списке '+,-,*,/'")
    return result