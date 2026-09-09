price = float(input('Цена: '))
discount = float(input('Скидка: '))
vat = float(input('НДС: '))
base = price * (1 - discount/100)
vat_amount = base * (vat/100)
total = base + vat_amount
print(f'База после скидки: {float(base)} ₽')
print(f'НДС: {float(vat_amount)} ₽')
print(f'Итого к оплате: {float(total)} ₽')