"""
Variables for The Chasm
"""

from classes import * # Importing classes

# Miscellaneous Variables
debug_toggles : dict = {
    "true_sight" : False,
    "instant_break" : False,
    "omniscience" : False
}
MAP_LENGTH : int = 40
MAP_HEIGHT : int = 20
XP_SCALING_FACTOR : int = 5
current_map : str = ""
current_screen : str = "title"
RESET_ON_START : bool = False
current_menu_options : list = []
selected_option : str = None

# Banners
program_banner : list = [
    "                                                                           ",
    "@@@@@@@ @@@  @@@ @@@@@@@@     @@@@@@@ @@@  @@@  @@@@@@   @@@@@@ @@@@@@@@@@ ",
    "  @!!   @@!  @@@ @@!         !@@      @@!  @@@ @@!  @@@ !@@     @@! @@! @@!",
    "  @!!   @!@!@!@! @!!!:!      !@!      @!@!@!@! @!@!@!@!  !@@!!  @!! !!@ @!@",
    "  !!:   !!:  !!! !!:         :!!      !!:  !!! !!:  !!!     !:! !!:     !!:",
    "   :     :   : : : :: ::      :: :: :  :   : :  :   : : ::.: :   :      :  ",
    "                                                                           "
]

menu_banner : list = [
    "                                      ",
    "@@@@@@@@@@  @@@@@@@@ @@@  @@@ @@@  @@@",
    "@@! @@! @@! @@!      @@!@!@@@ @@!  @@@",
    "@!! !!@ @!@ @!!!:!   @!@@!!@! @!@  !@!",
    "!!:     !!: !!:      !!:  !!! !!:  !!!",
    " :      :   : :: ::  ::    :   :.:: : ",
    "                                      "
]

skills_banner : list = [
    "                                              ",
    " @@@@@@ @@@  @@@ @@@ @@@      @@@       @@@@@@",
    "!@@     @@!  !@@ @@! @@!      @@!      !@@    ",
    " !@@!!  @!@@!@!  !!@ @!!      @!!       !@@!! ",
    "    !:! !!: :!!  !!: !!:      !!:          !:!",
    "::.: :   :   ::: :   : ::.: : : ::.: : ::.: : ",
    "                                              "
]

inventory_banner : list = [
    "                                                                         ",
    "@@@ @@@  @@@ @@@  @@@ @@@@@@@@ @@@  @@@ @@@@@@@  @@@@@@  @@@@@@@  @@@ @@@",
    "@@! @@!@!@@@ @@!  @@@ @@!      @@!@!@@@   @!!   @@!  @@@ @@!  @@@ @@! !@@",
    "!!@ @!@@!!@! @!@  !@! @!!!:!   @!@@!!@!   @!!   @!@  !@! @!@!!@!   !@!@! ",
    "!!: !!:  !!!  !: .:!  !!:      !!:  !!!   !!:   !!:  !!! !!: :!!    !!:  ",
    ":   ::    :     ::    : :: ::  ::    :     :     : :. :   :   : :   .:   ",
    "                                                                         "
]

crafting_banner : list = [
    "                                                                  ",
    " @@@@@@@ @@@@@@@   @@@@@@  @@@@@@@@ @@@@@@@ @@@ @@@  @@@  @@@@@@@ ",
    "!@@      @@!  @@@ @@!  @@@ @@!        @!!   @@! @@!@!@@@ !@@      ",
    "!@!      @!@!!@!  @!@!@!@! @!!!:!     @!!   !!@ @!@@!!@! !@! @!@!@",
    ":!!      !!: :!!  !!:  !!! !!:        !!:   !!: !!:  !!! :!!   !!:",
    " :: :: :  :   : :  :   : :  :          :    :   ::    :   :: :: : ",
    "                                                                  "
]

stats_banner : list = [
    "                                        ",
    " @@@@@@ @@@@@@@  @@@@@@  @@@@@@@  @@@@@@",
    "!@@       @!!   @@!  @@@   @!!   !@@    ",
    " !@@!!    @!!   @!@!@!@!   @!!    !@@!! ",
    "    !:!   !!:   !!:  !!!   !!:       !:!",
    "::.: :     :     :   : :    :    ::.: : ",
    "                                        "
]

# Tileset
PLAYER        : str = "P"
EMPTY         : str = "·"
BORDER        : str = "░"
ORE_NODE      : str = "■"
RARE_ORE_NODE : str = "◙"
GEM_NODE      : str = "▲"
RARE_GEM_NODE : str = "♦"
PLANT         : str = "♣"
RARE_PLANT    : str = "♠"
LADDER_UP     : str = "↑"
LADDER_DOWN   : str = "↓"

# Resource Data
ORE_DATA : dict = {
    "Ores" : [
        "Stone",
        
        "Raw Copper",
        
        "Raw Iron",

        "Raw Silver",

        "Raw Gold",

        "Raw Platinum",

        "Raw Bismuth",

        "Raw Titanium",

        "Raw Abyssite"
    ],
    "Generation Data" : {
        # Type (STR)  : (Chance (FLOAT), Expected Depth (INT))
        "Stone"        : (0.75, 1),

        "Raw Copper"   : (0.35, 5),

        "Raw Iron"     : (0.2, 10),

        "Raw Silver"   : (0.15, 24),

        "Raw Gold"     : (0.1, 57),

        "Raw Platinum" : (0.05, 66),

        "Raw Bismuth"  : (0.025, 81),

        "Raw Titanium" : (0.005, 90),

        "Raw Abyssite" : (0.0025, 100)
    },
    "Format Data" : {
        "Stone"        : (ORE_NODE, ("lightblack", "bright", "black")),

        "Raw Copper"   : (ORE_NODE, ("yellow", "bright", "black")),

        "Raw Iron"     : (ORE_NODE, ("white", "bright", "black")),

        "Raw Silver"   : (ORE_NODE, ("lightwhite", "bright", "black")),

        "Raw Gold"     : (ORE_NODE, ("lightyellow", "bright", "black")),

        "Raw Platinum" : (ORE_NODE, ("lightblue", "bright", "black")),

        "Raw Bismuth"  : (RARE_ORE_NODE, ("lightmagenta", "bright", "black")),

        "Raw Titanium" : (RARE_ORE_NODE, ("blue", "bright", "black")),

        "Raw Abyssite" : (RARE_ORE_NODE, ("magenta", "bright", "black"))
    },
    "Other Data" : {
        # Type (STR) : (Average Health (INT), Average Amount (INT), Tier Required (INT))
        "Stone"        : (3, 5, 1),

        "Raw Copper"   : (4, 5, 1),

        "Raw Iron"     : (6, 5, 2),

        "Raw Silver"   : (7, 5, 3),

        "Raw Gold"     : (10, 4, 4),

        "Raw Platinum" : (14, 4, 5),

        "Raw Bismuth"  : (19, 3, 7),

        "Raw Titanium" : (25, 2, 10),

        "Raw Abyssite" : (50, 2, 15)
    }
}
GEM_DATA : dict = {
    "Gems" : [
        "Amethyst",

        "Topaz",

        "Sapphire",

        "Emerald",

        "Ruby",

        "Diamond",

        "Painite",

        "Onyx",

        "Tourmaline",

        "Kyanite",

        "Vantalite"
    ],
    "Generation Data" : {
        # Type (STR) : (Chance (FLOAT), Expected Depth (INT))
        "Amethyst"   : (0.5, 1),

        "Topaz"      : (0.35, 8),

        "Sapphire"   : (0.25, 17),
        
        "Emerald"    : (0.15, 25),

        "Ruby"       : (0.1, 36),

        "Diamond"    : (0.05, 42),

        "Painite"    : (0.025, 58),

        "Onyx"       : (0.025, 71),

        "Tourmaline" : (0.01, 86),

        "Kyanite"    : (0.005, 93),

        "Vantalite"  : (0.001, 100)
    },
    "Format Data" : {
        "Amethyst"   : (GEM_NODE, ("magenta", "bright", "black")),

        "Topaz"      : (GEM_NODE, ("yellow", "bright", "black")),

        "Sapphire"   : (GEM_NODE, ("blue", "bright", "black")),

        "Emerald"    : (GEM_NODE, ("green", "bright", "black")),

        "Ruby"       : (GEM_NODE, ("red", "bright", "black")),

        "Diamond"    : (GEM_NODE, ("lightblue", "bright", "black")),

        "Painite"    : (GEM_NODE, ("lightred", "bright", "black")),

        "Onyx"       : (RARE_GEM_NODE, ("black", "bright", "black")),

        "Tourmaline" : (RARE_GEM_NODE, ("lightgreen", "bright", "black")),

        "Kyanite"    : (RARE_GEM_NODE, ("lightcyan", "bright", "black")),

        "Vantalite"  : (RARE_GEM_NODE, ("lightmagenta", "bright", "black"))
    },
    "Other Data" : {
        # Type (STR) : (Average Health (INT), Average Amount (INT), Tier Required (INT))
        "Amethyst"   : (2, 6, 1),

        "Topaz"      : (3, 6, 1),

        "Sapphire"   : (5, 5, 2),

        "Emerald"    : (8, 5, 4),

        "Ruby"       : (9, 5, 4),

        "Diamond"    : (13, 4, 5),

        "Painite"    : (16, 4, 6),

        "Onyx"       : (20, 3, 7),

        "Tourmaline" : (35, 3, 9),

        "Kyanite"    : (50, 2, 12),

        "Vantalite"  : (75, 2, 15)
    }
}
PLANT_DATA : dict = {
    "Plants" : [
        "Grass",

        "Small Roots",
        
        "Large Roots",

        "Deep Algae",

        "Luminous Moss",

        "Dark Fungus"
    ],
    "Generation Data" : {
        # Type (STR) : (Chance (FLOAT), Expected Depth (INT))
        "Grass"         : (0.5, 1),

        "Small Roots"   : (0.25, 12),

        "Large Roots"   : (0.125, 26),

        "Deep Algae"    : (0.05, 42),

        "Luminous Moss" : (0.025, 60),

        "Dark Fungus"   : (0.005, 100)
    },
    "Format Data" : {
        "Grass"         : (PLANT, ("lightgreen", "bright", "black")),

        "Small Roots"   : (PLANT, ("lightyellow", "bright", "black")),

        "Large Roots"   : (PLANT, ("yellow", "bright", "black")),
        
        "Deep Algae"    : (PLANT, ("green", "bright", "black")),

        "Luminous Moss" : (RARE_PLANT, ("lightcyan", "bright", "black")),

        "Dark Fungus"   : (RARE_PLANT, ("black", "bright", "black"))
    },
    "Other Data" : {
        # Type (STR)    : (Average Health (INT), Average Amount (INT), Tier Required (INT))
        "Grass"         : (1, 7, 1),

        "Small Roots"   : (2, 5, 2),

        "Large Roots"   : (4, 4, 5),

        "Deep Algae"    : (10, 3, 7),

        "Luminous Moss" : (25, 2, 11),

        "Dark Fungus"   : (65, 1, 15)
    }
}

# Skills Data
SKILLS : dict = {
    # Skill Name (STR) : Max Level (INT)
    "Darkvision"    : 5,    # Reduces darkness creep.

    "Fortunate"     : 5,    # Increases resource gain by 50% per level

    "Hard Hitting"  : 10,   # Increases damage dealt to resource nodes by 50% per level.

    "Surefire"      : 3,    # Gives you a 1/3 chance per level to ignore reflection chances on higher tier resources.

    "Quick Learner" : 10,   # Increases experience gain by 20% per level.

    "Conservation"  : 5,    # Gives you a 7.5% chance to not consume a resource when crafting per level.

    "Mastery"       : None  # Every level increases damage dealt to resource nodes by 25%, experience gain by 10%, resource gain by 20%, and reduces darkness creep. Unlocked after all other skills are maxed out, and can be upgraded infinitely.
}

SKILL_DESCRIPTIONS : dict = {
    "Darkvision"    : "Decreases darkness creep.",

    "Fortunate"     : "+50%% resources.",

    "Hard Hitting"  : "+50%% damage.",

    "Surefire"      : "+33.3%% chance to ignore deflections.",

    "Quick Learner" : "+20%% experience.",

    "Conservation"  : "+7.5%% resource conservation.",

    "Mastery"       : "+25%% damage, +10%% experience, +20%% resources, decreases darkness creep."
}

# Recipe Data
# Basic Recipes
RECIPES = {
    "Refined_Stone"       : Recipe("Refined Stone", 1, {"Stone": 2}, 2),

    "Copper_Ingot"        : Recipe("Copper Ingot", 1, {"Raw Copper" : 3}, 4),

    "Iron_Ingot"          : Recipe("Iron Ingot", 1, {"Raw Iron" : 3}, 5),

    "Silver_Ingot"        : Recipe("Silver Ingot", 1, {"Raw Silver" : 4}, 8),

    "Gold_Ingot"          : Recipe("Gold Ingot", 1, {"Raw Gold" : 4}, 10),

    "Platinum_Ingot"      : Recipe("Platinum Ingot", 1, {"Raw Platinum" : 4}, 12),

    "Bismuth_Ingot"       : Recipe("Bismuth Ingot", 1, {"Raw Bismuth" : 5}, 15),

    "Titanium_Ingot"      : Recipe("Titanium Ingot", 1, {"Raw Titanium" : 5}, 18),

    "Abyssite_Ingot"      : Recipe("Abyssite Ingot", 1, {"Raw Abyssite" : 6}, 25),

    # Alloys
    "Steel_Bar"           : Recipe("Steel Bar", 2, {"Iron Ingot" : 1, "Stone" : 4}, 10),

    "Rubinum_Alloy"       : Recipe("Rubinum Alloy", 1, {"Platinum Ingot" : 1, "Ruby" : 3}, 15),

    "Emeruth_Alloy"       : Recipe("Emeruth Alloy", 1, {"Bismuth Ingot" : 1, "Emerald" : 3}, 20),

    "Diamanium_Alloy"     : Recipe("Diamanium Alloy", 1, {"Titanium Ingot" : 1, "Diamond" : 3}, 25),

    "Vanabyss_Alloy"      : Recipe("Vanabyss Alloy", 1, {"Abyssite Ingot" : 1, "Vanalite" : 3}, 35),

    # Fibers
    "Simple_Fiber"        : Recipe("Simple Fiber", 3, {"Small Roots" : 3}, 2),

    "Advanced_Fiber"      : Recipe("Advanced Fiber", 2, {"Simple Fiber" : 1, "Large Roots" : 1}, 10),

    "Luminous_Fiber"      : Recipe("Luminous Fiber", 1, {"Advanced Fiber" : 1, "Luminous Moss" : 2}, 20),

    # Catalysts
    "Basic_Catalyst"      : Recipe("Basic Catalyst", 1, {"Copper Ingot" : 10, "Iron Ingot" : 5, "Refined Stone" : 25, "Simple Fiber" : 20, "Amethyst" : 5}, 10),

    "Sturdy_Catalyst"     : Recipe("Sturdy Catalyst", 1, {"Basic Catalyst" : 3, "Platinum Ingot" : 10, "Steel Bar" : 15, "Sapphire" : 10}, 30),

    "Alloy_Catalyst"      : Recipe("Alloy Catalyst", 1, {"Sturdy Catalyst" : 5, "Rubinum Alloy" : 10, "Emeruth Alloy" : 10, "Diamanium Alloy" : 10, "Advanced Fiber" : 10, "Onyx" : 5}, 50),

    "Sparkling_Catalyst"  : Recipe("Sparkling Catalyst", 1, {"Alloy Catalyst" : 10, "Tourmaline" : 15, "Kyanite" : 10, "Painite" : 25}, 100),

    "Void_Catalyst"       : Recipe("Void Catalyst", 1, {"Sparkling Catalyst" : 15,"Vanabyss Ingot" : 15, "Vanalite" : 5, "Dark Fungus" : 10, "Luminous Fiber" : 5}, 250),

    "Supreme Catalyst"    : Recipe("Supreme Catalyst", 1, {"Vanabyss Alloy" : 25, "Void Catalyst" : 25, "Alloyed Catalyst" : 25, "Sturdy Catalyst" : 25, "Basic Catalyst" : 25}, 5000)
}
# Item Descriptions
DESCRIPTIONS : dict = {
    # Raw Materials
    "Stone"                 : "A chunk of rock. Largely unremarkable.",

    "Raw Copper"            : "An unrefined piece of copper. Conducts electricity.",

    "Raw Iron"              : "An unrefined piece of iron. Slightly magnetic.",

    "Raw Silver"            : "An unrefined piece of silver. Slightly reflective.",

    "Raw Gold"              : "An unrefined piece of gold. Very valuable.",

    "Raw Platinum"          : "An unrefined piece of platinum. Moderately durable.",

    "Raw Bismuth"           : "An unrefined piece of bismuth. Very colorful.",

    "Raw Titanium"          : "An unrefined piece of titanium. very durable.",

    "Raw Abyssite"          : "An unrefined piece of abyssite. Vibrating.",

    "Amethyst"              : "An amethyst crystal. Oddly soothing.",

    "Topaz"                 : "A topaz crystal. Very tough.",

    "Sapphire"              : "A sapphire crystal. Resists abrasions.",

    "Emerald"               : "An emerald crystal. Slightly tough.",

    "Ruby"                  : "A ruby crystal. Faintly glows.",

    "Diamond"               : "A diamond crystal. Extremely tough.",

    "Painite"               : "A painite crystal. Vibrant and lustrous.",

    "Onyx"                  : "An onyx crystal. Jet black and smooth.",

    "Tourmaline"            : "A tourmaline crystal. Generates electricity.",

    "Kyanite"               : "A kyanite crystal. Shifts in color occasionally.",

    "Vantalite"             : "A vantalite crystal. Does not reflect light.",

    "Grass"                 : "A handful of grass. Flammable when dried.",

    "Small Roots"           : "A handful of roots. Slightly damp.",

    "Large Roots"           : "A few large roots. Very tough.",

    "Deep Algae"            : "A chunk of algae. Soft and squishy.",

    "Luminous Moss"         : "A chunk of moss. Glows in the dark.",

    "Dark Fungus"           : "A black fungus. Highly poisonous.",

    # Crafted Items
    "Refined Stone"         : "A smooth clump of rock. It's kind of shiny.",

    "Copper Ingot"          : "An ingot of copper. Conducts electricity better.",

    "Iron Ingot"            : "An ingot of iron. It's magnetism is increased.",

    "Silver Ingot"          : "An ingot of silver. You can see your reflection.",

    "Gold Ingot"            : "An ingot of gold. Extremely valuable.",

    "Platinum Ingot"        : "An ingot of platinum. More durable than platinum ore.",

    "Bismuth Ingot"         : "An ingot of bismuth. Its color is more vibrant.",

    "Titanium Ingot"        : "An ingot of titanium. Extremely durable.",

    "Abyssite Ingot"        : "An ingot of abyssite. Emits a small humming noise.",

    "Steel Bar"             : "A rod of steel. Very rigid.",

    "Rubinum Alloy"         : "A mix of ruby and platinum. Glows when struck.",

    "Emeruth Alloy"         : "A mix of emerald and bismuth. Very, very colorful.",

    "Diamanium Alloy"       : "A mix of diamond and titanium. Almost indestructible.",

    "Vanabyss Alloy"        : "A mix of vanalite and abyssite. Freezing cold and pitch black.",

    "Simple Fiber"          : "Fibers made of roots. Made to fasten objects.",

    "Advanced Fiber"        : "More durable fibers. Much stronger and thicker.",

    "Luminous Fiber"        : "High quality fibers. Glows brighter when stretched.",

    "Basic Catalyst"        : "The first catalyst. One of many.",

    "Sturdy Catalyst"       : "The second catalyst. Very strong.",

    "Alloy Catalyst"        : "The third catalyst. An alloy of alloys.",

    "Sparkling Catalyst"    : "The fourth catalyst. Emits a brilliant aura.",

    "Void Catalyst"         : "The fifth catalyst. Dark and cold.",

    "Supreme Catalyst"      : "The last catalyst. The zenith of your journey."
}

HARVESTER_REQUIREMENTS = {
    "Tier 2 Harvester"    : Harvester_Recipe("Tier 2 Harvester", {"Refined Stone" : 10, "Amethyst" : 10}),

    "Tier 3 Harvester"    : Harvester_Recipe("Tier 3 Harvester", {"Copper Ingot" : 10, "Refined Stone" : 15, "Topaz" : 15}),

    "Tier 4 Harvester"    : Harvester_Recipe("Tier 4 Harvester", {"Iron Ingot" : 15, "Simple Fiber" : 5, "Sapphire" : 15}),

    "Tier 5 Harvester"    : Harvester_Recipe("Tier 5 Harvester", {"Steel Bar" : 10, "Iron Ingot" : 25, "Basic Catalyst" : 5}),

    "Tier 6 Harvester"    : Harvester_Recipe("Tier 6 Harvester", {"Silver Ingot" : 15, "Sapphire" : 35}),

    "Tier 7 Harvester"    : Harvester_Recipe("Tier 7 Harvester", {"Gold Ingot" : 15, "Silver Ingot" : 20, "Steel Bar" : 20, "Sturdy Catalyst" : 5}),

    "Tier 8 Harvester"    : Harvester_Recipe("Tier 8 Harvester", {"Platinum Ingot" : 20, "Gold Ingot" : 30, "Ruby" : 10}),

    "Tier 9 Harvester"    : Harvester_Recipe("Tier 9 Harvester", {"Rubinum Alloy" : 20, "Platinum Ingot" : 10, "Ruby" : 5}),

    "Tier 10 Harvester"   : Harvester_Recipe("Tier 10 Harvester", {"Bismuth Ingot" : 25, "Steel Bar" : 35, "Platinum Ingot" : 30}),

    "Tier 11 Harvester"   : Harvester_Recipe("Tier 11 Harvester", {"Emeruth Alloy" : 30, "Bismuth Ingot" : 15, "Emerald" : 10}),

    "Tier 12 Harvester"   : Harvester_Recipe("Tier 12 Harvester", {"Titanium Ingot" : 30, "Steel Bar" : 45, "Bismuth Ingot" : 30}),

    "Tier 13 Harvester"   : Harvester_Recipe("Tier 13 Harvester", {"Diamanium Ingot" : 40, "Titanium Ingot" : 20, "Diamond" : 15, "Alloy Catalyst" : 5}),

    "Tier 14 Harvester"   : Harvester_Recipe("Tier 14 Harvester", {"Abyssite Ingot" : 45, "Vanalite" : 30, "Titanium Ingot" : 45, "Painite" : 30}),

    "Tier 15 Harvester"   : Harvester_Recipe("Tier 15 Harvester", {"Vanabyss Alloy" : 50, "Abyssite Ingot" : 30, "Vanalite" : 30, "Void Catalyst" : 5})
}