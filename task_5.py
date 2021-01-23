'''
5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,
разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел
к полученной ранее сумме и после этого завершить программу.
'''

def my_sum ():
    sum_result = 0
    exit = False
    while exit == False:
        number = input('Input numbers or Q for quit: ').split()

        result = 0
        for element in range(len(number)):
            if number[element] == 'q' or number[element] == 'Q':
                exit = True
                break
            else:
                result = result + int(number[element])
        sum_result = sum_result + result
        print(f'Current sum is {sum_result}')
    print(f'Your final sum is {sum_result}')
(my_sum())