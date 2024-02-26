data=open('space.txt',encoding='utf-8').read().split('\n')
spacenew=open('space_new.csv','w')
spacenew.write(f'ShipName,planet,coord_place,direction')
z=[]
for i in data:
    s=i.split('*')
    if '0 0' in s[2]:
        n=int(s[0][-3])
        m=int(s[0][-2])
        a=s[3].index(' ')
        t=len(s[1])
        s[2]=[]
        if ' ' in s[1]:
            t-=1
        if n>5:
            s[2].append(n+int(s[3][:a]))
        if n<=5:
            s[2].append((n+int(s[3][:a]))*(-4)+t)
        if m>3:
            s[2].append(m+int(s[3][a+1:])+t)
        if m<=3:
            s[2].append((n+int(s[3][a+1:]))*m*(-1))
        if s[0][3]=='V':
            print(s[0]+' - ('+str(s[2][0])+', '+str(s[2][1])+')')
            z.append(s[0])
    if s[0][3]=='V' and s[0] not in z:
        k=s[2].index(' ')
        print(s[0]+' - ('+s[2][:k]+', '+s[2][k+1:]+')')
    spacenew.write(f'{s[0]},{s[1]},{s[2]},{s[3]},\n')
