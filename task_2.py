'''
2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
'''

# Функция информации о пользователе
def my_func(name, surname, birth_year, city, email, telephone):
    return ' '.join([name, surname, birth_year, city, email, telephone])
print(my_func(name='Vasia',
              surname='Poopkin,',
              birth_year='Birth year: 1980,',
              city='City: Moscow,',
              email='email: why@mail.ru,',
              telephone='Telephone: 8(985)532-54-11'))