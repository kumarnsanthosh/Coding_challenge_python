import random
godzilla = 100
kong = 100
heals = 0
guard = 0

def godzilla_attack():
    a = random.randint(10, 30)
    return a

def heal():
    h = random.randint(10, 25)
    return h
rounds = 1
def kong_attack():
    e = random.randint(10, 35)
    return e
print('Kong🦍 vs Godzilla🦖')
print(f'godzilla score is {godzilla}, kong score is {kong}')
while True:
    fight = input(f"Fight:").lower()
    if fight == 'a':
        ka = kong_attack()
        ga = godzilla_attack()
        if godzilla - ka < 0 or kong - ga < 0:
            godzilla += 0
            kong += 0
            if godzilla > kong:
                godzilla -= ka
                print(f"godzilla wins, godzilla score is {godzilla}, kong out of health")
                break
            else:
                kong -= ga
                print(f"kong wins, kong score is {kong}, godzilla out of health ")
                break
        else:
            godzilla -= ka
            kong -= ga
            print(f'godzilla score is {godzilla}, kong score is {kong}')
    elif fight == 'd':
        if godzilla <= 0 and godzilla < kong:
            print(f"kong wins, kong score is {kong}, godzilla out of health")
            break
        elif kong <= 0 and kong < godzilla:
            print(f"godzilla wins, godzilla score is {godzilla}, kong out of health")
            break
        ka = kong_attack()
        g = int(ka / 2)
        if guard < 3:
            kong -= random.randint(1, g)
            godzilla -= g
            guard += 1
            print(f'godzilla score is {godzilla}, kong score is {kong}')
        else:
            print('Out of guard')
    elif fight == 'h':
        if heals < 3:
            if godzilla < 80 and kong < 80:
                godzilla += heal()
                kong += heal()
                print(f'godzilla score is {godzilla}, kong score is {kong}')
            elif kong > 80 or godzilla > 80:
                kong += 0
                godzilla += 0
                print(f'Alredy health more than 80%')
        else:
             print("Out of heals") 
        heals += 1
    else:
         print("Enter the right command, attack, defend or heal")
    



    
    
    

        
        


