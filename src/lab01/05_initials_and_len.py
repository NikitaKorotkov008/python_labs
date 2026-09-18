fio = input('Введите ФИО: ')
print(f'Инициалы: {fio.split()[0][0].upper()}{fio.split()[1][0].upper()}{fio.split()[2][0].upper()}.')
print(f'Длина (символов): {len(' '.join(fio.split()))}')