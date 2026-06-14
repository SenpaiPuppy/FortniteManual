


from typing import Any 
from worlds.AutoWorld import World # type: ignore
from BaseClasses import MultiWorld, CollectionState, Item # type: ignore
from ..Items import ManualItem
from ..Locations import ManualLocation
from ..Data import game_table, item_table, location_table, region_table
from ..Helpers import is_option_enabled, get_option_value, format_state_prog_items_key, ProgItemsCat, remove_specific_item
import logging
import random
def hook_get_filler_item_name(world: World, multiworld: MultiWorld, player: int) -> str | bool:
    return False
def before_generate_early(world: World, multiworld: MultiWorld, player: int) -> None:
    pass
def before_create_regions(world: World, multiworld: MultiWorld, player: int):
    pass




def after_create_regions(world: World, multiworld: MultiWorld, player: int):
    
    #Locations --------------------------------------------
    RemoveAccolades = world.options.remove_accolades.value
    RemoveBossHunts = world.options.boss_hunt.value
#   RemoveAnomalies = world.options.rift_anomalies.value
    RemoveArchipelago = world.options.archipelago_locations.value
    RemoveEliminations = world.options.elimination_locations.value
    #Goals ------------------------------------------------
    Goal = world.options.goal.value
    EliminationTokens = world.options.elimination_goal.value
    #Data -------------------------------------------------
    locationNamesToRemove: list[str] = [] # List of location names
    possible_count = [5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100,
    105,110,115,120,125,130,135,140,145,150,155,160,165,170,175,180,185,190,195,200]

# Remove undesired Catagories -----------------------------
    
    locationNamesToRemove += RemoveAccolades
    if RemoveBossHunts == False: locationNamesToRemove += world.location_name_groups["Boss"]
    if RemoveArchipelago == False: locationNamesToRemove += world.location_name_groups["Archipelago"]

# Remove extra EliminationGoals or All Eliminations depending on goal

    if Goal != 1:
        for term in possible_count:
            Eliminations = [f"Victory Eliminations - {term}"]
            locationNamesToRemove.extend(Eliminations)
    else:
        for term in possible_count:
            if term >= EliminationTokens:
                Eliminations = [f"Victory Eliminations - {term + 5}",f"Eliminations - ({term})"]
                #print(Eliminations)
                locationNamesToRemove.extend(Eliminations)
            else:
                Eliminations = [f"Eliminations - ({term})"]
                locationNamesToRemove.extend(Eliminations)
                #print(Eliminations)

# Remove Elimination Options --------------------------------

    if RemoveEliminations < 200:
        for term in possible_count:
            #print(term)
            if term >= RemoveEliminations:
                Eliminations = [f"Eliminations - ({term + 5})"]
                locationNamesToRemove.extend(Eliminations)
                #print(f"Removing: {Eliminations}")

# Remove Locations ------------------------------------------

    for region in multiworld.regions:
        if region.player == player:
            for location in list(region.locations):
                if location.name in locationNamesToRemove:
                    region.locations.remove(location)
                    
# ----------------------------------------( xxxxx )---------------------------------------- #



def before_create_items_all(item_config: dict[str, int|dict], world: World, multiworld: MultiWorld, player: int) -> dict[str, int|dict]:
    return item_config
def before_create_items_starting(item_pool: list, world: World, multiworld: MultiWorld, player: int) -> list:
    return item_pool
def before_create_items_filler(item_pool: list, world: World, multiworld: MultiWorld, player: int) -> list:

    itemNamesToRemove: list[str] = [] # List of item names
    pre_collect: list[str] = []
    CrownList: list[str] = []
    possible_count = [5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100]
    
#-- Goal_Values -----------------------------------------                    
    Goal = world.options.goal.value
    EliminationTokens = world.options.elimination_goal.value
#-- Rarity --------------------------------------------                      
    RarityEnabled = world.options.rarity_toggle.value
    ProgressiveEnabled = world.options.progressive_rarities.value
    RarityCount = world.options.rarity_counts.value
#-- Items --------------------------------------------                       
    Materials = world.options.resourceful_materials.value
    PocketItem = world.options.starting_pocket_item.value
    KeyCard = world.options.vault_key_cards.value
    Consumable = world.options.consumable_toggle.value
    Utility = world.options.utlity_toggle.value
#   Fishing = world.options.progressive_fishing.value - Unused
    SuperWeapons = world.options.super_weapon_varients.value
#-- Skills -------------------------------------------                       
    LessonSkills = world.options.lesson_skills.value
    ShoppingItems = world.options.shopping_items.value
    WeaponMastery = world.options.weapon_mastery.value
    Gamemode = world.options.progressive_gamemode.value
    MoveRando = world.options.move_randomization.value
    
# ----------------------------------------( Data )---------------------------------------- #

        # goal items 
    VictoryCrown =      ["Victory Crown"]
    ElimTokens =     ["Elimination Tokens"]
        # Progressive - Typically Archipelago Specific
    ProgressiveRarity =  ["Progressive Rarity"]
    ProgressiveBuilding = ["Progressive Building Materials"]
    ProgressiveCatch = ["Progressive Fishing Rod", "Progressive Harpoon Gun"]
    GamemodeItems = ["Progressive Gamemode"] #Quids?
        # Unchanged Items
    Rarities = ["Rarity - Uncommon","Rarity - Rare","Rarity - Epic","Rarity - Legendary/Mythic"]
    MaterialItems = ["Materials - Wood", "Materials - Brick", "Materials - Metal"]
        # Common Changes
    PocketItems =       ["Pocket Item: Shockwave","Pocket Item: Med-mist Smoke","Pocket Item: Shield Bubble"]
    KeyCardItems =      [] # Can Change between seasons or updates
    UtilityItems =      [] # Common
    ConsumableItems =   [] # Common
    FishingItems =      [] # Rare to Change, ie. Harpoon Gun
    SuperWeaponItems =  [] # Typically Season Based
        # Player Options
    RemoveSkills =      []
    ShoppingSkills =    []
    WeaponSkills =      []
    MovementItems =     []
        # weapons viable for starting (common to change, yaml option?) Options -> Yaml -> List
    WeaponAR =  ["Chaos Exploder Rifle","Surgical Pulse Rifle", "Warforged Assault Rifle"]
    WeaponSG =  ["Extending Focus Shotgun","Striker Pump Shotgun","Maven Auto Shotgun"]
    WeaponSMG = ["Flex SMG","Stinger SMG"]
    WeaponPS =  ["Ranger Pistol", "Lancehead Pistol"]

    SpriteItems = [] # Seasonal???
    Sprites = world.options.sprite_toggle.value

    for item_check in list(item_pool): 
        item_table_element = next(i_t for i_t in item_table if i_t['name'] == item_check.name)
        item_categories = item_table_element.get("category", []) # gets the Category of Items!
            # Common Changes
        if "KeyCard" in item_categories: KeyCardItems.append(f"{item_check.name}")
        if "Utility" in item_categories: UtilityItems.append(f"{item_check.name}")
        if "Consumable" in item_categories: ConsumableItems.append(f"{item_check.name}")
        if "Fishing" in item_categories: FishingItems.append(f"{item_check.name}")
        if "SuperWeapon" in item_categories: SuperWeaponItems.append(f"{item_check.name}")
            # Player Options
        if "Skills" in item_categories: RemoveSkills.append(f"{item_check.name}")
        if "Shopping" in item_categories: ShoppingSkills.append(f"{item_check.name}")
        if "Mastery" in item_categories: WeaponSkills.append(f"{item_check.name}")
        if "Movement" in item_categories: MovementItems.append(f"{item_check.name}")
        if "Sprites" in item_categories: SpriteItems.append(f"{item_check.name}")
    #print(f"Rarity Items: {RarityItems}\nMaterial Items: {MaterialItems}\nKeyCard Items: {KeyCardItems}\nUtility Items: {UtilityItems}\nConsumable Items: {ConsumableItems}\nFishing: {FishingItems}\nProgressive Fishing: {ProgressiveFishingItems}\nSuper Weapons: {SuperWeaponItems}\nSkills: {RemoveSkills}\nMasteries: {WeaponSkills}\nGamemode: {GamemodeItems}\nMovement: {MovementItems}")
    
# ------------------------------------( Starting Items )----------------------------------- #

    if WeaponMastery == True:
        StartingSkill = random.choice(WeaponSkills)
        if StartingSkill == "Assault Rifle Mastery":
            StartingWeapon = random.choice(WeaponAR)
            pre_collect.append(StartingSkill)
            pre_collect.append(StartingWeapon)
        if StartingSkill == "Shotgun Mastery":
            StartingWeapon = random.choice(WeaponSG)
            pre_collect.append(StartingSkill)
            pre_collect.append(StartingWeapon)
        if StartingSkill == "SMG Mastery":
            StartingWeapon = random.choice(WeaponSMG)
            pre_collect.append(StartingSkill)
            pre_collect.append(StartingWeapon)
        if StartingSkill == "Pistol Mastery":
            StartingWeapon = random.choice(WeaponPS)
            pre_collect.append(StartingSkill)
            pre_collect.append(StartingWeapon)
        if StartingSkill == "Melee Mastery":
            StartingWeapon =  random.choice(WeaponAR)
            pre_collect.append("Assault Rifle Mastery")
            pre_collect.append(StartingWeapon)

# ----------------------------------------( Rarity )--------------------------------------- #

    if RarityEnabled == False:
        itemNamesToRemove.extend(Rarities)
        itemNamesToRemove.extend(ProgressiveRarity*10)
    if RarityEnabled == True:
        if ProgressiveEnabled == False: itemNamesToRemove.extend(ProgressiveRarity*10)
        if ProgressiveEnabled == True:
            itemNamesToRemove.extend(Rarities)
            if RarityCount == 4: itemNamesToRemove.extend(ProgressiveRarity*6)
            if RarityCount == 5: itemNamesToRemove.extend(ProgressiveRarity*5)
            if RarityCount == 6: itemNamesToRemove.extend(ProgressiveRarity*4)
            if RarityCount == 7: itemNamesToRemove.extend(ProgressiveRarity*3)
            if RarityCount == 8: itemNamesToRemove.extend(ProgressiveRarity*2)
            if RarityCount == 9: itemNamesToRemove.extend(ProgressiveRarity)

# ----------------------------------------( Items )---------------------------------------- #

    if Materials == 1:
        for term in MaterialItems: pre_collect.append(term)
        itemNamesToRemove.extend(ProgressiveBuilding*5)
    if Materials == 2:
        itemNamesToRemove.extend(ProgressiveBuilding*5)
    if Materials == 3:
        for term in MaterialItems: itemNamesToRemove.append(term)
        itemNamesToRemove.extend(ProgressiveBuilding*2)
    if Materials == 4: 
        for term in MaterialItems: itemNamesToRemove.append(term)
        itemNamesToRemove.extend(ProgressiveBuilding)
    if Materials == 5:
        for term in MaterialItems: itemNamesToRemove.append(term)

    if PocketItem == 0:
        for term in PocketItems: itemNamesToRemove.append(term)
    if PocketItem == 1: 
        a =  random.choice(PocketItems)
        pre_collect.append(a)
    if PocketItem == 2: pre_collect.append("Pocket Item: Shockwave")
    if PocketItem == 3: pre_collect.append("Pocket Item: Med-mist Smoke")
    if PocketItem == 4: pre_collect.append("Pocket Item: Shield Bubble")

    if KeyCard == False:
        for term in KeyCardItems: itemNamesToRemove.append(term)

    if Utility == False:
        for term in UtilityItems: itemNamesToRemove.append(term)

    if Consumable == False:
        for term in ConsumableItems: itemNamesToRemove.append(term)
    
    #if Fishing == 1:
    #    itemNamesToRemove.extend(ProgressiveCatch*2)
    #if Fishing == 2:
    #    for term in FishingItems: itemNamesToRemove.append(term)
    #if Fishing == 3:
    #    itemNamesToRemove.extend(ProgressiveCatch*2)
    #    for term in FishingItems: pre_collect.append(term)

    if SuperWeapons == False:
        for term in SuperWeaponItems: itemNamesToRemove.append(term)

    if Sprites == False:
        for term in SpriteItems: itemNamesToRemove.append(term)
    if Sprites == True:
        RandomSprite = random.choice(SpriteItems)
        pre_collect.append(RandomSprite)

# ----------------------------------------( Skills )--------------------------------------- #
    SetList2 = ["Dance Lessons","Driving Lessons","Searchable Lessons","Forage Lessons","Building Lessons","Fishing Lessons"]
    SetList1 = ["Gold Spender","Sprite Dust","Ammo Restock", "Recruit Character", "Patch Up", "Activate Rift","Upgrade Weapon"]
    
    for term in list(LessonSkills):
        if term in SetList2:
            SetList2.remove(term)

    for term in list(ShoppingItems): # if term "in" shoppinglist?
        if term in SetList1:
            SetList1.remove(term)
            
    itemNamesToRemove.extend(SetList2)
    itemNamesToRemove.extend(SetList1)

    if WeaponMastery == False: itemNamesToRemove.extend(WeaponSkills)
    if Gamemode == False: itemNamesToRemove.extend(GamemodeItems*4)
    if MoveRando == False: itemNamesToRemove.extend(MovementItems)


# ----------------------------------( Item Remove/Collect )-------------------------------- #
    #print(f"Removing Items: {itemNamesToRemove}")
    for itemName in itemNamesToRemove:
        item = next(i for i in item_pool if i.name == itemName)
        remove_specific_item(item_pool, item)
    
    #print(f"Precollect: {pre_collect}")
    #multiworld.random.shuffle(item_pool) 
    for count in pre_collect:
        item = next(i for i in item_pool if i.name in pre_collect)
        multiworld.push_precollected(item)
        item_pool.remove(item)




# ----------------------------------------( Goals )---------------------------------------- #

    Locations = world.get_locations()
    location_count = len([location for location in Locations])-1 

    if Goal == 0: #Victory Crowns
        CrownList.extend(ElimTokens*20)
        lc = (location_count - (len(item_pool)-70))*-1
        real_crowns = lc + 50
        if real_crowns > 50: real_crowns = 50 
        CrownList.extend(VictoryCrown*real_crowns)
        
    if Goal == 1: #Eliminations
        CrownList.extend(VictoryCrown*50)
        for counts in possible_count: 
            if counts > EliminationTokens:
                CrownList.extend(ElimTokens)
    if Goal == 2: #Accolades
        CrownList.extend(VictoryCrown*50)
        CrownList.extend(ElimTokens*20)

    for itemName in CrownList:
            item = next(i for i in item_pool if i.name == itemName)
            remove_specific_item(item_pool, item)

    return item_pool

# ----------------------------------------( xxxxx )---------------------------------------- #




# The complete item pool prior to being set for generation is provided here, in case you want to make changes to it
def after_create_items(item_pool: list, world: World, multiworld: MultiWorld, player: int) -> list:
    return item_pool
# Called before rules for accessing regions and locations are created. Not clear why you'd want this, but it's here.
def before_set_rules(world: World, multiworld: MultiWorld, player: int):
    pass
# Called after rules for accessing regions and locations are created, in case you want to see or modify that information.
def after_set_rules(world: World, multiworld: MultiWorld, player: int):
    pass
# The item name to create is provided before the item is created, in case you want to make changes to it
def before_create_item(item_name: str, world: World, multiworld: MultiWorld, player: int) -> str:
    return item_name
# The item that was created is provided after creation, in case you want to modify the item
def after_create_item(item: ManualItem, world: World, multiworld: MultiWorld, player: int) -> ManualItem:
    return item
# This method is run towards the end of pre-generation, before the place_item options have been handled and before AP generation occurs
def before_generate_basic(world: World, multiworld: MultiWorld, player: int):
    pass
# This method is run at the very end of pre-generation, once the place_item options have been handled and before AP generation occurs
def after_generate_basic(world: World, multiworld: MultiWorld, player: int):
    pass
# This method is run every time an item is added to the state, can be used to modify the value of an item.
# IMPORTANT! Any changes made in this hook must be cancelled/undone in after_remove_item
def after_collect_item(world: World, state: CollectionState, Changed: bool, item: Item):
    pass
# This method is run every time an item is removed from the state, can be used to modify the value of an item.
# IMPORTANT! Any changes made in this hook must be first done in after_collect_item
def after_remove_item(world: World, state: CollectionState, Changed: bool, item: Item):
    pass
# This is called before slot data is set and provides an empty dict ({}), in case you want to modify it before Manual does
def before_fill_slot_data(slot_data: dict, world: World, multiworld: MultiWorld, player: int) -> dict:
    return slot_data
# This is called after slot data is set and provides the slot data at the time, in case you want to check and modify it after Manual is done with it
def after_fill_slot_data(slot_data: dict, world: World, multiworld: MultiWorld, player: int) -> dict:
    return slot_data
# This is called right at the end, in case you want to write stuff to the spoiler log
def before_write_spoiler(world: World, multiworld: MultiWorld, spoiler_handle) -> None:
    pass
# This is called when you want to add information to the hint text
def before_extend_hint_information(hint_data: dict[int, dict[int, str]], world: World, multiworld: MultiWorld, player: int) -> None:
    pass
def after_extend_hint_information(hint_data: dict[int, dict[int, str]], world: World, multiworld: MultiWorld, player: int) -> None:
    pass
def hook_interpret_slot_data(world: World, player: int, slot_data: dict[str, Any]) -> dict[str, Any]:
    """
        Called when Universal Tracker wants to perform a fake generation
        Use this if you want to use or modify the slot_data for passed into re_gen_passthrough
    """
    return slot_data
