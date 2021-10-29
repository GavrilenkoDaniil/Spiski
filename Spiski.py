from random import *
from keyboard import *
print("Камень, ножницы, бумага")
a=""
arv1=0
arv2=0
while a not in [1,2,3]:
    try:
        a=int(input("С кем играть?\n1 - с человеком\n2 - с компьютером\n3 - компьютер с компьютером"))
    except:
        ValueError
if a==1:
    while True:
        print("Играем? esc - выйти, enter - играем")
        if read_key()=='esc':
            break
        else:
            print("Ты выбрал играть с человеком\nВыбери предмет:")
            b=0
            while b not in [1,2,3]:
                try:
                    b=int(input("1 - Камень\n2 - Ножницы\n3 - Бумага"))
                    break
                except:
                    ValueError
                    print("Введи правильное число")
            c=0
            while c not in [1,2,3]:
                try:
                    c=int(input("1 - Камень\n2 - Ножницы\n3 - Бумага"))
                except:
                    ValueError
                    print("Введи правильное число")
            if b==1 and c==2:
                print("player1 победил")
                arv1+=1
            elif b==1 and c==3:
                print("player2 победил")
                arv2+=1
            elif b==1 and c==1:
                print("Ничья")
            elif b==2 and c==1:
                print("player2 победил")
                arv2+=1
            elif b==2 and c==2:
                print("Ничья")
            elif b==2 and c==3:
                print("player1 победил")
                arv1+=1
            elif b==3 and c==1:
                print("player1 победил")
                arv1+=1
            elif b==3 and c==2:
                print("player2 победил")
                arv2+=1
            elif b==3 and c==3:
                print("Ничья") 
            print(f"{arv1}- очки player1\n{arv2} - очки player2") 
elif a==2:
    while True:
        print("Играем? esc - выйти, enter - играем")
        if read_key()=='esc':
            break
        elif read_key()=='enter':
            print("Ты выбрал играть с компьютером")
            b=0
            arv1=0
            arv2=0
            while b not in [1,2,3]:
                try:
                    b=int(input("1 - Камень\n2 - Ножницы\n3 - Бумага"))
                except:
                    ValueError
                    print("Введи правильное число")
            d=randint(1,3)
            if b==1 and d==2:
                print("Ты победил")
                arv1+=1
            elif b==1 and d==3:
                print("Робот победил")
                arv2+=1
            elif b==1 and d==1:
                print("Ничья")
            elif b==2 and d==1:
                print("Робот победил")
                arv2+=1
            elif b==2 and d==2:
                print("Ничья")
            elif b==2 and d==3:
                print("Ты победил")
                arv1+=1
            elif b==3 and d==1:
                print("Ты победил")
                arv1+=1
            elif b==3 and d==2:
                print("Робот победил")
                arv2+=1
            elif b==3 and d==3:
                print("Ничья") 
            print(f"{arv1}- твои очки\n{arv2} - очки робота")
elif a==3:
    v1=["Камень","Ножницы","Бумага"]
    v2=["Камень","Ножницы","Бумага"]
    while True:
        print("Играем? esc - выйти, enter - играем")
        if read_key()=='esc':
            break
        elif read_key()=='enter':
            p1=choice(v1)
            print("Первый робот: ",p1)
            p2=choice(v2)
            print("Второй робот ",p2)
            if p1==p2:
                print("Ничья")
            elif p1==v1[0] and p2==v2[1] or p1==v1[2] and p2==v2[0] or p1==v1[1] and p2==v2[2]:
                print("Выйграл player1")
            else:
                print("Выйграл player2")
