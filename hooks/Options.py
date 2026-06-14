# Object classes from AP that represent different types of options that you can create
from Options import Option, FreeText, NumericOption, Toggle, DefaultOnToggle, Choice, TextChoice, OptionList, Range, NamedRange, OptionGroup, PerGameCommonOptions # pyright: ignore[reportAttributeAccessIssue]
# These helper methods allow you to determine if an option has been set, or what its value is, for any player in the multiworld
from ..Helpers import is_option_enabled, get_option_value
from typing import Type, Any

#   -------------------- ( Goal )--------------------
class VictoryCrowns(Range): # type: ignore 
    """The Percent% of Victory Crowns total needed to Goal.
    Crown Count may be low (5-15 total) due to select yaml options and an expansive loot pool."""
    #display_name = "Victory Crown %"
    range_start = 10
    range_end = 100
    default = 50
class EliminationTokens(Range): # type: ignore 
    """How many Eliminations needed to Goal.
    Eliminations are recorded as Locations
    5 Eliminations = 1 Check, X Eliminations = Goal"""
    #display_name = "Elim. Tokens"
    range_start = 20
    range_end = 100
    default = 50
class AccoladeGoal(Range): # pyright: ignore[reportGeneralTypeIssues]
    """In order to goal with the Accolade Goal, you'll need to have completed a 
    certain number of Accolades and gained a Victory Royale after!
    Reminder, the Accolade Goal only checks for Fortnite Accolades, 
    Archipelago locations do not count for goal.
    You can decide the Percent% of Accolades using the options below"""
    #display_name = "Accolade %"
    range_start = 10
    range_end = 80
    default = 40
#   -------------------- ( Lcoations )--------------------
class RemoveAccolades(OptionList):
    """Determines what Accolades are removed to the Location Pool
    This is to help pad out Hard Accolades (Three to One, Elimination Escapade)
    or ones that aren't possible (Super Swooper) but Exist in the Fortnite Collection Book.
    If you want a location to exist still but have a filler item be sure to use the Exclude Location section instead!
    """
    display_name = "Remove-Accolades"
    default = ["I'm Fine, Really",
               "Who Needs 'Em?",
               "Pacifist", "True Pacifist",
               "Elimination Collector", 
               "Elimination Hoarder", 
               "Elimination Escapade", 
               "Mega Elimination", 
               "Epic Elimination", 
               "Against the World", 
               "Three to One Odds", 
               "Two to One Odds",
               "Maximum Overshields"]
class ArchipelagoLocations(Toggle): # type: ignore
    """Add's addition locations involving Searching certain Containers or finding Character Quests."""
    default = True
class BossHunt(Toggle): # type: ignore
    """Adds the Defeat of several Bosses to the Location list
    Bosses include: Wofle, The Voidblade, Skeletor, Saving John Wick's Dog.
    """
    #display_name = "Boss Hunt"
    default = True
class EliminationLocations(Range): # type: ignore
    """Add's up to # of Locations which are achieved via Eliminations
    Does not work with Elimination Goal
    5 Eliminations = 1 Check"""
    #display_name = "Elimination Locations"
    range_start = 0
    range_end = 200
    default = 50
#   -------------------- ( Rarity )--------------------
class RarityEnabled(Toggle): # type: ignore
    """Would you like to Enable the need for specific Rarities all together?
    Common, Uncommon, Rare, Epic and Legendary/Mythic
    False = (Disable Rarities)
    True = (Keep Enabled)"""
    #display_name = "Rarities Toggle"
    default = True
class ProgressiveRarities(Toggle): # type: ignore
    """Would you like to gain Rarities on a Progressive Scaling?
    Common-> Uncommon-> Rare-> Epic-> Legendary/Mythic
    rarity_toggle must be True"""
    #display_name = "ProgRarities Toggle"
    default = False
class ProgressiveRarityCount(Range): # type: ignore 
    """The Amount of 'Progressive Rarity' items that are added to the pool
    (progressive_rarities needs to be Enabled)"""
    #display_name = "Prog. Rarities"
    range_start = 4
    range_end = 10
    default = 5
#   -------------------- ( Items )--------------------
class Resourcefulness(Range): # type: ignore 
    """Should Materials be Progressive, Split in the Item Pool or Pre Collected?
    1 - Wood, Brick and Metal are Pre Collected, No Progressive Materials
    2 - Wood, Brick and Metal Materials are Split in the Item Pool
    3/4/5 - Progressive Building Materials (X Count) | Wood -> Brick -> Metal"""
    #display_name = "Building Materials"
    default = 2
    range_start = 1
    range_end = 5
class StartingPocketItem(Range): #  type: ignore
    """     0 - Disableld, 1 - Random Pocket Item
    2 - Shockwave, 3 - Med-mist, 4 - Shield Bubble"""
    range_end = 4
class VaultKeyCards(Toggle): # type: ignore 
    """Should Vault/Key Cards be an item added to the pool?
    Vault Key, Epic Vault Key, Duck Vault Key and the Unstable Element"""
    #display_name = "Vault Key Cards"
    default = True
class ConsumableToggle(Toggle): # type: ignore
    """Should Consumable items be added to the pool?
    (Generation may fail with Items >= Available Locations)
    Unstable Element, Self-Revive Device, Medkit, Bandages, 
    Small Shield Potion, Shield Potion, Chug Jug, Bush, Business Turret.
    """
    #display_name = "Consumable Toggle"
    default = True
class UtilityToggle(Toggle): # type: ignore 
    """Should Utility items be added to the pool?
    (Generation may fail with Items >= Available Locations)
    Brick-A-Bunker, Overdrive Grenade, Shrub Bomb, Guardian Shield,
    Smoke Cloud, Seven Sliders, Pulse Scanner, Rift-To-Go, Limitless Seven Sliders"""
    #display_name = "Utility Toggle"
    default = True
class SpriteToggle(Toggle): # type: ignore 
    """Should Sprite items be added to the pool?
    Water Spite, Earth Sprite, Fire Sprite, Duck Sprite, Ghost Sprite, 
    Demon Sprite, King Sprite, Dream Sprite, Punk Sprite and Zero Point Sprite"""
    #display_name = "Utility Toggle"
    default = True
class ProgressiveFishing(Range): # type: ignore
    """Should Harpoon Guns and Fishing Rods be Progressive, Seperate items or not Exist??
    1: Fishing Rod -> Pro Fishing Rod, Harpoon Gun -> Enhanced Harpoon Gun
    2: Progressive Fishing Rod, Progressive Harpoon Gun
    3: Items do not Exist in the Item Pool"""
    #display_name = "Progressive Fishing"
    default = 2
    range_start = 1
    range_end = 3
class SuperWeaponVarients(Toggle): # type: ignore
    """Should Upgraded Weapons be an Addition Unlockable or Share Items with their non Mythic Parts?
    They would still require the need for 'Rarity - Legendary/Mythic' or Progressive to be Useable.
    Examples include; Wolfe's Maven Auto Shotgun, Voidbalde's Burst Rifle, Skeletor's Extending Shotgun, 
                      9mm Baba Yaga Pistol and The Limitless Seven Sliders.
    False: Items are Like their Counterparts
    True: Items are added to the Pool"""
    #display_name = "Upgraded Weapons"
    default = False
#   -------------------- ( Skills )--------------------
class LessonSkills(OptionList):
    """A set of actions required to do certain things. The list below are for possible items in the pool, remove if not desired.
    Dance Lessons:      The Ability to Emote or Shoulder Ride/Carry
    Driving Lessons:    The Ability to Drive a Motorized Vehicle
    Forage Lessons:     The Ability to use/collect Foarge items (Apples, Mushrooms)
    Building Lessons:   The Ability to Build in Build Playlists (User Choice if this includes Port-A-Bunkers)
    Searchable Lessons: The Ability to Search Containers (Checsts, Ammo Boxes, Produce Boxes, Safes, Cash Registers, etc.)
    Fishing Lessons:    The Ability to Fish in Water and Fishing Holes"""
    display_name = "Skills"
    default = ["Dance Lessons", "Searchable Lessons", "Driving Lessons", "Forage Lessons", "Building Lessons", "Fishing Lessons"]
class ShoppingToggle(OptionList): # type: ignore 
    """A set of actions required to do certain things. The list below are for possible items in the pool, remove if not desired.
    Gold Spender:       The Ability to Use Vending Machines or Aquire Services
    Sprite Dust:        The Ability to Use Sprite Dust for Purchases
    Ammo Restock:       Restock your Ammo to Full
    Recruit Character:  Hire (Character)
    Patch Up:           Heal up to 40 Health or Heal 100 Health/Shield (Vending or NPC)
    Activate Rift:      Summon a Rift
    Upgrade Weapon:     Upgrade Weapon to Next Rarity"""
    display_name = "Shopping  Toggle"
    default = ["Gold Spender","Sprite Dust","Ammo Restock","Recruit Character","Patch Up", "Activate Rift","Upgrade Weapon"]
class WeaponMastery(Toggle): # type: ignore
    """A set of Masteries in order to operate specific Weapon Types
    Assault Rifle:  Chaos Exploder Rifle, Surgical Pulse Rifle, 
                    Warforged Assault Rifle and Hunting Rifle
    Shotgun:        Extending Focus Shotgun, Striker Pump Shotgun, Maven Auto Shotgun
    SMG:            Flex SMG, Stinger SMG
    Pistol:         Ranger Pistol, Lancehead Pistol"""
    #display_name = "Masteries"
    default = True
class ProgressiveGamemode(Toggle): # type: ignore
    """Should the need to access Duo, Trios and Squad playlists be locked behind Progressive Gamemodes?
    True: Progressive Gamemodes are added to the pool
    False: There are no Gamemode items added to the pool"""
    #display_name = "Progressive GM"
    default = False
class MoveRando(Toggle): # type: ignore #done
    """Would you like to restrict player Movement? (No Logic, WIP)
    Jump, Sprint, Ledge Jump, Wall Scramble, Mantle, Crouch, Sliding, Swiming and Hurdling"""
    default = False
    
#-- Unused --------------------------
class StabilizeWeaponsToggle(Toggle): # type: ignore # Not the call, too much to keep track and guess # Item
    """Would you like to add all of the possible Weapons from the 'Stabilize the Anomaly' Rift Event as items?
    True: Add's the Items, preventing the User from using them until unlocked
    False: The user can use these items and they arent added to the pool
    Barron's Double Down Pistol, Overclocked Pulse Rifle, Havoc Pump Shotgun, Havoc Suppressed AR, Explosive Repeater Rifle, Reaper Sniper Rifle, Grapple Blade, Chains of Hades, Typhoon Blade, The Kneecapper\nWeapons may not be up to date..."""
    display_name = "Rift Weapons"
    default = False
class RiftAnomaliesToggle(Toggle): # type: ignore
    """Would you like to add specific Anomaly Actions as locations?
    Stabilize the Anomaly: Complete the Rift Anomaly
    The Llamanomaly: Ride a Llama and take it for loot!"""
    #display_name = "Anomaly Toggle"
    default = True

# This is called before any manual options are defined, in case you want to define your own with a clean slate or let Manual define over them
def before_options_defined(options: dict[str, Type[Option[Any]]]) -> dict[str, Type[Option[Any]]]: # type: ignore

#-- Goals --------------------------------------------------
    options["victory_crowns"] = VictoryCrowns
    options["elimination_goal"] = EliminationTokens
    options["accolade_precentage"] = AccoladeGoal
#-- Locations ----------------------------------------------
    options["remove_accolades"] = RemoveAccolades
    options["archipelago_locations"] = ArchipelagoLocations 
    options["boss_hunt"] = BossHunt
    #options["rift_anomalies"] = RiftAnomaliesToggle 
    options["elimination_locations"] = EliminationLocations
#-- Rarity -------------------------------------------------
    options["rarity_toggle"] = RarityEnabled
    options["progressive_rarities"] = ProgressiveRarities
    options["rarity_counts"] = ProgressiveRarityCount
#--  Items -------------------------------------------------
    options["resourceful_materials"] = Resourcefulness
    options["starting_pocket_item"] = StartingPocketItem
    options["vault_key_cards"] = VaultKeyCards 
    options["consumable_toggle"] = ConsumableToggle
    options["utlity_toggle"] = UtilityToggle 
    options["sprite_toggle"] = SpriteToggle
    #options["progressive_fishing"] = ProgressiveFishing 
    options["super_weapon_varients"] = SuperWeaponVarients 
#-- Skills -------------------------------------------------
    options["lesson_skills"] = LessonSkills
    options["shopping_items"] = ShoppingToggle
    options["weapon_mastery"] = WeaponMastery 
    options["progressive_gamemode"] = ProgressiveGamemode 
    options["move_randomization"] = MoveRando 

    return options

# This is called after any manual options are defined, in case you want to see what options are defined or want to modify the defined options
def after_options_defined(options: Type[PerGameCommonOptions]): # type: ignore
    # To access a modifiable version of options check the dict in options.type_hints
    # For example if you want to change DLC_enabled's display name you would do:
    # options.type_hints["DLC_enabled"].display_name = "New Display Name"
    #options["move_randomization"].__doc__ = """
        #Choose your victory condition.
        #- Goal 1: Description.
        #- Goal 2: Description.
        #"""
    #return options

    #  Here's an example on how to add your aliases to the generated goal
    # options.type_hints['goal'].aliases.update({"example": 0, "second_alias": 1})
    # options.type_hints['goal'].options.update({"example": 0, "second_alias": 1})  #for an alias to be valid it must also be in options

    pass

# Use this Hook if you want to add your Option to an Option group (existing or not)
def before_option_groups_created(groups: dict[str, list[Type[Option[Any]]]]) -> dict[str, list[Type[Option[Any]]]]: # type: ignore
    
    groups['Goal Options'] = [VictoryCrowns,EliminationTokens,AccoladeGoal]

    groups['Locations'] = [RemoveAccolades,ArchipelagoLocations,BossHunt,EliminationLocations] #RiftAnomaliesToggle

    groups['Rarity'] = [RarityEnabled,ProgressiveRarities,ProgressiveRarityCount]

    groups['Items'] = [Resourcefulness,StartingPocketItem,VaultKeyCards,SpriteToggle,ConsumableToggle,UtilityToggle,SuperWeaponVarients]

    groups['Skills'] = [LessonSkills,ShoppingToggle,WeaponMastery,ProgressiveGamemode,MoveRando]

    return groups

def after_option_groups_created(groups: list[OptionGroup]) -> list[OptionGroup]: # type: ignore
    return groups
