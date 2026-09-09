n = int(input('Введите число: '))
cnt = 0
ochno = 0
zaochno = 0
while cnt < n:
    s = list(input().split())
    cnt+=1
    if s[3] == 'True':
        ochno+=1
    else:
        zaochno+=1
print(ochno, zaochno)