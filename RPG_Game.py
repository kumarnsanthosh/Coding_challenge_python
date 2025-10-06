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
print('Welcome to the game! Kong🦍 vs Godzilla🦖')
while True:
    print(f'godzilla score is {godzilla}, kong score is {kong}')
    fight = input(f"Fight:").lower()
    if fight == 'a' and godzilla > 0 and kong > 0:
        godzilla -= kong_attack()
        kong -= godzilla_attack()
        if godzilla <= 0 and godzilla < kong:
            print(f"kong wins, kong score is {kong}, godzilla out of health")
            break
        elif kong <= 0 and kong < godzilla:
            print(f"godzilla wins, godzilla score is {godzilla}, kong out of health")
            break
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
            else:
                print('Out of guard')
    elif fight == 'h':
        if heals < 3:
            if godzilla < 80 or kong < 80:
                godzilla += heal()
                kong += heal()
                heals += 1
            elif kong > 80 or godzilla > 80:
                kong += 0
                godzilla += 0
                print(f'Alredy health more than 80%')
        else:
             print("Out of heals") 
    else:
         print("Enter the right command, attack, defend or heal")



    
    
    

        
        


