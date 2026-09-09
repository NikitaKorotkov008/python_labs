fio = input('Введите ФИО: ')
print(f'Инициалы: {fio.split()[0][0]}{fio.split()[1][0]}{fio.split()[2][0]}.')
print(f'Длина (символов): {len(' '.join(fio.split()))}')