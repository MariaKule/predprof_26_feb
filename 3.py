data=open('space.txt',encoding='utf-8').read().split('\n')
data.pop(0)
new=[]
for i in data:
    s=i.split('*')
    new.append(s)
while True:
    korabl=input('Введите название корабля: ')
    if korabl=='stop':
        break
    for i in range(len(new)):
        if new[i][0]==korabl:
            print(f'Корабль {new[i][0]} был отправлен с планеты: {new[i][1]} и его направление движения было: {new[i][3]}')
