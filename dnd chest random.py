import random
number_players = input('how many players are there')
land_monsters = ['dragon','goblin','space marine','skeleton']
sea_monsters = ['kraken']

#is_sale_on = ["y",'n']
#sale_price = [10,20,30,40,40]

dock_merchant_food = ['bread','steak','pork']
dock_merchant_armour = ['leather pads','breastplate','chainmail']
dock_merchant_weapons = ['shortbow','longbow','crossbow','shortsword','longsword']
dock_merchant_healing_items = ['health potion','antidote',]
dock_merchant_weapon_extras = ['10 arrows','10 crossbow bolts']
dock_merchant_weapons_extra_price = ['10GP','20GP']
dock_merchant_food_price = ['1SP','1GP']
dock_merchant_armour_price = ['5GP','10GP',"15GP",'20GP']
dock_merchant_weapons_price = ['5GP','10GP','15GP','20GP']
dock_merchant_healing_items_price = ['5GP','10GP']

cap_merchant_food = ['bread','steak','pork']
cap_merchant_clothes = ['fine clothes','travller clothes']
cap_merchant_weapons = ['shortsword','longsword']
cap_merchant_healing_items = ['health potion','antidote',]
cap_merchant_food_price = ['1SP','1GP']
cap_merchant_armour_price = ['5GP','10GP',"15GP",'20GP']
cap_merchant_weapons_price = ['5GP','10GP','15','20GP']
cap_merchant_healing_items_price = ['5GP','10GP']

wand_merchant_food = ['bread','steak','pork']
wand_merchant_armour = ['leather pads','breastplate','chainmail']
wand_merchant_weapons = ['shortbow','longbow','crossbow','shortsword','longsword']
wand_merchant_healing_items = ['health potion','antidote',]
wand_merchant_weapon_extras = ['10 arrows','10 crossbow bolt']
wand_merchant_weapons_extra_price = ['10GP','20GP']
wand_merchant_food_price = ['1SP','1GP']
wand_merchant_armour_price = ['5GP','10GP',"15GP",'20GP']
wand_merchant_weapons_price = ['5GP','10GP','15GP','20GP']
wand_merchant_healing_items_price = ['5GP','10GP']

#merchant_food = ['bread','steak','pork']
#merchant_armour = ['leather pads','breastplate','chainmail']
#merchant_weapons = ['shortbow','longbow','crossbow','10 pack of arrow','shortsword','longsword']
#merchant_healing_items = ['health potion','antidote',]
#merchant_food_price = ['1SP','1GP']
#merchant_armour_price = ['5GP','10GP',"15GP",'20GP']
#merchant_weapons_price = ['5GP','10GP','15','20GP']
#merchant_healing_items_price = ['5GP','10GP']
for i in ("99999999999999999999999999999999999999999999999"):
    menu = input('what operation do you want ')
    if menu == ('1 land mob spawn'):
        monster1=random.choice(land_monsters)
        print('A hostile '+monster1+' has appeared')
    elif menu == ('2 land mob spawn'):
        monster1=random.choice(land_monsters)
        monster2=random.choice(land_monsters)
        print("A "+monster1+' and a '+monster2+'has appeared')
    elif menu == ('3 land mob spawn'):
        monster1=random.choice(land_monsters)
        monster2=random.choice(land_monsters)
        monster3=random.choice(land_monsters)
        print("a "+monster1+', '+monster2+' and a '+monster3+' have spawned')










#chest loot randomiser 
    elif menu == ('chest'): 
        start = input("what level chest do you want ")
        lv1chest = ["old sword" , "health potion" , "10SP" , "10 ten arrows" , "short bow","leather amrour","rope", "camel","travler clothes ",'thieves tools']
        lv1chestno = ["1","2","3"]
        lv2chest = ["10gp","longbow","long sword","chainmail armour","battle axe","fine clothes","2 health potions",'ring of invisablity']
        lv2chestno = ["1","2",'3','4']
        lv3chest = ['great club','great sword','great axe','breast plate','bomb','10 PP','can o beans' ]
        lv3chestno =['1','2']
        if start == ("lv1"):
            numofitems = random.choice(lv1chestno)
            if numofitems == ("1"):
                item = random.choice(lv1chest)
                print(item)
            
            elif numofitems == ("2"):
                item = random.choice(lv1chest)
                item2 = random.choice(lv1chest)
                print(item+' and '+item2)
            elif numofitems == ("3"):
                item = random.choice(lv1chest)
                item2 = random.choice(lv1chest)
                item3 = random.choice(lv2chest)
                print(item+", "+item2+" and "+item3)
        elif start == ("lv2"):
            lv2numofitems = random.choice(lv2chestno)
            if lv2numofitems == ("1"):
                item = random.choice(lv2chest)
                print(item)
            
            elif lv2numofitems == ("2"):
                item = random.choice(lv2chest)
                item2 = random.choice(lv2chest)
                print(item+' and '+item2)
            elif lv2numofitems == ("3"):
                item = random.choice(lv2chest)
                item2 = random.choice(lv2chest)
                item3 = random.choice(lv2chest)
                print(item+", "+item2+" and "+item3)
            elif lv2numofitems == ("4"):
                item = random.choice(lv2chest)
                item2 = random.choice(lv2chest)
                item3 = random.choice(lv2chest)
                item4 = random.choice(lv2chest)
                print(item+", "+item2+", "+item3+" and "+item4)
            
        elif start == ("lv3"):
            lv3numofitems = random.choice(lv3chestno)
            if lv3numofitems == ("1"):
                item = random.choice(lv2chest)
                print(item)
            elif lv3numofitems == ("2"):
                item = random.choice(lv3chest)
                item2 = random.choice(lv3chest)
                print(item+' and '+item2)
            
        else:
            print("sorry that doesnt exist")
#dock city merchant

    if menu ==  ("dock merchant"):
        dock_merchant_chat = input('Hello there adventuer what would you like to buy to day ')
        if dock_merchant_chat == ("armour"):
            armour_item_quatity = random.choice(number_players)
            armour_sell = random.choice(dock_merchant_armour)
            armour_price = random.choice(dock_merchant_armour_price)
            if armour_sell == "breastplate":
                armour_price = ("10GP")
            print("i have "+armour_item_quatity+' '+armour_sell+" for "+armour_price+' each')
                
        elif dock_merchant_chat ==("weapons"):
            weapons_items_quatity = random.choice(number_players)
            weapons_sells = random.choice(dock_merchant_weapons)
            weapons_price = random.choice(dock_merchant_weapons_price)
            print("i have "+weapons_items_quatity+" "+weapons_sells+" for "+weapons_price+' each')
        elif dock_merchant_chat ==("heals"):
            healing_items_quatity = random.choice(number_players)
            healing_items_sells = random.choice(dock_merchant_healing_items)
            healing_items_price = random.choice(dock_merchant_healing_items_price)
            print("i have "+healing_items_quatity+" "+healing_items_sells+" for "+healing_items_price+' each')
        elif dock_merchant_chat ==("food"):
            food_items_quatity = random.choice(number_players)
            food_items_quatity+3
            food_sells = random.choice(dock_merchant_food)
            food_price = random.choice(dock_merchant_food_price)
            print("i have "+food_items_quatity+" "+food_sells+" for "+food_price+' each')
        elif dock_merchant_chat ==("ammo"):
            ammo_items_quatity = random.choice(number_players)
            ammo_sells = random.choice(dock_merchant_weapon_extras)
            ammo_price = random.choice(dock_merchant_weapons_extra_price)
            print("i have "+ammo_items_quatity+" "+ammo_sells+" for "+ammo_price+' each')
   #capital city merchant
   
   
    if menu ==  ("cap merchant"):
        cap_merchant_chat = input('Hello there adventuer what would you like to buy to day ')
        if cap_merchant_chat == ("clothes"):
            armour_item_quatity = random.choice(number_players)
            armour_sells = random.choice(cap_merchant_clothes)
            armour_price = random.choice(cap_merchant_armour_price)
            print("i have "+armour_item_quatity+" "+armour_sells+" for "+armour_price+" each")
        elif dock_merchant_chat ==("weapons"):
            weapons_items_quatity = random.choice(number_players)
            weapons_sells = random.choice(cap_merchant_weapons)
            weapons_price = random.choice(cap_merchant_weapons_price)
            print("i have "+weapons_items_quatity+" "+weapons_sells+" for "+weapons_price+' each')
        elif cap_merchant_chat ==("heals"):
            healing_items_quatity = random.choice(number_players)
            healing_items_sells = random.choice(cap_merchant_healing_items)
            healing_items_price = random.choice(cap_merchant_healing_items_price)
            print("i have "+healing_items_quatity+" "+healing_items_sells+" for "+healing_items_price+' each')
        elif cap_merchant_chat ==("food"):
            food_items_quatity = random.choice(number_players)
            food_items_quatity+3
            food_sells = random.choice(cap_merchant_food)
            food_price = random.choice(cap_merchant_food_price)
            print("i have "+food_items_quatity+" "+food_sells+" for "+food_price+' each')
        #elif cap_merchant_chat ==("ammo"):
           # ammo_items_quatity = random.choice(number_players)
            #ammo_sells = random.choice(cap_merchant_weapon_extras)
            #ammo_price = random.choice(cap_merchant_weapons_extra_price)
            #print("i have "+ammo_items_quatity+" "+ammo_sells+" for "+ammo_price+' each')

#wandering merchant

    if menu ==  ("wandering merchant"):
        wand_merchant_chat = input('Hello there adventuer what would you like to buy to day ')
        if wand_merchant_chat == ("clothes"):
            armour_item_quatity = random.choice(number_players)
            armour_sells = random.choice(cap_merchant_clothes)
            armour_price = random.choice(cap_merchant_armour_price)
            print("i have "+armour_item_quatity+" "+armour_sells+" for "+armour_price+" each")
        elif wand_merchant_chat ==("weapons"):
            weapons_items_quatity = random.choice(number_players)
            weapons_sells = random.choice(wand_merchant_weapons)
            weapons_price = random.choice(wand_merchant_weapons_price)
            print("i have "+weapons_items_quatity+" "+weapons_sells+" for "+weapons_price+' each')
        elif wand_merchant_chat ==("heals"):
            healing_items_quatity = random.choice(number_players)
            healing_items_sells = random.choice(wand_merchant_healing_items)
            healing_items_price = random.choice(wand_merchant_healing_items_price)
            print("i have "+healing_items_quatity+" "+healing_items_sells+" for "+healing_items_price+' each')
        elif wand_merchant_chat ==("food"):
            food_items_quatity = random.choice(number_players)
            food_sells = random.choice(wand_merchant_food)
            food_price = random.choice(wand_merchant_food_price)
            print("i have "+food_items_quatity+" "+food_sells+" for "+food_price+' each')
        elif cap_merchant_chat ==("ammo"):
            ammo_items_quatity = random.choice(number_players)
            ammo_sells = random.choice(wand_merchant_weapon_extras)
            ammo_price = random.choice(wand_merchant_weapons_extra_price)
            print("i have "+ammo_items_quatity+" "+ammo_sells+" for "+ammo_price+' each')