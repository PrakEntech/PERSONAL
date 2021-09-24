import os,time
from random import randint

cm=[["Flare Blitz",90,70,2,"Recoil - 33%"],
   ["Dragon Rage",0.4,90,5,""],
   ["Wing Attack",60,90,3,""],
   ["Fire Fang",65,85,5,"Burned - 30%"]]
Charizard = {"speed":100, "HP":245,"HP_Cur":245, "Type":"Fire","Moves":cm}

im=[["Mach Punch",40,90,5,""],
   ["Flame Wheel",60,90,5,"Burned - 10%"],
   ["Fire Spin",35,85,4,""],
   ["Acrobatics",55,90,3,""]]
Infernape = {"speed":108, "HP":242,"HP_Cur":242, "Type":"Fire","Moves":im}

mm=[["Hyper Beam",90,70,1,""],
   ["Fire Punch",75,90,4,"Burned - 10%"],
   ["Ember",40,100,5,""],
   ["Lava Plume",80,80,4,"Burned - 30%"]]
Magmortar = {"speed":83, "HP":240,"HP_Cur":240, "Type":"Fire","Moves":mm}

lm=[["Leaf Blade",90,70,2,""],
   ["Synthesis",0,100,4,"Regen - 33%"],
   ["Quick Attack",40,100,5,""],
   ["Magical Leaf",60,90,2,""]]
Leafeon = {"speed":95, "HP":223,"HP_Cur":223, "Type":"Grass","Moves":lm}

dm=[["Sucker Punch",70,90,3,""],
   ["Razor Leaf",55,95,3,"Critical Hit - 12.5%"],
   ["Peck",35,90,5,""],
   ["Leafage",40,90,4,""]]
Decidueye = {"speed":70, "HP":245,"HP_Cur":245, "Type":"Grass","Moves":dm}

vm=[["Petal Blizzard",90,70,1,""],
   ["Tackle",40,90,5,""],
   ["Vine Whip",45,90,5,""],
   ["Take Down",90,85,2,""]]
Venusaur = {"speed":80, "HP":249,"HP_Cur":249, "Type":"Grass","Moves":vm}

gm=[["Water Pulse",60,95,4,""],
   ["Night Slash",70,80,4,""],
   ["Hydro Pump",90,80,1,""],
   ["Quick Attack",40,100,5,""]]
Greninja = {"speed":122, "HP":235,"HP_Cur":235, "Type":"Water","Moves":gm}

gym=[["Twister",40,100,5,"Flinch - 30%"],
   ["Ice Fang",65,95,4,""],
   ["Aqua Tail",90,80,2,""],
   ["Blizzard",90,70,2,""]]
Gyarados = {"speed":81, "HP":274,"HP_Cur":274, "Type":"Water","Moves":gym}

bm=[["Water Gun",40,100,5,""],
   ["Bite",60,90,4,"Flinch - 30%"],
   ["Skull Bash",90,90,2,""],
   ["Flash Cannon",80,80,2,""]]
Blastoise = {"speed":78, "HP":247,"HP_Cur":247, "Type":"Water","Moves":bm}

mom=[["Gust",40,100,5,""],
   ["Ancient Power",60,90,4,""],
   ["Incinerate",60,90,2,""],
   ["Heat Wave",95,80,1,"Burned - 10%"]]
Moltres = {"speed":90, "HP":290,"HP_Cur":290, "Type":"Fire","Moves":mom}

sm=[["Extrasensory",80,90,2,"Flinch - 10%"],
   ["Surf",90,90,2,""],
   ["Water Gun",40,100,5,""],
   ["Facade",70,90,2,""]]
Suicune = {"speed":85, "HP":310,"HP_Cur":310, "Type":"Water","Moves":sm}

fm=[["Metal Claw",50,95,4,""],
   ["Power Whip",120,80,2,""],
   ["Knock Off",65,90,3,""],
   ["Tackle",40,100,5,""]]
Ferrothorn = {"speed":20, "HP":258,"HP_Cur":258, "Type":"Grass","Moves":fm}

rm=[["Spark",65,90,4,"Flinch - 30%"],
   ["Zap Cannon",120,80,1,""],
   ["Thunder Shock",40,100,5,"Flinch - 10%"],
   ["Howl",0,100,5,"User's Attack - 10"]]
Raikou = {"speed":115, "HP":290,"HP_Cur":290, "Type":"Electric","Moves":rm}

manm=[["Tackle",40,100,5,""],
   ["Discharge",80,95,2,"Flinch - 30%"],
   ["Thunder Fang",65,95,4,"Flinch - 10%"],
   ["Quick Attack",40,100,5,""]]
Manectric = {"speed":105, "HP":250,"HP_Cur":250, "Type":"Electric","Moves":manm}

elm=[["Rising Voltage",70,90,3,""],
   ["Thunder Punch",75,95,2,""],
   ["Quick Attack",40,100,5,""],
   ["Thunder",110,80,2,"Flinch - 30%"]]
Electivire = {"speed":95, "HP":260,"HP_Cur":260, "Type":"Electric","Moves":elm}

zm=[["Pluck",60,95,4,""],
   ["Drill Peck",80,90,2,""],
   ["Zap Cannon",120,80,1,""],
   ["Thunderbolt",90,85,3,"Flinch - 10%"]]
Zapdos = {"speed":100, "HP":290,"HP_Cur":290, "Type":"Electric","Moves":zm}

tm=[["Rock Slide",75,90,3,"Flinch - 30%"],
   ["Stone Edge",100,80,3,"Critical Hit - 12.5%"],
   ["Stomp",65,100,3,""],
   ["Scary Face",0,100,5,"Decrease in Rival Pokemon's Speed by 25"]]
Tyranitar = {"speed":61, "HP":310,"HP_Cur":310, "Type":"Rock","Moves":tm}

lycm=[["Howl",0,100,5,"User's Attack - 10"],
   ["Accelerock",40,100,5,""],
   ["Rock Throw",50,90,5,""],
   ["Rock Tomb",60,95,3,"Decrease in Rival Pokemon's Speed by 15"]]
Lycanroc = {"speed":112, "HP":260,"HP_Cur":260, "Type":"Rock","Moves":lycm}

gigam=[["Smack Down",50,95,5,""],
   ["Power Gem",80,90,3,""],
   ["Tackle",40,100,5,""],
   ["Take Down",90,85,4,"Recoil - 25%"]]
Gigalith = {"speed":25, "HP":280,"HP_Cur":280, "Type":"Rock","Moves":gigam}

rhym=[["Horn Attack",65,95,3,""],
   ["Rock Slide",75,90,3,"Flinch - 30%"],
   ["Scary Face",0,100,5,"Decrease in Rival Pokemon's Speed by 25"],
   ["Earthquake",100,90,2,""]]
Rhyperior = {"speed":40, "HP":340,"HP_Cur":340, "Type":"Rock","Moves":rhym}

probdict = {100: [1, 1], 95: [19, 20], 85: [17, 20], 90: [9, 10], 80: [4, 5], 70: [7, 10], 30: [3, 10], 33: [33, 100], 10: [1, 10], 12.5: [1, 8]}
pw,cw=0,0
def strlist(a):
    if a=='':return ['','']
    l=['','']
    for i in range(len(a)):
        if a[i].isalpha():l[0]+=a[i]
        elif a[i].isnumeric():l[1]+=a[i]
    l[1]=int(l[1])
    return l
def PokeAdvan(p,x):
    c={'Fire':0,'Grass':1,'Water':2}
    if p=='Rock':
        if x=='Fire':return 1
        if x in ['Water','Grass']:return -1
        else:return 0
    if x=='Rock':
        if p=='Fire':return -1
        if p in ['Water','Grass']:return 1
        else:return 0
    if p=='Electric':
        if x=='Grass':return -1
        elif x=='Water':return 1
        else:return 0
    if x=='Electric':
        if p=='Grass':return 1
        elif p=='Water':return -1
        else:return 0
    p,x=c[p],c[x]
    if (p-x== -1) or (p-x== 2): return 1
    elif (p-x== 1) or (p-x== -2): return -1
    else:return 0
def lifeBar(a,b):return '|'+'_'*int(round((a/b * 20),0))+'|'
pb,cb=[None,None],[None,None]
pf,cf=0,0
print("Pokemon Battle By - Prakhar")
pokemonList=["Charizard","Infernape","Magmortar","Moltres","Venusaur","Leafeon","Decidueye","Ferrothorn","Blastoise","Gyarados","Greninja","Suicune","Raikou","Manectric","Electivire","Zapdos","Lycanroc","Tyranitar","Gigalith","Rhyperior"]
pokedataList=[Charizard,Infernape,Magmortar,Moltres,Venusaur,Leafeon,Decidueye,Ferrothorn,Blastoise,Gyarados,Greninja,Suicune,Raikou,Manectric,Electivire,Zapdos,Lycanroc,Tyranitar,Gigalith,Rhyperior]

m=4
curP,curC = None,None
condition='y'
while condition=='y':
    c=4
    while c>2:
        c=int(input('0. Start\n1. List All Pokemons\n2. Exit\n'))
        if c==0:
            os.system('clear')
            pl=[None,None,None,"NOW"]
            cp=[None,None,None,"NOW"]
            while(cp[0]==cp[1] or cp[0]==cp[2])or cp[1]==cp[2]:
                for i in range(3):cp[i] = pokemonList[randint(0,18)]
            while(pl[0]==pl[1] or pl[0]==pl[2])or pl[1]==pl[2]:
                for i in range(3):pl[i] = pokemonList[randint(0,18)]
            break
        elif c==1:
            os.system('clear')
            for i in pokemonList:
                print(i,end='\n')
            input('Press Enter to Exit...')
            os.system('clear')
            c=4
            continue
        elif c==2:exit()

    for z in range(1,4):
        m=4
        if z==1:
            print("Your Partners -\n0. "+pl[0]+"\n1. "+pl[1]+"\n2. "+pl[2])
            while m>2:
                m=int(input("\nChoose your Pokemon for Battle "+str(z)+" - "))
            pl[-1] = pl[m]
            print(pl[-1]+", I choose You.")
            cp[-1]=cp[randint(0,2)]
            time.sleep(1)
        elif z==2:
            print("Your Partners -\n0. "+pl[0]+"\n1. "+pl[1])
            while m>1:
                m=int(input("\nChoose your Pokemon for Battle "+str(z)+" - "))
            pl[-1] = pl[m]
            print(pl[-1]+", I choose You.")
            cp[-1]=cp[randint(0,1)]
            time.sleep(1)
        else:
            pl[-1] = pl[0]
            cp[-1] = cp[0]
            print(pl[-1]+", I choose You.")
            time.sleep(1)
        print("Your Rival choose, "+cp[-1]+'\n')
        time.sleep(1)
        for i in range(len(pokemonList)):
            if pl[-1] == pokemonList[i]:curP = dict(pokedataList[i])
        for i in range(len(pokemonList)):
            if cp[-1] == pokemonList[i]:curC = dict(pokedataList[i])

        tA = PokeAdvan(curP["Type"],curC["Type"])
        if tA==1:
            for i in range(4):
                if int(curP["Moves"][i][1])!=0:curP["Moves"][i][1]+=5
            print("Your Pokemon has a Type Advantage.")
        if tA==-1:
            for i in range(4):
                if int(curC["Moves"][i][1]!=0):curC["Moves"][i][1]+=5
            print("Your Pokemon has a Type Disadvantage.")
        time.sleep(1)
        while True:
            os.system('clear')
            a="\n\nCPU - "+cp[-1]+'('+curC["Type"]+')'+" - "+lifeBar(curC["HP_Cur"],curC["HP"])+"("+str(curC["HP_Cur"])+"/"+str(curC["HP"])+")\n\nPLY - "+pl[-1]+'('+curP["Type"]+')'+" - "+lifeBar(curP["HP_Cur"],curP["HP"])+"("+str(curP["HP_Cur"])+"/"+str(curP["HP"])+""")

Moves -
0. """+curP["Moves"][0][0]+" - P  - "+str(curP["Moves"][0][1])+", A  - "+str(curP["Moves"][0][2])+"%, PP - "+str(curP["Moves"][0][3])+" times "+curP["Moves"][0][4]+"""
1. """+curP["Moves"][1][0]+" - P  - "+str(curP["Moves"][1][1])+", A  - "+str(curP["Moves"][1][2])+"%, PP - "+str(curP["Moves"][1][3])+" times "+curP["Moves"][1][4]+"""
2. """+curP["Moves"][2][0]+" - P  - "+str(curP["Moves"][2][1])+", A  - "+str(curP["Moves"][2][2])+"%, PP - "+str(curP["Moves"][2][3])+" times "+curP["Moves"][2][4]+"""
3. """+curP["Moves"][3][0]+" - P  - "+str(curP["Moves"][3][1])+", A  - "+str(curP["Moves"][3][2])+"%, PP - "+str(curP["Moves"][3][3])+" times "+curP["Moves"][3][4]
            print(a,end='\n')
            while True:
                pMove=4
                while pMove>3:pMove=int(input('\nYour Attack - '))
                if curP["Moves"][pMove][3]==0:
                    print('This Attack cannot be used more.',end='\n')
                    continue
                else:break
            if curP['speed']>curC['speed']:
                temp = probdict[curP["Moves"][pMove][2]]
                if randint(1,temp[1])<=temp[0]:
                    temp=strlist(curP["Moves"][pMove][4])
                    if 'ritical' in temp[0]:
                        temp=probdict[temp[1]/10]
                        if randint(1,temp[1])<=temp[0]:
                            print('Critical Hit By your Pokemon')
                            curC["HP_Cur"] -= 30
                            time.sleep(1)
                    elif 'ecoil' in temp[0]:
                        print('Your Pokemon suffered, Recoil Damage')
                        curP["HP_Cur"] -= temp[1]
                        time.sleep(1)
                    elif 'urned' in temp[0]:
                        temp=probdict[temp[1]]
                        if randint(1,temp[1])<=temp[0]:
                            cb=[1,randint(2,3)]
                            if cb[0]<=cb[1] and cb[0]!=0:
                                cb[0]+=1
                                if cb[0]==cb[1]:cb=[None,None]
                                print("Your Pokemon's Attack, caused a burn to "+cp[-1])
                                curC["HP_Cur"] -= 20
                            time.sleep(1)
                    elif 'linch' in temp[0]:
                        temp=probdict[temp[1]]
                        if randint(1,temp[1])<=temp[0]:
                            cf=1
                            time.sleep(1)
                    if curP["Moves"][pMove][1]!=0 and curP["Moves"][pMove][1]!=0.4:
                        if curP["Moves"][pMove][1]>0 and curP["Moves"][pMove][1]<1:
                            curC["HP_Cur"] -= int(curP["Moves"][pMove][1]*curC["HP"])
                            curP["Moves"][pMove][3]-=1
                        else:
                            curC["HP_Cur"]-=curP["Moves"][pMove][1]
                            curP["Moves"][pMove][3]-=1
                    elif curP["Moves"][pMove][1]==0.4:
                        curC["HP_Cur"] -= int((curC["HP"]*40)/100)
                        curP["Moves"][pMove][3]-=1
                    elif curP["Moves"][pMove][4]=="User's Attack - 10":
                        for i in range(3):curP["Moves"][i][1]+=10
                    elif curP["Moves"][pMove][4]=="Decrease in Rival Pokemon's Speed by 15":
                        curC["speed"]-=15
                        curC["HP_Cur"]-=curP["Moves"][pMove][1]
                    elif curP["Moves"][pMove][4]=="Decrease in Rival Pokemon's Speed by 25":curC["speed"]-=25
                    elif curP["Moves"][pMove][1]==0 and curP["HP_Cur"]>0:
                        curP["HP_Cur"] += int((curP["HP"]*33)/100)
                        if curP["HP_Cur"]>curP["HP"]:curP["HP_Cur"]=curP["HP"]
                        curP["Moves"][pMove][3]-=1
                    print('Your Attack - '+curP["Moves"][pMove][0])
                else:
                    print("YOUR POKEMON'S ATTACK MISSED!!!")
                    curP["Moves"][pMove][3]-=1
                time.sleep(1)
                if cf==0:
                    cpMove = randint(0,3)
                    temp = probdict[curC["Moves"][cpMove][2]]
                    if randint(1,temp[1])<=temp[0]:
                        temp=strlist(curC["Moves"][cpMove][4])
                        if 'ritical' in temp[0]:
                            temp=probdict[temp[1]/10]
                            if randint(1,temp[1])<=temp[0]:
                                print('Critical Hit By '+cp[-1])
                                curP["HP_Cur"] -= 30
                                time.sleep(1)
                        elif 'ecoil' in temp[0]:
                            print(cp[-1]+' suffered, Recoil Damage')
                            curP["HP_Cur"] -= temp[1]
                            time.sleep(1)
                        elif 'urned' in temp[0]:
                            temp=probdict[temp[1]]
                            if randint(1,temp[1])<=temp[0]:
                                pb=[1,randint(2,3)]
                                if pb[0]<=pb[1] and pb[0]!=0:
                                    pb[0]+=1
                                    if pb[0]==pb[1]:pb=[None,None]
                                    print(cp[-1]+"'s Attack, caused a burn to your Pokemon")
                                    curP["HP_Cur"] -= 20
                                time.sleep(1)
                        if curC["HP_Cur"]>=0:print(cp[-1]+' used '+curC["Moves"][cpMove][0])
                        if (curC["Moves"][cpMove][1]!=0 and curC["HP_Cur"]>=0)and curC["Moves"][cpMove][1]!=0.4:
                            if curC["Moves"][cpMove][1]>0 and curC["Moves"][cpMove][1]<1:
                                curP["HP_Cur"] -= int(curC["Moves"][cpMove][1]*curP["HP"])
                                curC["Moves"][cpMove][3]-=1
                            else:
                                curP["HP_Cur"]-=curC["Moves"][cpMove][1]
                                curC["Moves"][cpMove][3]-=1
                        elif curC["Moves"][cpMove][1]==0.4:
                            curP["HP_Cur"] -= int((curP["HP"]*40)/100)
                            curC["Moves"][cpMove][3]-=1
                        elif curC["Moves"][cpMove][4]=="User's Attack - 10":
                            for i in range(3):curC["Moves"][i][1]+=10
                        elif curC["Moves"][cpMove][4]=="Decrease in Rival Pokemon's Speed by 15":
                            curP["speed"]-=15
                            curP["HP_Cur"]-=curC["Moves"][cpMove][1]
                        elif curC["Moves"][cpMove][4]=="Decrease in Rival Pokemon's Speed by 25":curP["speed"]-=25
                        elif curC["Moves"][cpMove][1]==0 and curC["HP_Cur"]>0:
                            curC["HP_Cur"] += int((curC["HP"]*33)/100)
                            if curC["HP_Cur"]>curC["HP"]:curC["HP_Cur"]=curC["HP"]
                            curC["Moves"][cpMove][3]-=1
                    else:
                        print("RIVAL POKEMON'S ATTACK MISSED!!!")
                        curC["Moves"][cpMove][3]-=1
                    time.sleep(1)
                else:
                    cf=0
                    print(pl[-1]+"'s Attack, flinched "+cp[-1])
            else:
                cpMove = randint(0,3)
                temp = probdict[curC["Moves"][cpMove][2]]
                if randint(1,temp[1])<=temp[0]:
                    temp=strlist(curC["Moves"][cpMove][4])
                    if 'ritical' in temp[0]:
                        temp=probdict[temp[1]/10]
                        if randint(1,temp[1])<=temp[0]:
                            print('Critical Hit By '+cp[-1])
                            curP["HP_Cur"] -= 30
                            time.sleep(1)
                    elif 'ecoil' in temp[0]:
                        print(cp[-1]+' suffered, Recoil Damage')
                        curP["HP_Cur"] -= temp[1]
                        time.sleep(1)
                    elif 'linch' in temp[0]:
                        temp=probdict[temp[1]]
                        if randint(1,temp[1])<=temp[0]:
                            pf=1
                            time.sleep(1)
                    elif 'urned' in temp[0]:
                        temp=probdict[temp[1]]
                        if randint(1,temp[1])<=temp[0]:
                            pb=[1,randint(2,3)]
                            if pb[0]<=pb[1] and pb[0]!=0:
                                pb[0]+=1
                                if pb[0]==pb[1]:pb=[None,None]
                                print(cp[-1]+"'s Attack, caused a burn to your Pokemon")
                                curP["HP_Cur"] -= 20
                            time.sleep(1)
                    if curC["HP_Cur"]>=0:print(cp[-1]+' used '+curC["Moves"][cpMove][0])
                    if (curC["Moves"][cpMove][1]!=0 and curC["HP_Cur"]>=0)and curC["Moves"][cpMove][1]!=0.4:
                        if curC["Moves"][cpMove][1]>0 and curC["Moves"][cpMove][1]<1:
                            curP["HP_Cur"] -= int(curC["Moves"][cpMove][1]*curP["HP"])
                            curC["Moves"][cpMove][3]-=1
                        else:
                            curP["HP_Cur"]-=curC["Moves"][cpMove][1]
                            curC["Moves"][cpMove][3]-=1
                    elif curC["Moves"][cpMove][1]==0.4:
                        curP["HP_Cur"] -= int((curP["HP"]*40)/100)
                        curC["Moves"][cpMove][3]-=1
                    elif curC["Moves"][cpMove][4]=="User's Attack - 10":
                        for i in range(3):curC["Moves"][i][1]+=10
                    elif curC["Moves"][cpMove][4]=="Decrease in Rival Pokemon's Speed by 15":
                        curP["speed"]-=15
                        curP["HP_Cur"]-=curC["Moves"][cpMove][1]
                    elif curC["Moves"][cpMove][4]=="Decrease in Rival Pokemon's Speed by 25":curP["speed"]-=25
                    elif curC["Moves"][cpMove][1]==0 and curC["HP_Cur"]>0:
                        curC["HP_Cur"] += int((curC["HP"]*33)/100)
                        if curC["HP_Cur"]>curC["HP"]:curC["HP_Cur"]=curC["HP"]
                        curC["Moves"][cpMove][3]-=1
                else:
                    print("RIVAL POKEMON'S ATTACK MISSED!!!")
                    curC["Moves"][cpMove][3]-=1
                time.sleep(1)
                if pf==0:
                    temp = probdict[curP["Moves"][pMove][2]]
                    if randint(1,temp[1])<=temp[0]:
                        temp=strlist(curP["Moves"][pMove][4])
                        if 'ritical' in temp[0]:
                            temp=probdict[temp[1]/10]
                            if randint(1,temp[1])<=temp[0]:
                                print('Critical Hit By your Pokemon')
                                curC["HP_Cur"] -= 30
                                time.sleep(1)
                        elif 'ecoil' in temp[0]:
                            print('Your Pokemon suffered, Recoil Damage')
                            curP["HP_Cur"] -= temp[1]
                            time.sleep(1)
                        elif 'urned' in temp[0]:
                            temp=probdict[temp[1]]
                            if randint(1,temp[1])<=temp[0]:
                                cb=[1,randint(2,3)]
                                if cb[0]<=cb[1] and cb[0]!=0:
                                    cb[0]+=1
                                    if cb[0]==cb[1]:cb=[None,None]
                                    print("Your Pokemon's Attack, caused a burn to "+cp[-1])
                                    curC["HP_Cur"] -= 20
                                time.sleep(1)
                        if (curP["Moves"][pMove][1]!=0 and curP["HP_Cur"]>=0)and curP["Moves"][pMove][1]!=0.4:
                            if curP["Moves"][pMove][1]>0 and curP["Moves"][pMove][1]<1:
                                curC["HP_Cur"] -= int(curP["Moves"][pMove][1]*curC["HP"])
                                curP["Moves"][pMove][3]-=1
                            else:
                                curC["HP_Cur"]-=curP["Moves"][pMove][1]
                                curP["Moves"][pMove][3]-=1
                        elif curP["Moves"][pMove][1]==0.4:
                            curC["HP_Cur"] -= int((curC["HP"]*40)/100)
                            curP["Moves"][pMove][3]-=1
                        elif curP["Moves"][pMove][4]=="User's Attack - 10":
                            for i in range(3):curP["Moves"][i][1]+=10
                        elif curP["Moves"][pMove][4]=="Decrease in Rival Pokemon's Speed by 15":
                            curC["speed"]-=15
                            curC["HP_Cur"]-=curP["Moves"][pMove][1]
                        elif curP["Moves"][pMove][4]=="Decrease in Rival Pokemon's Speed by 25":curC["speed"]-=25
                        elif curP["Moves"][pMove][1]==0 and curP["HP_Cur"]>0:
                            curP["HP_Cur"] += int((curP["HP"]*33)/100)
                            if curP["HP_Cur"]>curP["HP"]:curP["HP_Cur"]=curP["HP"]
                            curP["Moves"][pMove][3]-=1
                        if curP["HP_Cur"]>=0:print('Your Attack - '+curP["Moves"][pMove][0])
                    else:
                        print("YOUR POKEMON'S ATTACK MISSED!!!")
                        curP["Moves"][pMove][3]-=1
                    time.sleep(1)
                else:
                    pf=0
                    print(cp[-1]+"'s Attack, flinched "+pl[-1])

            if curP["HP_Cur"]<=0:
                pl.remove(pl[-1])
                cp.remove(cp[-1])
                pl[-1]="NOW"
                break
            elif curC["HP_Cur"]<=0:
                cp.remove(cp[-1])
                pl.remove(pl[-1])
                cp[-1]="NOW"
                break

        if pl[-1]=="NOW":
            cp[-1]="NOW"
            print("\nYour Rival WON Battle "+str(z)+".")
            cw+=1
        elif cp[-1]=="NOW":
            pl[-1]="NOW"
            print("\nYou WON Battle "+str(z)+".")
            pw+=1
        time.sleep(1)
        os.system('clear')


    if pw>cw:print("WINNER - PLAYER\nCongratulations, You are now 1 step closer to become\nTHE BEST POKEMON TRAINER")
    else:print("WINNER - COMPUTER\nHey PLAYER, that was a close Battle, Better Luck Next Time")
    condition = input('Do you want to play again(y/n) - ')
    os.system('clear')
