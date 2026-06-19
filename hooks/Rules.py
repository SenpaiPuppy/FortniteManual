from typing import Optional
from worlds.AutoWorld import World # type: ignore
from ..Helpers import clamp, get_items_with_value
from BaseClasses import MultiWorld, CollectionState # type: ignore
from ..Data import location_table

import re

def EarlyBird(world: World, multiworld: MultiWorld, player: int, state: CollectionState):
    RarityEnabled = world.options.rarity_toggle.value
    ProRarity = world.options.progressive_rarities.value
    ShoppingItems = world.options.shopping_items.value

    if RarityEnabled == False:
        return True
    
    if RarityEnabled == True:
        if ProRarity == True:
            if "Sprite Dust" in ShoppingItems:
                if "Upgrade Weapon" in ShoppingItems:
                    return "|Upgrade Weapon| and |Sprite Dust| and |Progressive Rarity:4|"
                else:
                    return "|Sprite Dust| and |Progressive Rarity:4|"
            else:
                if "Upgrade Weapon" in ShoppingItems:
                    return "|Upgrade Weapon| and |Progressive Rarity:4|"
                else:
                    return "|Progressive Rarity:4|"
                
        if ProRarity == False:
            if "Sprite Dust" in ShoppingItems:
                if "Upgrade Weapon" in ShoppingItems:
                    return "|Upgrade Weapon| and |Sprite Dust| and |Rarity - Legendary/Mythic|"
                else:
                    return "|Sprite Dust| and |Rarity - Legendary/Mythic|"
            else:
                if "Upgrade Weapon" in ShoppingItems:
                    return "|Upgrade Weapon| and |Rarity - Legendary/Mythic|"
                else:
                    return "|Rarity - Legendary/Mythic|"
    return False

def RapidRampage(world: World, multiworld: MultiWorld, player: int, state: CollectionState):
    Toggle = world.options.weapon_mastery.value
    if Toggle == True:
        return "|Assault Rifle Mastery| and |@Assault Rifle:1|"
    return "|@Assault Rifle:1|"

def ShellShocked(world: World, multiworld: MultiWorld, player: int, state: CollectionState):
    Toggle = world.options.weapon_mastery.value
    if Toggle == True:
        return "|Assault Rifle Mastery| and |@Assault Rifle:1|"
    return "|@Assault Rifle:1|"

def SubtleSavagery(world: World, multiworld: MultiWorld, player: int, state: CollectionState):
    Toggle = world.options.weapon_mastery.value
    if Toggle == True:
        return "|Assault Rifle Mastery| and |@Assault Rifle:1|"
    return "|@Assault Rifle:1|"
    
def SteadySharpshooter(world: World, multiworld: MultiWorld, player: int, state: CollectionState):
    Toggle = world.options.weapon_mastery.value
    if Toggle == True:
        return "|Assault Rifle Mastery| and |@Sniper:1|"
    return "|@Sniper:1|"

def PinpointPrecision(world: World, multiworld: MultiWorld, player: int, state: CollectionState):
    Toggle = world.options.weapon_mastery.value
    if Toggle == True:
        return "|Assault Rifle Mastery| and |@Assault Rifle:1|" 
    return "|@Assault Rifle:1|"
    
def OneMansTrash(world: World, multiworld: MultiWorld, player: int, state: CollectionState):
    Toggle = world.options.weapon_mastery.value
    Gamemode = world.options.progressive_gamemode.value
    if Gamemode == True:
        if Toggle == True:
            return "|Progressive Gamemode:2| and |@Mastery:2|"
        else:
            return "|Progressive Gamemode:2|"
    if Gamemode == False:
        if Toggle == True:
            return "|@Mastery:2|"
    return True

def ImpossibleShot(world: World, multiworld: MultiWorld, player: int, state: CollectionState):
    Toggle = world.options.weapon_mastery.value
    if Toggle == True:
        return "|Assault Rifle Mastery| and |Hunting Rifle|"
    return "|Hunting Rifle|"

def OffTheDome(world: World, multiworld: MultiWorld, player: int, state: CollectionState):
    Toggle = world.options.weapon_mastery.value
    if Toggle == True:
        return "|SMG Mastery| and |Pistol Mastery| and |@Pistol:1| and |@SMG:1|"
    return "|@Pistol:1| and |@SMG:1|"

def AgainstTheWorld(world: World, multiworld: MultiWorld, player: int, state: CollectionState):
    Toggle = world.options.weapon_mastery.value
    if Toggle == True:
        return "|@Mastery:2|"
    return True
    
def FruitsAndVeggies(world: World, multiworld: MultiWorld, player: int, state: CollectionState):
    skills = world.options.lesson_skills.value
    if "Forage Lessons" in skills:
        return "|Forage Lessons|"
    return True

def SelfReviveDevice(world: World, multiworld: MultiWorld, player: int, state: CollectionState):
    Toggle = world.options.consumable_toggle.value
    if Toggle == True:
        return "|Self-Revive Device|"
    return True

def DemolitionDomination(world: World, multiworld: MultiWorld, player: int, state: CollectionState):
    Toggle = world.options.weapon_mastery.value
    if Toggle == True:
        return "|Melee Mastery|"
    return True
    
def BustlingBuilder(world: World, multiworld: MultiWorld, player: int, state: CollectionState):
    Mats = world.options.resourceful_materials.value
    skills = world.options.lesson_skills.value
    if "Building Lessons" in skills:
        if Mats == 1: return "|Building Lessons|"
        if Mats == 2: return "|Building Lessons| and (|Materials - Wood| or |Materials - Metal| or |Materials - Brick|)"
        if Mats >= 3: return "|Building Lessons| and |Progressive Building Materials|"
    if "Building Lessons" not in skills:
        if Mats == 1: return True
        if Mats == 2: return "|Materials - Wood| or |Materials - Metal| or |Materials - Brick|"
        if Mats >= 3: return "|Progressive Building Materials|"
    return True

def Resourcefulness(world: World, multiworld: MultiWorld, player: int, state: CollectionState):
    Mats = world.options.resourceful_materials.value
    skills = world.options.weapon_mastery.value
    if skills == True:
        if Mats == 1: return "|Melee Mastery|"
        if Mats == 2: return "|Melee Mastery| and (|Materials - Wood| or |Materials - Metal| or |Materials - Brick|)"
        if Mats >= 3: return "|Melee Mastery| and |Progressive Building Materials|"
    if skills == False:
        if Mats == 2: return "|Materials - Wood| or |Materials - Metal| or |Materials - Brick|"
        if Mats >= 3: return "|Progressive Building Materials|"
    return True

def CharacterRecruit(world: World, multiworld: MultiWorld, player: int, state: CollectionState):
    Shopping = world.options.shopping_items.value
    if "Gold Spender" in Shopping:
        if "Recruit Character" in Shopping:
            return "|Recruit Character| and |Gold Spender|"
        if "Recruit Character" not in Shopping:
            return "|Gold Spender|"
    if "Recruit Characters" in Shopping:
        if "Gold Spender" not in Shopping:
            return "|Recruit Character|"
    return True

def RoadTrip(world: World, multiworld: MultiWorld, player: int, state: CollectionState):
    Skills = world.options.lesson_skills.value
    if "Driving Lessons" in Skills:
        return "|Driving Lessons|"
    return True

def MasterExtractor(world: World, multiworld: MultiWorld, player: int, state: CollectionState):
    Sprite = world.options.sprite_toggle.value
    Skills = world.options.lesson_skills.value
    if "Searchable Lessons" in Skills:
        if Sprite == True:
            return "|Searchable Lessons| and |@Sprites:2|"
        if Sprite == False:
            return "|Searchable Lessons|"
    if Sprite == True:
        if "Searchable Lessons" not in Skills:
            return "|@Sprites:2|"
    return True

def AverageLooper(world: World, multiworld: MultiWorld, player: int, state: CollectionState):
    Shopping = world.options.shopping_items.value
    if "Gold Spender" in Shopping:
        return "|Gold Spender|"
    return True

def SevenSliders(world: World, multiworld: MultiWorld, player: int, state: CollectionState):
    Utility = world.options.utlity_toggle.value
    Super = world.options.super_weapon_varients.value
    if Super == True:
        if Utility == True:
            return "|Limitless Seven Sliders| or |Seven Sliders|"
    if Super == False:
        if Utility == True:
            return "|Seven Sliders|"
    return True

def Deconsecrated(world: World, multiworld: MultiWorld, player: int, state: CollectionState):
    SuperWep = world.options.super_weapon_varients.value
    RarityEnabled = world.options.rarity_toggle.value
    ProRarity = world.options.progressive_rarities.value
    Toggle = world.options.weapon_mastery.value

    if SuperWep == False:
        if RarityEnabled == True:
            if ProRarity == False:
                if Toggle == True:
                    return "|Pistol Mastery| and |Lancehead Pistol| and (|Rarity - Rare| or |Rarity - Epic| or |Rarity - Legendary/Mythic|)"
                if Toggle == False:
                    return "|Lancehead Pistol| and (|Rarity - Rare| or |Rarity - Epic| or |Rarity - Legendary/Mythic|)"
        if RarityEnabled == True:
            if ProRarity == True:
                if Toggle == True:
                    return "|Pistol Mastery| and |Lancehead Pistol| and |Progressive Rarity:2|"
                if Toggle == False:
                    return "|Lancehead Pistol| and |Progressive Rarity:2|"
        if RarityEnabled == False:
            if Toggle == True:
                return "|Pistol Mastery| and |Lancehead Pistol|"
            if Toggle == False:
                return "|Lancehead Pistol|"

    if SuperWep == True:
        if RarityEnabled == True:
            if ProRarity == False:
                if Toggle == True:
                    return "(|Pistol Mastery| and |Lancehead Pistol| and (|Rarity - Rare| or |Rarity - Epic| or |Rarity - Legendary/Mythic|) or (|9mm Baba Yaga Pistol| and |Pistol Mastery| and |Rarity - Legendary/Mythic|)"
                if Toggle == False:
                    return "(|Lancehead Pistol| and (|Rarity - Rare| or |Rarity - Epic| or |Rarity - Legendary/Mythic|) or (|9mm Baba Yaga Pistol| and |Rarity - Legendary/Mythic|)"
        if RarityEnabled == True:
            if ProRarity == True:
                if Toggle == True:
                    return "(|Pistol Mastery| and |Lancehead Pistol| and (|Progressive Rarity:2|) or (|9mm Baba Yaga Pistol| and |Pistol Mastery| and |Progressive Rarity:4|)"
                if Toggle == False:
                    return "(|Lancehead Pistol| and |Progressive Rarity:2|) or (|9mm Baba Yaga Pistol| and |Progressive Rarity:4|)"
        if RarityEnabled == False:
            if Toggle == True:
                return "(|Pistol Mastery| and |Lancehead Pistol|) or (|9mm Baba Yaga Pistol| and |Pistol Mastery|)"
            if Toggle == False:
                return "|Lancehead Pistol| or |9mm Baba Yaga Pistol|"

def ImFineReally(world: World, multiworld: MultiWorld, player: int, state: CollectionState):
    Consumables = world.options.consumable_toggle.value
    if Consumables == True:
        return "|Small Shield Potion| or |Shield Potion|"
    return True
def WhoNeedsEm(world: World, multiworld: MultiWorld, player: int, state: CollectionState):
    Consumables = world.options.consumable_toggle.value
    if Consumables == True:
        return "|Medkit| or |Bandages| or |Chug Jug| or |Guzzle Juice|"
    return True
def MaximumOvershields(world: World, multiworld: MultiWorld, player: int, state: CollectionState):
    Consumables = world.options.consumable_toggle.value
    if Consumables == True:
        return "|Small Shield Potion| or |Shield Potion| or |Chug Jug|"
    return True



def DuckVaultKey(world: World, multiworld: MultiWorld, player: int, state: CollectionState):
    KeyCards = world.options.vault_key_cards.value
    if KeyCards == True:
        return "|Duck Vault Key|"
    return True

def NormalVaultKey(world: World, multiworld: MultiWorld, player: int, state: CollectionState):
    KeyCards = world.options.vault_key_cards.value
    if KeyCards == True:
        return "|Vault Key|"
    return True

def EpicVaultKey(world: World, multiworld: MultiWorld, player: int, state: CollectionState):
    KeyCards = world.options.vault_key_cards.value
    if KeyCards == True:
        return "|Epic Vault Key|"
    return True

def Fishing(world: World, multiworld: MultiWorld, player: int, state: CollectionState):
    lessons = world.options.lesson_skills.value
    if "Fishing Lessons" in lessons:
        return "|Fishing Lessons|"
    return True

def Searchables(world: World, multiworld: MultiWorld, player: int, state: CollectionState):
    lessons = world.options.lesson_skills.value
    if "Searchable Lessons" in lessons:
        return "|Searchable Lessons|"
    return True

def UnstableElement(world: World, multiworld: MultiWorld, player: int, state: CollectionState):
    KeyCards = world.options.vault_key_cards.value
    if KeyCards == True:
        return "|Unstable Element|"
    return True

def DanceLessons(world: World, multiworld: MultiWorld, player: int, state: CollectionState):
    Lessons = world.options.lesson_skills.value
    if "Dance Lessons" in Lessons:
        return "|Dance Lessons|"
    return True

def UncommonRarity(world: World, multiworld: MultiWorld, player: int, state: CollectionState):
    RarityEnabled = world.options.rarity_toggle.value
    ProRarity = world.options.progressive_rarities.value
    if RarityEnabled == True:
        if ProRarity == True:
            return "|Progressive Rarity:1|"
        else: 
            return "|Rarity - Uncommon| or |Rarity - Rare| or |Rarity - Epic| or |Rarity - Legendary/Mythic|"
    return True
    
def RarityRare(world: World, multiworld: MultiWorld, player: int, state: CollectionState):
    RarityEnabled = world.options.rarity_toggle.value
    ProRarity = world.options.progressive_rarities.value
    if RarityEnabled == True:
        if ProRarity == True:
            return "|Progressive Rarity:2|"
        else: 
            return "|Rarity - Rare| or |Rarity - Epic| or |Rarity - Legendary/Mythic|"
    return True
    
def RarityEpic(world: World, multiworld: MultiWorld, player: int, state: CollectionState):
    RarityEnabled = world.options.rarity_toggle.value
    ProRarity = world.options.progressive_rarities.value
    if RarityEnabled == True:
        if ProRarity == True:
            return "|Progressive Rarity:3|"
        else: 
            return "|Rarity - Epic| or |Rarity - Legendary/Mythic|"
    return True

def LegendaryRarity(world: World, multiworld: MultiWorld, player: int, state: CollectionState):
    RarityEnabled = world.options.rarity_toggle.value
    ProRarity = world.options.progressive_rarities.value
    if RarityEnabled == True:
        if ProRarity == True:
            return "|Progressive Rarity:4|"
        else: 
            return "|Rarity - Legendary/Mythic|"
    return True

def WeaponUpgrade(world: World, multiworld: MultiWorld, player: int, state: CollectionState):
    ShoppingItems = world.options.shopping_items.value
    if "Sprite Dust" in ShoppingItems:
        if "Upgrade Weapon" in ShoppingItems:
            return "|Sprite Dust| and |Upgrade Weapon|"
        else:
            return "|Sprite Dust|"
    else: 
        if "Upgrade Weapon" in ShoppingItems:
            return "|Upgrade Weapon|"
        else: 
            return True
        
def DuosGamemode(world: World, multiworld: MultiWorld, player: int, state: CollectionState):
    Toggle = world.options.progressive_gamemode.value
    if Toggle == True:
        return "|Progressive Gamemode:1|"
    return True
def TriosGamemode(world: World, multiworld: MultiWorld, player: int, state: CollectionState):
    Toggle = world.options.progressive_gamemode.value
    if Toggle == True:
        return "|Progressive Gamemode:2|"
    return True
def SquadsGamemode(world: World, multiworld: MultiWorld, player: int, state: CollectionState):
    Toggle = world.options.progressive_gamemode.value
    if Toggle == True:
        return "|Progressive Gamemode:3|"
    return True








def accolade_goal(world: World, multiworld: MultiWorld, player: int, state: CollectionState):

    Locations = world.get_locations()
    goal_precentage = world.options.accolade_precentage.value
    AccoladeLocations = []

    for location_check in list(Locations):
        item_table_element = next(i_t for i_t in location_table if i_t['name'] == location_check.name)
        location_categories = item_table_element.get("category", []) # gets the Category of Items!
        if "First in Match" in location_categories: AccoladeLocations.append(f"{location_check.name}")
        if "Weapons" in location_categories: AccoladeLocations.append(f"{location_check.name}")
        if "Combat" in location_categories: AccoladeLocations.append(f"{location_check.name}")
        if "Victory Royale" in location_categories: AccoladeLocations.append(f"{location_check.name}")
        if "Survival" in location_categories: AccoladeLocations.append(f"{location_check.name}")
        if "Resources" in location_categories: AccoladeLocations.append(f"{location_check.name}")
        if "Social" in location_categories: AccoladeLocations.append(f"{location_check.name}")
        if "Special" in location_categories: AccoladeLocations.append(f"{location_check.name}")
        if "Seasonal" in location_categories: AccoladeLocations.append(f"{location_check.name}")
    
    AccessibleLocations = len([location for location in Locations if
                    location.address is not None and
                    location.name in AccoladeLocations and
                    location.can_reach(state)])
                    
    location_count = len(AccoladeLocations)
    accolade_needed = round(location_count * (goal_precentage/100))
    #print(f"{AccessibleLocations} >= {accolade_needed} | Location Count: {location_count} | Goal Precentage: {goal_precentage}")
    #print(f"Accolades Needed: {AccessibleLocations} >= {accolade_needed}")
    #print(len(AccoladeLocations))
    #print(AccoladeLocations)
    if AccessibleLocations >= accolade_needed:
        return True
    return False



def victoryCrown(world:World, player: int, state: CollectionState):
    VictoryCrowns = world.options.victory_crowns.value #x%
    return f"|Victory Crown:{VictoryCrowns}%|"



def eliminationGoal(world:World, player: int, state: CollectionState):
    EliminationTokens = world.options.elimination_goal.value #20 = 4 Tokens
    results = int(EliminationTokens / 5)
    return f"|Elimination Tokens:{results}|"

def spriteGoal(world:World, player: int, state: CollectionState):
    SpritesToggle = world.options.sprite_toggle.value
    SpriteCount = world.options.sprites_needed_goal.value
    if SpritesToggle == False:
        return True
    if SpritesToggle == True:
        if SpriteCount > 10 and SpriteCount <= 20:
            return "|@Sprites:2|"
        if SpriteCount > 20 and SpriteCount <= 30:
            return "|@Sprites:3|"
        if SpriteCount > 30 and SpriteCount <= 40:
            return "|@Sprites:4|"
        if SpriteCount > 40 and SpriteCount <= 50:
            return "|@Sprites:5|"
        if SpriteCount > 50 and SpriteCount <= 60:
            return "|@Sprites:6|"
        if SpriteCount > 60 and SpriteCount <= 70:
            return "|@Sprites:7|"
        if SpriteCount > 70 and SpriteCount <= 80:
            return "|@Sprites:8|"
        if SpriteCount > 80 and SpriteCount <= 90:
            return "|@Sprites:9|"
        if SpriteCount > 90 and SpriteCount <= 100:
            return "|@Sprites:10|"
        if SpriteCount <= 10:
            return True
