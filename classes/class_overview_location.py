# -*- coding: utf-8 -*-
import random

class OverviewLocation:
    
    part_01 = [
        "Adamantine", "Aerial", "Airborne", "Amphibious", "Ancient", 
        "Arachnid", "Aromatic", "Astrological", "Asymmetrical", 
        "Azure", "Belowground", "Bizarre", "Black", 
        "Blackened", "Bleak", "Blue", "Blue glowing", 
        "Bone", "Breathing", "Bronze", "Brooding", 
        "Bubbling", "Buried", "Calcified", "Celestial", 
        "Chiseled", "Chosen", "Circuitous", "Circular", 
        "Clay", "Cliff", "Coastal", "Coiled", 
        "Collapsing", "Concealed", "Conquered", "Contaminated", 
        "Contemplation", "Convoluted", "Corroded", "Criminal", 
        "Crimson", "Crooked", "Crude", "Cruel", 
        "Crumbling", "Cryptic", "Crystalline", "Cunning", 
        "Curious", "Cursed", "Cyclopean", "Dank", "Dark", 
        "Dead", "Deadly", "Death", "Decaying", "Deceptive", 
        "Decomposing", "Defiled", "Demolished", "Demonic", "Desolate", 
        "Destroyed", "Devious", "Diamond", "Dilapidated", "Dimensional", 
        "Diseased", "Disorienting", "Divided", "Dormant", "Double", 
        "Dream", "Drilling", "Earthen", "Ebony", "Eldritch", 
        "Elliptical", "Emerald", "Enchanted", "Enclosed", "Entombed", 
        "Eroding", "Erratic", "Ethereal", "Fabrication", "Factory", 
        "Fear","Feeding", "Fertile", "Flesh","Fortified", 
        "Fortress","Fossilized", "Frightful", "Gas","Glittering", 
        "Granite", "Green", "Grey", "Gruesome","Harvest",
        "Heliotropic", "Hidden", "High", "Hollowed","Horned", 
        "Horrid", "Hunting", "Hydroponic", "Industrial", "Intermittent", 
        "Intriguing", "Inverted", "Invulnerable", "Isolated", "Labyrinthine", 
        "Lethargy","Levitating", "Limestone", "Living", "Midnight", 
        "Moaning", "Monastic", "Mosaic", "Mountain", "Mud",
        "Murder","Nest","Obsidian", "Octagonal", "Offshore", 
        "Orb","Painted", "Pearly", "Perilous", "Philosophical", 
        "Platform", "Pod","Poisoned", "Poorly-built","Pulsing", 
        "Putrid", "Quaking", "Ramshackle", "Red", "Remade", 
        "Reversible", "Ruined", "Rune","Sacrificial", "Sapphire", 
        "Scarlet", "Sea-swept", "Seaweed","Sentient", "Shadow",
        "Ship","Shunned","Silent","Singular","Sinister",
        "Slaying","Spiraling","Star","Star-shaped","Storm-tossed",
        "Sub","Sunken","Tall","Temporal","Temporary",
        "Three-Part","Titanic","Towering","Toxic","Treasure",
        "Triangular","Trinket","Tumbled","Twilight","Unearthed",
        "Unfinished","Unnatural","Unsealed","Unstable","Unthinkable",
        "Urban","Vertical","Vile","Wailing","Walled",
        "Waterborne","Watery","Weird", "White", "Wooden" 
        ]

    part_02 = [
        "Abbey of the", "Aerie of the", "Asylum of the", "Aviary of the", 
        "Barracks of the", "Bastion of the", "Bazaar of the", "Bluffs of the", 
        "Brewery of the", "Bridge of the", "Cairn of the", "Canyon of the", 
        "Carnival of the", "Castle of the","Cathedral of the", "Cellars of the", 
        "Chapel of the", "Chapterhouse of the", "Church of the", "City of the", 
        "Cliffs of the", "Cloister of the", "Cocoon of the", "Coliseum of the", 
        "Contrivance of the", "Cottage of the", "Court of the", "Cradle of the", 
        "Crags of the", "Craters of the", "Crypt of the", "Demi-plane of the", 
        "Dens of the", "Dimension of the", "Domain of the", "Domains of the", 
        "Dome of the", "Dungeons of the", "Dwelling of the", "Edifice of the", 
        "Fane of the", "Farm of the", "Forest of the", "Forge of the", 
        "Fortress of the", "Foundry of the", "Galleon of the", "Galleries of the", 
        "Garden of the", "Garrison of the", "Generator of the", "Glade of the", 
        "Globe of the", "Grotto of the", "Hall of the", "Halls of the", 
        "Harbor of the", "Hatcheries of the", "Haven of the", "Hill of the", 
        "Hive of the", "Holt of the", "House of the", "Hut of the", 
        "Island of the", "Isles of the", "Jungle of the", "Keep of the", 
        "Kennels of the", "Labyrinth of the", "Lair of the", "Lighthouse of the", 
        "Lodgings of the", "Manse of the", "Mansion of the", "Marsh of the", 
        "Maze of the", "Megalith of the", "Mill of the", "Mines of the", 
        "Monastery of the", "Monolith of the", "Mounds of the", "Necropolis of the", 
        "Nest of the", "Obelisk of the", "Outpost of the", "Pagoda of the", 
        "Palace of the", "Pavilion of the", "Pits of the", "Plane of the", 
        "Prison of the", "Pyramid of the", "Rift of the","Sanctuary of the",
        "Sanctum of the","Shrine of the","Spire of the","Stockades of the",
        "Stronghold of the","Tower of the", "Webs of the", "Zeppelin of the" 
        ]
    
    part_03 = [
        "Ant", "Ape", "Armored","Army of the", "Artificial", "Baboon",
        "Bandit", "Bat","Bear", "Beetle","Bitter", "Blood", 
        "Bone","Brain", "Breeding", "Broken", "Bronze", "Burned", 
        "Cabalistic", "Carnal", "Caterpillar","Centipede","Changing", 
        "Chaos","Clan of the", "Cloned", "Cloud","Cockroach",
        "Conjoined", "Crimson", "Crippled", "Crocodile","Cursed", 
        "Dark", "Death","Decayed", "Deceitful", "Deluded", 
        "Demonic", "Deranged", "Dinosaur","Diseased", "Dragonfly",
        "Dread", "Elemental", "Elephant","Enchanted", "Enslaved", 
        "Feathered", "Feral", "Fiery", "Flame", "Flying", 
        "Forest", "Frost", "Genius", "Ghostly", "Giant", 
        "Gluttonous", "Gnarled", "Grotesque", "Guardian", "Half-breed", 
        "Hallucinogenic", "Heart","Hellish", "Hive", "Hollow", 
        "Horde of the", "Horned", "Horrific", "Howling", "Hunchback", 
        "Hybrid", "Hyena","Ice", "Immoral", "Immortal", "Imprisoned", 
        "Insane", "Insatiable", "Insidious", "Iron", "Jackal",
        "Jade", "Jewel", "Lava", "Leech","Leeching", "Legendary", 
        "Leopard","Lesser", "Lion","Loathsome", "Lunar", "Mad", 
        "Mammoth","Man-eating", "Mantis","Many-legged", "Massive", 
        "Master", "Mastermind", "Mechanical", "Mental", "Mind", 
        "Minions of the", "Mist","Monkey","Moon","Moth",
        "Mutant", "Mutant", "Narcotic", "Ooze", "Outlawed", 
        "Poisonous", "Polluted", "Predatory", "Raider","Rat",
        "Reaver", "Reawakened", "Resurrected", "Sabertooth", "Sabertoothed", 
        "Sand","Scarlet", "Scheming", "Scorched", "Sea",
        "Secret", "Shadow", "Shattered", "Skeletal", "Slave", 
        "Slime","Slug","Smoke", "Snail","Snake","Spell",
        "Summoned", "Tribe of the", "Twisted", "Undead", "Unholy", 
        "Unseen", "Vampiric", "Villainous", "Wasp","Water", 
        "Winged", "Worm","Wounded", "Wraith","Zombie" 
        ]
    
    part_04 = [
        "Abbot", "Actor", "Alchemist", "Altar", "Apparition", 
        "Apprentice", "Artifact", "Assassin", "Automaton", "Basilisk", 
        "Bats","Beast", "Behemoth", "Berserkers","Binder", "Bishop", 
        "Breeder", "Brood", "Brotherhood", "Burrower", "Caller", 
        "Cannibal", "Captive", "Centaur", "Ceremony", "Chalice", 
        "Changeling", "Chanter", "Chieftain of Goblins", "Chimera", "Circlet", 
        "Clan", "Cleric", "Cockatrice", "Collector", "Colossus", 
        "Combiner", "Congregation", "Coronet", "Crafter", "Crawler", 
        "Creator", "Creature", "Crown", "Cult", "Cultists", 
        "Cyclops", "Daughter", "Demigod", "Demon", "Device", "Displacer", 
        "Djinni", "Doppelganger", "Dragon", "Dreamer", "Druid", 
        "Efreet", "Egg", "Emissary", "Emperor", "Executioner", 
        "Exile", "Experimenter", "Eye", "Eyeball", "Father", 
        "Frog", "Fungus", "Gargoyles","Gatherer", "Genie", 
        "Ghosts","Ghouls", "Giants","God", "Goddess", 
        "Golem", "Grail", "Griffon", "Guardian", "Hag", 
        "Harpies", "Head", "Horde", "Hornets","Horror", 
        "Hounds","Hunter", "Hunters", "Hybrid", "Hydra", "Idol", 
        "Infiltrator", "Insect", "Jailer", "Keeper", "Killer", 
        "King", "Knight", "Larva", "Lich", "Lord", 
        "Lycanthrope", "Mage", "Magician", "Maker", "Manticore", 
        "Master", "Medusa", "Minotaurs","Monks", "Monster", 
        "Mother", "Mummy", "Mushroom", "Naga", "Nomads", 
        "Octopus", "Ogres","Oozes","People", "Pirates",
        "Priest", "Priesthood", "Priests","Prince", "Princess", 
        "Puddings","Puppet", "Puppet master","Rakshasa", "Rats",
        "Reaver", "Resurrectionist", "Salamander", "Satyr", "Scholar", 
        "Scorpion", "Seed", "Serpent", "Shaman", "Shaman of the Orcs",
        "Shaper", "Simulacrum", "Sisterhood", "Skeletons", "Slimes",
        "Slitherer", "Society", "Son", "Sorcerer", "Sorceress", 
        "Spawn", "Sphinx", "Spiders","Spirits", "Star", "Statue", 
        "Statues","Surgeon", "Titan", "Toad", "Tree", 
        "Trees","Tribe","Troglodytes", "Trolls","Tyrant", 
        "Walker", "Warlord", "Warlord of the Orcs", "Wasps","Weaver", 
        "Whisperer", "Witch", "Wizard", "Wolves", "Worg",
        "Worm", "Wyrm", "Wyvern", "Yeti", "Zombies" 
        ]


    
    def __init__(self):
        pass



    def getResult(self):
        a = random.randint(0, len(self.part_01) - 1)
        b = random.randint(0, len(self.part_02) - 1)
        c = random.randint(0, len(self.part_03) - 1)
        d = random.randint(0, len(self.part_04) - 1)
        return self.part_01[a] + " " + self.part_02[b] + " " + self.part_03[c] + " " + self.part_04[d]
        