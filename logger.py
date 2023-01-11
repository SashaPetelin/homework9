from datetime import datetime as dt
from time import time

def log_result(num1, oper, num2, result):                                        
    time = dt.now().strftime('%H:%M:%S')
    with open('file.csv','a', encoding='UTF-8') as file:
        file.write(f'{time} Результат вычисления: ({num1}) {oper} ({num2}) = {result}\n')           