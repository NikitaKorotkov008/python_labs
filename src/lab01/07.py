string = input('Введите строку: ')
final_string = ''
ind_up = 0
ind_low = 0
for i in string:
    if i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        final_string += i
        ind_up = string.index(i)
        break
for j in string:
    if j in '1234567890':
        ind = string.index(j)+1
        ind_low = string.index(j)+1
        break
for i in range(ind_low, len(string), ind_low-ind_up):
    final_string += string[i]

print(final_string)