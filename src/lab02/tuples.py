def format_record(rec: tuple[str, str, float]) -> str:
    '''
    Функция берет данные из кортежа, проверяет сколько слов в фио, если их не из диапозона от 2 до 3,
    то вызыватя ValueError потоиу что не так введены данные
    Далее проверяетя корректность ввода gpa если тип данных не тот, то вызывается 
    TypeError
    Далее формируеются данные для строки вывода и все)
    '''
    if type(rec) is not tuple:
        raise ValueError('Должен быть кортеж')
    if len(rec) != 3:
        raise ValueError('Длина должна быть 3')
    fio, group, gpa = rec
    if len(list(fio.split())) not in range(2,4):
        raise ValueError('Не та длинна фио')
    if type(fio) is not str:
        raise ValueError('ФИО должны юыть строкой')
    if type(gpa) is not float:
        raise TypeError('Не тот тип данных gpa')
    if gpa < 0.0 or gpa > 5.0:
        raise ValueError('GPA должен быть в диапозоне от 0.0 до 5.0')
    if len(group) == 0:
        raise ValueError('Пустая группа')
    if type(group) is not str:
        raise ValueError('Группа должна быть строкой ')
    fio = list(fio.strip().split())
    flag = False 
    if len(fio) == 3:
        flag = True
    surname = fio[0].capitalize()+'.'
    initials = ''
    if flag:
        initials+=str(fio[1][0].upper()+'.')
        initials+=str(fio[2][0].upper()+'.')
    else :
        initials+=str(fio[1][0].upper()+'.')
    return f'"{surname}{initials}, гр. {group}, GPA {gpa:.2f}"'

print(format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)))
print(format_record(("Петров Пётр", "IKBO-12", 5.0)))
print(format_record(("Петров Пётр Петрович", "IKBO-12", 5.0)))
print(format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999)))
# print(format_record(("", "ABB-01", 4.0)))
# print(format_record(("Иванов Иван", "", 4.0)))
# print(format_record(("Иванов Иван", "ABB-01", "4.0")))