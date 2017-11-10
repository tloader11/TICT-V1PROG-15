import random
def monopolyworp():
    dubbel = 0
    while True:
        a= random.randint(1,6)
        b= random.randint(1,6)
        if a==b and dubbel < 2:
            print(a,"+",b,"=",a+b,"(dubbel)")
            dubbel+=1
        elif a==b and dubbel == 2:
            print(a,"+",b,"=","(direct naar gevangenis)")
            break
        else:
            print(a,"+",b,"=",a+b)
            break
monopolyworp()
