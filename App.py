import os
import sys
import random
import pickle
import re

sys.setrecursionlimit(10000000)
weapons = {"Iron Sword":50, "Bronze Sword":100, "Steel Sword":300, "Ebon Sword": 350, "Iron Greatsword":400, "Bronze Greatsword": 500, "Steel Greatsword": 550, "Ebon Greatsword": 600}
armour = {"Cheap Gambeson":50, "Iron Chainmail": 75, "Steel Chainmail": 125, "Ebon Chainmail": 200, "Iron Plate": 300, "Steel Plate": 400, "Ebon Plate": 500}
Spells = {"Fireball":350, "Heal":150}


class player:
    def __init__(self, name):
        self.name = name
        self.Race = "Human"
        self.Location = 'Town'
        self.Gold = 50
        self.MaxXP = 50
        self.EXP = 0
        self.BaseDefense = 0
        self.MaxHealth = 50
        self.Health = self.MaxHealth
        self.MaxArcana = 50
        self.Arcana = self.MaxArcana
        self.BaseAttack = 5
        self.pots = 0
        self.ArcanaPots = 0
        self.SpellList = []
        self.MiscInventory = []
        self.weap = ["Rusty Sword"]
        self.curweap = "Rusty Sword"
        self.armour = ["Clothing"]
        self.CurArmour = "Clothing"
    @property
    def Attack(self):
        Attack = self.BaseAttack
        if(PlayerIG.Race == "Dwarf"):
            Attack+=2
        if(self.curweap == "Rusty Sword"):
            Attack+=0
        if(self.curweap == "Iron Sword"):
            Attack+=5
        if(self.curweap == "Bronze Sword"):
            Attack+=7
        if(self.curweap == "Steel Sword"):
            Attack+=10
        if(self.curweap == "Ebon Sword"):
            Attack+=15
        if(self.curweap == "Iron Greatsword"):
            Attack+=20
        if (self.curweap == "Bronze Greatsword"):
            Attack+=25
        if(self.curweap == "Steel Greatsword"):
            Attack+=30
        if(self.curweap == "Ebon Greatsword"):
            Attack+=35
        if(self.curweap == "Forest Blade"):
            Attack+=40
        if (self.curweap == "Shadow Blade"):
            Attack+=50
        if (self.curweap == "Winter Blade"):
            Attack+=45
        if (self.curweap == "God-Slayer"):
            Attack+=85
        return Attack

    @property
    def Defense(self):
        Defense = self.BaseDefense
        if(PlayerIG.Race == "Dwarf"):
            Defense+=1
        if(self.CurArmour == "Cheap Gambeson"):
            Defense+=2
        if(self.CurArmour == "Iron Chainmail"):
            Defense+=3
        if(self.CurArmour == "Steel Chainmail"):
            Defense+=5
        if(self.CurArmour == "Ebon Chainmail"):
            Defense+=7
        if(self.CurArmour == "Iron Plate"):
            Defense+=10
        if(self.CurArmour == "Steel Plate"):
            Defense+=15
        if(self.CurArmour == "Ebon Plate"):
            Defense+=25
        return Defense

        
class Goblin:
    def __init__(self, name):
        self.name = name
        self.Gold = 15
        self.MaxHealth = 65
        self.Health = self.MaxHealth
        self.Attack = 5
        self.EXP = 20
GoblinIG = Goblin("Goblin")
class GoblinBoss:
    def __init__(self, name):
        self.name = name
        self.Gold = 1000
        self.MaxHealth = 200
        self.Health = self.MaxHealth
        self.Attack = 50
        self.EXP = 500
GoblinBossIG = GoblinBoss("Goblin King")

class TimberWolf:
    def __init__(self, name):
        self.name = name
        self.Gold = 25
        self.MaxHealth = 75
        self.Health = self.MaxHealth
        self.Attack = 5
        self.EXP = 25
TimberIG = TimberWolf("Timber Wolf")
class BrownBear:
    def __init__(self, name):
        self.name = name
        self.Gold = 30
        self.MaxHealth = 75
        self.Health = self.MaxHealth
        self.Attack = 7
        self.EXP = 45
BrownBearIG = BrownBear("Brown Bear")

class Troll:
    def __init__(self, name):
        self.name = name
        self.Gold = 50
        self.MaxHealth = 175
        self.Health = self.MaxHealth
        self.Attack = 35
        self.EXP = 75
TrollIG = Troll("Frost Troll")
class SnowWolf:
    def __init__(self, name):
        self.name = name
        self.Gold = 35
        self.MaxHealth = 150
        self.Health = self.MaxHealth
        self.Attack = 25
        self.EXP = 45
SnowWolfIG = SnowWolf("Snow Wolf")
class SnowWolfBoss:
    def __init__(self, name):
        self.name = name
        self.Gold = 1000
        self.MaxHealth = 400
        self.Health = self.MaxHealth
        self.Attack = 45
        self.EXP = 500
SnowWolfBossIG = SnowWolfBoss("Frost Werewolf")
class Skeleton:
    def __init__(self, name):
        self.name = name
        self.Gold = 125
        self.MaxHealth = 150
        self.Health = self.MaxHealth
        self.Attack = 55
        self.EXP = 125
SkeletonIG = Skeleton("Skeleton")
class SkeletonMinion:
    def __init__(self, name):
        self.name = name
        self.Gold = 0
        self.MaxHealth = 125
        self.Health = self.MaxHealth
        self.Attack = 45
        self.EXP = 0
SkeletonMIG = SkeletonMinion("Skeleton")
class NecromancerBoss:
    def __init__(self, name):
        self.name = name
        self.Gold = 1000
        self.MaxHealth = 500
        self.Health = self.MaxHealth
        self.Attack = 65
        self.EXP = 500
NecromancerBossIG = NecromancerBoss("Necromancer Lord")
class Necromancer:
    def __init__(self, name):
        self.name = name
        self.Gold = 125
        self.MaxHealth = 200
        self.Health = self.MaxHealth
        self.Attack = 85
        self.EXP = 85
NecromancerIG = Necromancer("Necromancer")
class Thug:
    def __init__(self, name):
        self.name = name
        self.Gold = 25
        self.MaxHealth = 55
        self.Health = self.MaxHealth
        self.Attack = 3
        self.EXP = 35
ThugIG = Thug("Thug")
def Start():
    os.system("clear")
    print("Let's Create your Character")
    option = raw_input("Name: ")
    global PlayerIG
    PlayerIG = player(option)
    if (len(PlayerIG.name) == 0):
        Start()
    Start0()
def Start0():
    os.system('clear')
    print("1)Dwarf")
    print("2)Elf")
    print("3)Human")
    option = raw_input("Race: ")
    if (option == "1"):
        PlayerIG.Race = "Dwarf"
    elif(option == "2"):
        PlayerIG.Race = "Elf"
    elif(option == "3"):
        PlayerIG.Race = "Human"
    else:
        Start0()
    if (len(PlayerIG.Race) >= 3):
        Start1()
    
def Tavern():
    os.system('clear')
    print("Innkeeper: Welcome! Tell me if you need anything")
    print("1)Rest[5g]")
    print("2)Tavern Games")
    print("3)Leave")
    option = raw_input("-->")
    if (option == "1"):
        if (PlayerIG.Gold >= 5):
            if (PlayerIG.Health == PlayerIG.MaxHealth and PlayerIG.Arcana == PlayerIG.MaxArcana):
                os.system('clear')
                print("You are already well rested")
                option = raw_input('')
                Tavern()
            else:
                PlayerIG.Gold -= 5
                PlayerIG.Health = PlayerIG.MaxHealth
                PlayerIG.Arcana = PlayerIG.MaxArcana
                print("You rested. Health and Arcana Replenished...")
                option = raw_input("")
                Tavern()
        else:
            print("You don't have the gold needed to rest...")
            option = raw_input("")
            Tavern()
    elif (option == "3"):
        print("You leave the tavern...")
        option = raw_input("")
        Start1()
    elif (option == "2"):
        TavernGames()
    else:
        Tavern()
def ProphetDice():
    os.system('clear')
    if (PlayerIG.Gold < 30):
        print("You don't have enough to  bet...")
        option = raw_input('')
        Tavern()
    print("Place a bet between 30 and %s"%(PlayerIG.Gold/2))
    option = raw_input('--->')
    if (re.search('[a-zA-Z]', option)):
        option = 1
    if (int(option) < 30 or int(option) > PlayerIG.Gold/2):
        ProphetDice()
    elif (int (option) >= 30 and int (option) < PlayerIG.Gold):
        global Bet
        Bet = int(option)
        ProphetDice2()
    else:
        ProphetDice()
def ProphetDice3():
    os.system('clear')
    DiceRoll1 = random.randint(1, 12)
    DiceRoll2 = random.randint(1, 12)
    print("You roll a %s"%(DiceRoll1))
    print("Do you think the opponent roll will be: ")
    print("1)Higher")
    print("2)Lower")
    print("3)Equal[Triples Bet]")
    print("_________________")
    option = raw_input('-->')
    if (option == "1"):
        if (DiceRoll1 < DiceRoll2):
            os.system('clear')
            print("You won %s Gold!"%(Bet*2))
            PlayerIG.Gold+=Bet*2
            option = raw_input('')
            Tavern()
        else:
            os.system('clear')
            print("You lost %s Gold..."%(Bet*2))
            PlayerIG.Gold-=Bet*2
            if (PlayerIG.Gold < 0):
                PlayerIG.Gold = 0
            option = raw_input('')
            Tavern()
    elif (option == "2"):
        if (DiceRoll1 > DiceRoll2):
            os.system('clear')
            print("You won %s Gold!"%(Bet*2))
            PlayerIG.Gold+=Bet*2
            option = raw_input('')
            Tavern()
        else:
            os.system('clear')
            print("You lost %s Gold..."%(Bet*2))
            PlayerIG.Gold-=Bet*2
            if (PlayerIG.Gold < 0):
                PlayerIG.Gold = 0
            option = raw_input('')
            Tavern()
    elif (option == "3"):
        if (DiceRoll1 == DiceRoll2):
            os.system('clear')
            print("You won %s Gold!"%(Bet*3))
            PlayerIG.Gold+=Bet*3
            option = raw_input('')
            Tavern()
        else:
            os.system('clear')
            print("You lost %s Gold..."%(Bet*3))
            PlayerIG.Gold-=Bet*3
            if (PlayerIG.Gold < 0):
                PlayerIG.Gold = 0
            option = raw_input('')
            Tavern()
    else:
        ProphetDice3()
def ProphetDice2():
    os.system('clear')
    print('Your bet is %s correct?'%(Bet))
    option = raw_input("Y/N: ")
    if (option == "Y" or option == "y"):
        ProphetDice3()
    elif (option == "N" or option == "n"):
        ProphetDice()
    else: 
        ProphetDice2()
def TavernGames():
    os.system('clear')
    print("1)Prophets Dice")
    print("E)Exit")
    option = raw_input("-->")
    if (option == "1"):
        ProphetDice()
    elif (option =="e" or option == "E"):
        Tavern()
    else:
        TavernGames()
def Equip():
    os.system('clear')
    print("|------------------|")
    print("|      Weapons     |")
    print("|------------------|")
    for weapon in PlayerIG.weap:
        print ("-"+weapon)
    print("|------------------|")
    print("|      Armour      |")
    print("|------------------|")
    for armour in PlayerIG.armour:
        print ("-"+armour)
    print("E)Exit Menu")
    option = raw_input('-->')
    if (option == PlayerIG.curweap):
        os.system('clear')
        print("That weapon is already equipped...")
        option = raw_input('')
        Equip()
    elif (option == "E" or option == "e"):
        os.system('clear')
        print("You Leave the menu...")
        option = raw_input('')
        Inventory()
    elif (option in PlayerIG.weap):
        os.system('clear')
        PlayerIG.curweap = option
        print ("You have equipped a %s"% (option))
        option = raw_input('')
        Equip()
    elif (option in PlayerIG.armour):
        os.system('clear')
        PlayerIG.CurArmour = option
        print ("You have equipped a %s"% (option))
        option = raw_input('')
        Equip()
    else:
        os.system('clear')
        print('You do not have that item')
        option = raw_input('')
        Equip()
        
      
def MiscInventory():
    os.system('clear')
    for item in PlayerIG.MiscInventory:
        print("-"+item)
    print("E)Exit")
    option = raw_input('')
    if (option == "e" or option == "E"):
        Inventory()
    else:
        MiscInventory()
def Inventory():
    os.system('clear')
    print("1)Equipment")
    print("2)Misc")
    print("E)Exit Menu")
    option = raw_input('-->')
    if (option == "1"):
        Equip()
    elif (option == "2"):
        MiscInventory()
    elif (option == "E" or option == "e"):
        os.system('clear')
        print("Leaving Inventory...")
        option = raw_input('')
        Start1()
    else:
        Inventory()
def SpellList():
    os.system('clear')
    for Spells in PlayerIG.SpellList:
        print ("-" + Spells)
    option = raw_input('')
    Magic()
def MagicAcademy():
    os.system("clear")
    print("Gold: %s Potion: %s"%(PlayerIG.Gold, PlayerIG.ArcanaPots))
    print("|-------------|")
    print("|    Magic    |")
    print("|-------------|")    
    print("-Fireball[350g]")
    print("-Heal[150g]")
    print("|-------------|")
    print("|     Misc    |")
    print("|-------------|")
    print("M) Arcana Potion[150g]")
    print("E) Exit Academy")
    option = raw_input("-->")
    if (option in Spells):
        if (PlayerIG.Gold >= Spells[option] and option not in PlayerIG.SpellList):
            os.system('clear')
            PlayerIG.Gold -= Spells[option]
            PlayerIG.SpellList.append(option)
            print("You have purchased the %s Spell"% (option))
            option = raw_input('')
            MagicAcademy()
    elif (option == "E" or option == "e"):
        os.system('clear')
        print("Teacher: May the Arcane Arts serve you well!")
        option = raw_input('')
        Start1()
    elif (option == "M" or option == "m"):
        os.system('clear')
        if (PlayerIG.Gold >= 150):
            PlayerIG.Gold-=150
            PlayerIG.ArcanaPots+=1
            MagicAcademy()
        else:
            os.system('clear')
            print("You lack %s gold..."%(PlayerIG.Gold-150))
            raw_input('')
            MagicAcademy()
        Start1()
    else:
        MagicAcademy()
def Start1():
    os.system('clear')
    print("Name: " + PlayerIG.name)
    print("Race: " + PlayerIG.Race)
    print("EXP: %s/%s"% (PlayerIG.EXP, PlayerIG.MaxXP))
    print("Health: %i/%i" % (PlayerIG.Health, PlayerIG.MaxHealth))
    print("Arcana: %i/%i" % (PlayerIG.Arcana, PlayerIG.MaxArcana))
    print("Weapon: %s"%(PlayerIG.curweap))
    print("Armour: %s"%(PlayerIG.CurArmour))
    print("Attack: %i" % (PlayerIG.Attack))
    print("Defense: %i"%(PlayerIG.Defense))
    print("Gold: %i" % (PlayerIG.Gold))
    print("Health Potions: %i Arcana Potions: %i" % (PlayerIG.pots, PlayerIG.ArcanaPots))
    print("___________________________")
    print("1)Explore")
    print("2)Shop")
    print("3)Tavern")
    print("4)Inventory")
    print("5)Magic")
    print("7)Save")
    print("8)Exit")
    option = raw_input("-->")
    if (option == "1"):
        Explore()
    if (option == "2"):
        store()
    if (option == "3"):
        Tavern()
    if (option == "4"):
        Inventory()
    if (option == "5"):
        Magic()
    if (option == "6"):
        os.system('clear')
        with open ('savefile', 'wb') as f:
            pickle.dump(PlayerIG, f)
            print("Game saved...")
        option = raw_input('')
        Start1()
            
    if (option == "7"):
        Main()
    else:
        Start1()
def Magic():
    os.system('clear')
    print("1)Magic Academy")
    print("2)Spell List")
    print("---------------")
    print("E)Exit Menu")
    option = raw_input("-->")
    if(option == "1"):
        MagicAcademy()
    if(option == "2"):
        SpellList()
    elif(option == "E" or option == "e"):
        os.system('clear')
        print("Exiting Menu...")
        Start1()
    else:
        Magic()
def attack():
    os.system("clear")
    pAttack = random.randint(PlayerIG.Attack/2, PlayerIG.Attack)
    eAttack = random.randint(enemy.Attack/2, enemy.Attack)
    if(pAttack == PlayerIG.Attack/2):
        print("You Missed...")
    else:
        enemy.Health -= pAttack
        print("You deal %i damage"%(pAttack))
        
    if(eAttack == enemy.Attack/2):
        print("%s Missed..."%(enemy.name))
    else:
        PlayerIG.Health -= eAttack
        print("%s deals %i damage"%(enemy.name, eAttack))
    option = raw_input('')
    if (eAttack > PlayerIG.Defense and PlayerIG.Health != PlayerIG.MaxHealth and PlayerIG.Defense != 0):
        Defense = random.randint(PlayerIG.Defense/2, PlayerIG.Defense)
        PlayerIG.Health+=Defense
        print("You deflected %i Damage"%(Defense))
        if (PlayerIG.Health >= PlayerIG.MaxHealth):
            PlayerIG.Health = PlayerIG.MaxHealth
        option = raw_input('')
    os.system('clear')
    if (PlayerIG.Health <= 0):
        die()
    if (enemy.Health <= 0):
        win()
    else:
        fight()
def GoblinBossTalk():
    os.system('clear')
    print("You enter the chamber and hear a cackle...")
    option = raw_input("")
    print('Goblin King: "Ah, another adventurer *sigh what are you doing here?"')
    print("________________________________________________________")
    print("1)Attack")
    print("2)Bribe for Forest Blade")
    option = raw_input('--->')
    if (option == "1"):
        os.system('clear')
        print("Wanna do it that way? Ok time to die.")
        option = raw_input('')
        fight()
    elif (option == "2"):
        os.system('clear')
        GoblinBossTalk2()
def GoblinBossTalk2():
    if ("Forest Blade" in PlayerIG.weap):
        fight()
    print('Goblin King: "Hmm you want my sword? How much for it..."')
    print("__________________")
    print("Current Gold: %s"%(PlayerIG.Gold))
    print("1)100[g]")
    print("2)500[g]")
    print("3)1000[g]")
    print("4)2000[g]")
    option = raw_input('--->')
    if (option == "1"):
        os.system('clear')
        print("Only 100 Gold? Come on!")
        option = raw_input('')
        fight()
    elif (option == "2"):
        os.system('clear')
        print("Only 500 Gold? Come on!")
        option = raw_input('')
        fight()
    elif (option == "3" and PlayerIG.Gold >= 1000):
        GAC = random.randint(1,2)
        if (GAC == 1):
            print("Hmm... fine. Take it and leave.")
            PlayerIG.Gold-= 1000
            PlayerIG.weap.append('Forest Blade')
            print('You find the Forest Blade...')
            option = raw_input('')
            Start1()
        elif (GAC == 2):
            os.system('clear')
            print("Hmm...No... not enough...time to die.")
            option = raw_input('')
            fight()
    elif (option == "4" and PlayerIG.Gold >= 2000):
        print("Wait! 2000? Yes Yes take it and leave!")
        PlayerIG.Gold-= 2000
        PlayerIG.weap.append('Forest Blade')
        print("You find the Forest Blade...")
        option = raw_input('')
        Start1()
    else:
        GoblinBossTalk2()
def NecroPreFight():
    os.system('clear')
    print("Entering the chamber you see a man in black robes, with black eyes, eyeing you. ")
    print("He uses a grand staff to raise a skeleton at his feet")
    global enemy
    enemy = SkeletonMIG
    option = raw_input('')
    fight()
def Stronghold():
    os.system('clear')
    print("|-----------|")
    print("|Strongholds|")
    print("|-----------|")
    print("1)Forest Stronghold")
    print("2)Mountain Stronghold")
    print("3)Dungeon Stronghold")
    print("E)Exit Menu")
    option = raw_input('--->')
    if (option == "1"):
        PlayerIG.Location = "Forest Stronghold"
        global enemy
        enemy = GoblinBossIG
        GoblinBossTalk()
    elif (option == "2"):
        PlayerIG.Location = "Mountain Stronghold"
        global enemy
        enemy = SnowWolfBossIG
        fight()
    elif (option == "3"):
        PlayerIG.Location = "Dungeon Stronghold"
        global enemy
        NecroPreFight()
       
    elif (option == "E" or option == "e"):
        Explore()
    else:
        Stronghold()
def ArcaneSmith():
    os.system('clear')
    print("Hello, Adventurer!")
    print("1)Forge Godblade[10000g]")
    print("E)Exit")
    option = raw_input('-->')
    if (option == "1"):
        os.system('clear')
        if ("Shadow Blade" in PlayerIG.weap and "Winter Blade" in PlayerIG.weap and "Forest Blade" in PlayerIG.weap and PlayerIG.Gold >= 10000):
            print("You forged the God-Slayer...") 
            PlayerIG.Gold -= 10000
            PlayerIG.weap.remove('Winter Blade')
            PlayerIG.weap.remove('Shadow Blade')
            PlayerIG.weap.remove('Forest Blade')
            PlayerIG.weap.append('God-Slayer')
            if (PlayerIG.curweap == "Winter Blade" or PlayerIG.curweap == "Shadow Blade" or PlayerIG.curweap == "Forest Blade"):
                PlayerIG.curweap == "Rusty Sword"
            option = raw_input('')
            Explore()
        else:
            if ("Winter Blade" in PlayerIG.weap):
                pass
            else:
                print("You need the Winter Blade")
            
            if ("Forest Blade" in PlayerIG.weap):
                pass
            else:
                print("You need the Forest Blade")
            if ("Shadow Blade" in PlayerIG.weap):
                pass
            else:
                print("You need the Shadow Blade")
            if (PlayerIG.Gold <= 10000):
                print("You are missing %s Gold"%(10000 - PlayerIG.Gold))
            option = raw_input('')
            ArcaneSmith()
    elif(option == "e" or option == "E"):
        Explore()
    else:
        ArcaneSmith()

def Explore():
    os.system('clear')
    print("1)Forest")
    print("2)Mountains")
    print("3)Dungeons")
    print("4)Strongholds")
    print("5)Arcane Smith")
    print("E)Exit")
    option = raw_input('--->')
    if (option == "1"):
        PlayerIG.Location = 'Forest'
        prefight()
    elif (option == "2"):
        PlayerIG.Location = "Mountains"
        prefight()
    elif (option == "3"):
        PlayerIG.Location = "Dungeons"
        prefight()
    elif (option == "4"):
        Stronghold()
    if (option == "5"):
        ArcaneSmith()
    elif (option == "e" or option == "E"):
        Start1()
    else:
        Explore()
def prefight():
    global enemy
    enemynum = random.randint(1,10)
    if (PlayerIG.Location == "Forest"):
        if (enemynum == 1 or enemynum == 2 or enemynum == 3):
            enemy = ThugIG
        elif (enemynum == 4 or enemynum == 5):
            enemy = TimberIG
        elif (enemynum == 6 or enemynum == 7 or enemynum == 8):
            enemy = GoblinIG
        elif (enemynum == 9 or enemynum == 10):
            enemy = BrownBearIG
        fight()
    if (PlayerIG.Location == "Mountains"):
        if (enemynum <=5):
            enemy = TrollIG
        if (enemynum >=6):
            enemy = SnowWolfIG
        fight()
    if (PlayerIG.Location == "Dungeons"):
        if (enemynum <=5):
            enemy = SkeletonIG
        if (enemynum >=6):
            enemy = NecromancerIG
        fight()
    if (PlayerIG.Location == "Forest Stronghold"):
        enemy = GoblinBossIG
        fight()
    else:
        Explore()
def die():
    os.system('clear')
    print("You Were Defeated...")
    PlayerIG.Gold -= 10
    if (PlayerIG.Gold < 0):
        PlayerIG.Gold = 0
    PlayerIG.Health = 10
    enemy.Health = enemy.MaxHealth
    option = raw_input('')
    Start1()
    
def LevelUp():
    os.system('clear')
    PlayerIG.MaxXP += 50
    PlayerIG.EXP = 0
    PlayerIG.MaxArcana += 5
    PlayerIG.MaxHealth += 5
    print("You leveled up...")
    PlayerIG.MaxHealth += 5
    option = raw_input('')
def win():
    os.system('clear')
    global enemy
    if (enemy == SkeletonMIG):
        enemy = NecromancerBossIG
        print("You slay the skeletal minion...")
        option = raw_input('')
        fight()
        
    print("You are Victorious!")
    PlayerIG.Gold += enemy.Gold
    print("You got %s Gold"%(enemy.Gold))
    PlayerIG.EXP+=enemy.EXP
    print("You got %s EXP"%(enemy.EXP))
    if (PlayerIG.EXP >= PlayerIG.MaxXP):
        LevelUp()

    if (PlayerIG.Race=="Human"):
        GoldHumanChance = random.randint(1,3)
        if(GoldHumanChance == 1):
            print("You find 30 extra coins...")
            PlayerIG.Gold+=30
    if (enemy == GoblinBossIG):
        if ("Forest Blade" in PlayerIG.weap):
            pass
        else:
            print("You find the Forest Blade...")
            PlayerIG.weap.append('Forest Blade')
    if (enemy == SnowWolfBossIG):
        if ("Winter Blade" in PlayerIG.weap):
            pass
        else:
            print("You find the Winter Blade...")
            PlayerIG.weap.append('Winter Blade')
    if (enemy == NecromancerBossIG):
        if ("Shadow Blade" in PlayerIG.weap):
            pass
        else:
            print("You find the Shadow Blade...")
            PlayerIG.weap.append('Shadow Blade')
    enemy.Health = enemy.MaxHealth
    option = raw_input('')
    Start1()
    
    
def drinkpotH():
    os.system('clear')
    if (PlayerIG.pots >= 1):
        PlayerIG.pots-=1
        PlayerIG.Health = PlayerIG.MaxHealth
        print("You drank a potion! Health Restored")
        option = raw_input("")
        fight()
    else:
        print("You do not have a potion...")
        option = raw_input('')
        fight()
def flee():
    os.system('clear')
    if(PlayerIG.Race == "Elf"):
        runchance = random.randint(1, 100)
        if (runchance <= 65):
            print("Being an Elf fleeing was no issue...")
            enemy.Health = enemy.MaxHealth
            option = raw_input('')
            Start1()
        else:
            print("You failed to flee...")
            eAttack = random.randint(enemy.Attack/2, enemy.Attack)
            if(eAttack == enemy.Attack/2):
                print("%s Missed..."%(enemy.name))
            else:
                PlayerIG.Health -= eAttack
                print("%s deals %i damage"%(enemy.name, eAttack))
            option = raw_input('')
            os.system('clear')
            if (PlayerIG.Health <= 0):
                die()
            option = raw_input('')
            fight()
    elif(PlayerIG.Race != "Elf"):
        runchance = random.randint(1, 3)
        if (runchance == 1):
            print("You fled succesfully...")
            enemy.Health = enemy.MaxHealth
            option = raw_input('')
            Start1()
        else:
            print("You failed to flee...")
            eAttack = random.randint(enemy.Attack/2, enemy.Attack)
            if(eAttack == enemy.Attack/2):
                print("%s Missed..."%(enemy.name))
            else:
                PlayerIG.Health -= eAttack
                print("%s deals %i damage"%(enemy.name, eAttack))
            option = raw_input('')
            os.system('clear')
            if (PlayerIG.Health <= 0):
                die()
            option = raw_input('')
            fight()
def CastSpell():
    os.system('clear')
    print("Select A Spell To Cast")
    print("E)Exit")
    for Spells in PlayerIG.SpellList:
        print ("-" + Spells)
    option = raw_input('-->')
    if (option == "E" or option == "e"):
        fight()
    if (option in PlayerIG.SpellList):
        #FIREBALL SPELL
        if(option == "Fireball"):
            ArcanaCost = random.randint(15,30)
            FireDamage = random.randint(20,30 )
            if (PlayerIG.Arcana >= ArcanaCost):
                print("You cast a ball of fire for %i Arcana dealing %s %i Damage"%(ArcanaCost,enemy.name,FireDamage))
                PlayerIG.Arcana -= ArcanaCost
                enemy.Health -= FireDamage
                eAttack = random.randint(enemy.Attack/2, enemy.Attack)
                PlayerIG.Health-=eAttack
                print('Enemy does %s damage'%(eAttack))
                if (enemy.Health <= 0):
                    if (PlayerIG.Health <= 0):
                        PlayerIG.Health = 10
                    win()

                elif (PlayerIG.Health <= 0):
                    print("You died...")
                    option = raw_input('')
                    enemy.Health = enemy.MaxHealth
                    die()
                else:
                    option = raw_input('')
                    fight()
            else:
                os.system('clear')
                print("You failed to cast the spell...")
                raw_input('')
                CastSpell()
        #HEAL SPELL
        if(option == "Heal"):
            if (PlayerIG.Health >= PlayerIG.MaxHealth):
                print("You are already fully healed...")
                os.system('clear')
                option = raw_input('')
                CastSpell()
            HealAmount = random.randint(15,30)
            ArcanaCost = random.randint(10,20)
            if(PlayerIG.Arcana >= ArcanaCost):
                PlayerIG.Arcana -= ArcanaCost
                print("You watch as your wounds close, and aches fade")
                print("Spell Cost: %s"%(ArcanaCost))
                print("Heal Amount %s"%(HealAmount))
                PlayerIG.Health+=HealAmount
                if (PlayerIG.Health >= PlayerIG.MaxHealth):
                    PlayerIG.Health = PlayerIG.MaxHealth
                option = raw_input('')
                CastSpell()
            else:
                print("You fail to cast the spell...")
                os.system('clear')
                option = raw_input('')
                fight()
    else:
        os.system('clear')
        print("You don't know that spell...")
        raw_input('')
        fight()
def drinkpotA():
    if (PlayerIG.Arcana != PlayerIG.MaxArcana and PlayerIG.ArcanaPots >= 1):
        os.system('clear')
        print("You drank a potion...Arcana Restored")
        PlayerIG.Arcana = PlayerIG.MaxArcana
        option = raw_input('')
        fight()
    else:
        os.system('clear')
        print("You already are at Max Arcana")
        option = raw_input('')
        fight()
def fight():
    os.system('clear')
    print("%s   |    %s" % (PlayerIG.name, enemy.name))
    print("%s's Health: %s/%s    %s's Health: %s/%s"%(PlayerIG.name, PlayerIG.Health, PlayerIG.MaxHealth, enemy.name, enemy.Health, enemy.MaxHealth))
    print("Arcana: %s/%s"%(PlayerIG.Arcana, PlayerIG.MaxArcana))
    print("Potions: %s" % (PlayerIG.pots))
    print("Arcana Potions: %s"%(PlayerIG.ArcanaPots))
    print("_________________________________")
    print("1)Attack")
    print("2)Drink Health Potion")
    print("3)Drink Arcana Potion")
    print("4)Cast Spell")
    print("5)Flee")
    option = raw_input("-->")
    if (option == "1"):
        attack()
    elif (option == "2"):
        drinkpotH()
    elif (option == "3"):
        drinkpotA()
    elif (option == "4"):
        CastSpell()
    elif (option == "5"):
        flee()
    else:
        fight()
def store():
    os.system('clear')
    print("Welcome to the shop!")
    print("Anything in particular you want to buy?")
    print("Gold: %s Health Potion: %s"%(PlayerIG.Gold, PlayerIG.pots))
    print("")
    print("|------------------|")
    print("|      Weapons     |")
    print("|------------------|")
    print("-Iron Sword[50g]")
    print("-Bronze Sword[100g]")
    print("-Steel Sword[300g]")
    print("-Ebon Sword[350g]")
    print("-Iron Greatsword[400g]")
    print("-Bronze Greatsword[500g]")
    print("-Steel Greatsword[550g]")
    print("-Ebon Greatsword[600g]")
    print('')
    print("|------------------|")
    print("|      Armour      |")
    print("|------------------|")
    print("-Cheap Gambeson[50g]")
    print("-Iron Chainmail[75g]]")
    print("-Steel Chainmail[125g]")
    print("-Ebon Chainmail[200g]")
    print("-Iron Plate[300g]")
    print("-Steel Plate[400g]")
    print("-Ebon Plate[500g]")
    print("___________________")
    print('P)Potion[10g]')
    print('E)Exit Store')
    option = raw_input("-->")
    if (option in weapons):
        if (PlayerIG.Gold >= weapons[option]):
            os.system('clear')
            print("You purchased ") + option
            PlayerIG.weap.append(option)
            option = raw_input('')
            store()
        else:
            os.system('clear')
            print("You seem to be lacking %i coins..."% (weapons[option] - PlayerIG.Gold))
            option = raw_input('')
            store()
    if (option in armour):
        if (PlayerIG.Gold >= armour[option]):
            os.system('clear')
            PlayerIG.Gold -= armour[option]
            PlayerIG.armour.append(option)
            print("You have purchased %s "% (option))
            option = raw_input('')
            store()
        else:
            os.system('clear')
            print("You seem to be lacking %i coins..."% (armour[option] - PlayerIG.Gold))
            option = raw_input('')
            store()
    elif (option == "E" or option == "e"):
        os.system('clear')
        print("Goodbye come again soon!")
        option = raw_input('')
        Start1()
    elif (option == "P" or option == "p"):
        os.system('clear')
        if (PlayerIG.Gold >= 50):
            os.system('clear')
            PlayerIG.pots+=1
            PlayerIG.Gold-=50
            print("You bought a potion for 10 gold...")
            store()
        else:
            os.system("clear")
            print("You lack %i gold for a potion..."%(50-PlayerIG.Gold))
            raw_input('')
            store()
    else:
        os.system('clear')
        print("I do not have that item in stock...")
        option = raw_input('')
        store()
    
def Main():
    os.system('clear')
    print("|---------------------------------|")
    print("|  Welcome To The Eradaric Isles  |")
    print("|---------------------------------|")
    print("1) Start")
    print("2) Load")
    print("3) Exit")
    option = raw_input("--> ")
    
    if (option == "1"):
        Start()
    elif (option == "2"):
        if (os.path.exists('savefile') == True):
            os.system('clear')
            with open('savefile', 'rb') as f:
                global PlayerIG
                PlayerIG = pickle.load(f)
            print("Loaded save...")
            option = raw_input('')
            Start1()
        else:
            os.system('clear')
            print("Save not present...")
            option = raw_input('')
            Main()
    elif (option == "3"):
        print("Game Stopped")
        sys.exit()
    else:
        Main()
Main()
