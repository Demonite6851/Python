"""
Functions for The Chasm 
"""
import random, math, keyboard, time, variables, json, os # Importing libraries/files
from colorama import *
from variables import *
from classes import *

player_data : dict = {}
map_data : dict = {}

def get_data():
    global player_data, map_data
    with open("The Chasm/player_data.json", "r") as file: # Loading data from "player_data.json".
        player_data = json.load(file)
        player_data["position"] = tuple(player_data["position"])
    
    with open("The Chasm/map_data.json", "r") as file: # Loading data from "map_data.json".
        map_data = json.load(file)

def wait_for_keys(*keys):
    while True:
        key_checker = [keyboard.is_pressed(_) for _ in keys]
        if any(key_checker):
            time.sleep(0.15)
            
            return keys[key_checker.index(True)]

def reset_data(confirm : bool = False):
    manual_confirm = False
    if confirm:
        print("\033c"+"Are you sure you want to completely erase your data?")
        if wait_for_keys("space", "esc") == "space":
            print("\033c"+"Are you REALLY sure you want to completely erase your data?")
            if wait_for_keys("space", "esc") == "space":
                manual_confirm = True
    if not confirm or manual_confirm:
        default_player_data = {
                    "position": [
                        1,
                        1
                    ],
                    "level": 1,
                    "experience": 0,
                    "skill_points": 0,
                    "skills": {
                        "Darkvision": 0,
                        "Fortunate": 0,
                        "Hard Hitting": 0,
                        "Surefire": 0,
                        "Quick Learner": 0,
                        "Conservation": 0,
                        "Mastery": 0
                    },
                    "harvester_tier": 1,
                    "inventory": {
                        "raw_materials" : {},
                        "crafted_items" : {}
                    },
                    "depth": 1,
                    "luck": 0,
                    "vision": 3}
        with open("The Chasm\map_data.json", "w") as file:
            json.dump({"maps" : {}}, file, indent = 4)
        
        with open("The Chasm\player_data.json", "w") as file:
            json.dump(default_player_data, file, indent = 4)

if RESET_ON_START: reset_data()
get_data()

def save_data():
    """
    Saves map and player data to their respective files.
    """
    for _ in player_data:
        if type(_) == tuple:
            player_data[_] = list((player_data[_]))
    
    for _ in map_data:
        if type(_) == tuple:
            map_data[_] = list((map_data[_]))
    
    with open("The Chasm\player_data.json", "w") as file:
        json.dump(player_data, file, indent = 4)
    
    with open("The Chasm\map_data.json", "w") as file:
        json.dump(map_data, file, indent = 4)

def is_valid_move(map, new_pos: tuple | list):
    
    return ((new_pos[0] in range(len(map)) and new_pos[1] in range(len(map[0]))) and get_tile(map, new_pos) in [EMPTY, LADDER_DOWN, LADDER_UP])

def get_tile(layout, position):
    
    return layout[position[0]][position[1]]

def get_valid_neighbors(map, cell: tuple):
    _ : list = []
    if is_valid_move(map, (cell[0] + 1, cell[1])):
        _.append((cell[0] + 1, cell[1]))
    
    if is_valid_move(map, (cell[0] - 1, cell[1])):
        _.append((cell[0] - 1, cell[1]))
    
    if is_valid_move(map, (cell[0], cell[1] - 1)):
        _.append((cell[0], cell[1] - 1))
    
    if is_valid_move(map, (cell[0], cell[1] + 1)):
        _.append((cell[0], cell[1] + 1))
    
    return _

def display_map():
    object_positions : list = []
    object_formats : list = []
    if map_data["maps"][variables.current_map]["nodes"]:
        object_positions = [tuple(_["position"]) for _ in map_data["maps"][variables.current_map]["nodes"].values()]
        for obj in map_data["maps"][variables.current_map]["nodes"].values():
            if obj["item"].split("_")[0] in ORE_DATA["Ores"]:
                object_formats.append(ORE_DATA["Format Data"][obj["item"]])
            
            elif obj["item"] in GEM_DATA["Gems"]:
                object_formats.append(GEM_DATA["Format Data"][obj["item"]])
            
            elif obj["item"] in PLANT_DATA["Plants"]:
                object_formats.append(PLANT_DATA["Format Data"][obj["item"]])
            
            else:
                raise ValueError(f"Resource {obj["item"]} is not a valid resource type.")
    if variables.debug_toggles["true_sight"]:
        visible_tiles : list = raycast_circle(map_data["maps"][variables.current_map]["layout"], tuple(player_data["position"]), 9999999, True)
    
    else:
        visible_tiles : list = raycast_circle(map_data["maps"][variables.current_map]["layout"], tuple(player_data["position"]), (player_data["vision"] - darkness_creep()))
    map_to_print : list = []
    map_to_print.append(f"{"".join(f"{(auto_format(BORDER, ("black", "bright", "lightblack")) * (MAP_LENGTH + 2))}")}") # Prints the top BORDER.
    for i in range(MAP_HEIGHT):
        row_to_print : list = []
        row_to_print.append(f"{auto_format(BORDER, ("black", "bright", "lightblack"))}") # Prints the left BORDER.
        for j in range(MAP_LENGTH):
            if (i, j) in visible_tiles or (i, j) == player_data["position"] or ((i, j) in object_positions and (i, j) in visible_tiles): # Checks if the current position is visible, the player"s position, or the position of a visible node.
                if (i, j) == player_data["position"]: # Runs if the current position is the player"s position.
                    row_to_print.append(f"{auto_format(PLAYER, ("lightred", "bright", "black"))}")
                
                elif ((i ,j) in object_positions and (i, j) in visible_tiles): # Runs if the current position is the position of a visible node.
                    row_to_print.append(f"{auto_format(chr(ord(object_formats[object_positions.index((i, j))][0])), object_formats[object_positions.index((i, j))][1])}")
                
                else: # Runs if the current position is NOT the player"s position AND NOT the position of a visible node.
                    match chr(ord(map_data["maps"][variables.current_map]["layout"][i][j])):
                        case variables.BORDER:
                            row_to_print.append(f"{auto_format(chr(ord(map_data["maps"][variables.current_map]["layout"][i][j])), ("black", "bright", "lightblack"))}")
                        
                        case variables.LADDER_UP | variables.LADDER_DOWN:
                            row_to_print.append(f"{auto_format(chr(ord(map_data["maps"][variables.current_map]["layout"][i][j])), ("lightwhite", "bright", "lightblack"))}")
                        
                        case variables.EMPTY | _:
                            row_to_print.append(f"{auto_format(chr(ord(map_data["maps"][variables.current_map]["layout"][i][j])), ("black", "bright", "black"))}")
            else:
                row_to_print.append(f"{auto_format(BORDER, ("lightblack", "bright", "black"))}")
        row_to_print.append(f"{auto_format(BORDER, ("black", "bright", "lightblack"))}") # Prints the right BORDER.
        map_to_print.append(f"{"".join(row_to_print)}")
    map_to_print.append(f"{"".join(f"{(auto_format(BORDER, ("black", "bright", "lightblack")) * (MAP_LENGTH + 2))}")}") # Prints the bottom BORDER.
    current_tile : tuple = None
    match chr(ord(map_data["maps"][variables.current_map]["layout"][player_data["position"][0]][player_data["position"][1]])):
        case variables.LADDER_DOWN:
            current_tile = "Down Ladder"
        
        case variables.LADDER_UP:
            current_tile = "Up Ladder"
        
        case _:
            pass
    for obj in map_data["maps"][variables.current_map]["nodes"].values():
        if list(obj["position"]) != list(player_data["position"]):
            continue
        current_tile = (obj["item"], obj["health"], obj["tier"])
        break
    print("\033c" + "\n".join(map_to_print) + "\n")
    if current_tile:
        if current_tile != "Down Ladder" and current_tile != "Up Ladder":
            print((f"{auto_format(f"Current Tile: {current_tile[0]} (HP: {current_tile[1]}) ", ("magenta", "bright", "black"))}{auto_format(f"(TIER {current_tile[2]})", (("magenta", "bright", "black") if current_tile[2] <= player_data["harvester_tier"] else ("red", "bright", "black")))}").ljust(MAP_LENGTH + 2))
            print(f"{auto_format((f"Hit Chance: {(round(1 / (3 * (current_tile[2] - player_data["harvester_tier"])), 2) if current_tile[2] > player_data["harvester_tier"] else 1):.2%}"), ("magenta", "bright", "black"))}".ljust(MAP_LENGTH + 2))
        
        else:
            if current_tile == "Down Ladder":
                print(auto_format("Press space to decend.".center(MAP_LENGTH + 2), ("magenta", "bright", "black")))
            
            else:
                print(auto_format("Press space to ascend.".center(MAP_LENGTH + 2), ("magenta", "bright", "black")))

def auto_format(text : str, format: tuple = ("white", "normal", "black")): 
    value_dict : dict = {
        "F.BLACK" : Fore.BLACK,
        "F.RED" : Fore.RED,
        "F.GREEN" : Fore.GREEN,
        "F.BLUE" : Fore.BLUE,
        "F.YELLOW" : Fore.YELLOW,
        "F.CYAN" : Fore.CYAN,
        "F.MAGENTA" : Fore.MAGENTA,
        "F.WHITE" : Fore.LIGHTWHITE_EX,
        "F.LIGHTBLACK" : Fore.LIGHTBLACK_EX,
        "F.LIGHTRED" : Fore.LIGHTRED_EX,
        "F.LIGHTGREEN" : Fore.LIGHTGREEN_EX,
        "F.LIGHTBLUE" : Fore.LIGHTBLUE_EX,
        "F.LIGHTYELLOW" : Fore.LIGHTYELLOW_EX,
        "F.LIGHTCYAN" : Fore.LIGHTCYAN_EX,
        "F.LIGHTMAGENTA" : Fore.LIGHTMAGENTA_EX,
        "F.LIGHTWHITE" : Fore.WHITE,
        "S.DIM" : Style.DIM,
        "S.NORMAL" : Style.NORMAL,
        "S.BRIGHT" : Style.BRIGHT,
        "B.BLACK" : Back.BLACK,
        "B.RED" : Back.RED,
        "B.GREEN" : Back.GREEN,
        "B.BLUE" : Back.BLUE,
        "B.YELLOW" : Back.YELLOW,
        "B.CYAN" : Back.CYAN,
        "B.MAGENTA" : Back.MAGENTA,
        "B.WHITE" : Back.LIGHTWHITE_EX,
        "B.LIGHTBLACK" : Back.LIGHTBLACK_EX,
        "B.LIGHTRED" : Back.LIGHTRED_EX,
        "B.LIGHTGREEN" : Back.LIGHTGREEN_EX,
        "B.LIGHTBLUE" : Back.LIGHTBLUE_EX,
        "B.LIGHTYELLOW" : Back.LIGHTYELLOW_EX,
        "B.LIGHTCYAN" : Back.LIGHTCYAN_EX,
        "B.LIGHTMAGENTA" : Back.LIGHTMAGENTA_EX
    }
    
    return (value_dict["F." + format[0].upper()] + value_dict["S." + format[1].upper()] + value_dict["B." + format[2].upper()] + text)

def raycast_line(map, origin : tuple, angle : float, max_distance : int, ignore_walls : bool = False):
    """
    [ASSISTED BY CHATGPT]
    """
    if max_distance <= 0: return None
    # Calculates the cosine and sine of the angle to get the amount that should be added to each coordinate.
    dx : float = math.cos(angle)
    dy : float = math.sin(angle) 
    point : tuple = origin # Initializes the point being viewed as the origin.
    hit_tiles : list = [] # Creating an empty list for the points hit.
    for _ in range(int(round(max_distance))): # Iterates until the loop is broken or the max distance is reached.
        tile_coords = tuple((int(round(point[0])), int(round(point[1])))) # Rounds the coordinates of the point being viewed and assigns it to a new variable.
        
        if not (0 <= tile_coords[0] < len(map) and 0 <= tile_coords[1] < len(map[0])): # Runs if the point being viewed is out of bounds.
            return hit_tiles
        
        if (not is_valid_move(map, tile_coords)) and (not ignore_walls): # Runs if the point being viewed is not a valid move and "ignore_walls" is false.
            hit_tiles.append(tile_coords) # Adds the coordinates of the hit tile to the list.
            return hit_tiles
        hit_tiles.append(tile_coords) # Adds the coordinates of the hit tile to the list.
        point = (point[0] + dx, point[1] + dy) # Gets the next point on the line by adding the "dx" and "dy" variables to the point coordinates.
    
    return hit_tiles

def raycast_circle(map, origin : tuple, radius : int, ignore_walls : bool = False):
    """
    [ASSISTED BY CHATGPT]
    """
    if radius <= 0: return None
    interval : int = max(int(math.sin(1 / radius) * 25), 1) # Calculates the angle interval between rays.
    hit_points : set = set() # Creating an empty set for the points being hit by a ray. Using a set is easier for no repetition.
    for angle in range(0, int(200 * 3.14159265), interval): # Iterates through a range of angles calculated from the interval and casts a ray in that direction.
        hit_points.update(raycast_line(map, origin, angle / 100, radius + 1, ignore_walls)) # Adds every unique point to the hit_points list.
    
    return list(hit_points) # Returns every point that was hit by at least one ray.

def random_event(event : dict, is_bad: bool = False, luck_affected: bool = True, add_None : bool = True):
    outcomes : list = [_ for _ in event.keys()]
    chances : list = [_ for _ in event.values()] # Creating new lists for the outcomes and chances in the given event.
    if is_bad: # Checks whether or not the current event is bad.
        effective_luck : int = int(round(player_data["luck"] / (player_data["luck"] + 35) if player_data["luck"] < 0 else player_data["luck"] / (player_data["luck"] - 35))) # Applies a diminishing return on higher luck values.
    
    else:
        effective_luck : int = int(round(player_data["luck"] * -1 / (player_data["luck"] + 35) if player_data["luck"] < 0 else player_data["luck"] * -1 / (player_data["luck"] - 35))) # Applies a diminishing return on higher luck values.
    if player_data["luck"] == 0 or not luck_affected: # Checks if the base probabilities should be calculated or not.
        adjusted_chances : dict = {outcomes[_] : chances[_] for _ in range(len(outcomes))} # Creates a new dictionary for the adjusted chances and assigns the base values to it.
    
    else:
        adjusted_chances : dict = {}
        for outcome in outcomes:
            adjusted_chances[outcome] = max(0.0, min(1.0, (event[outcome] * effective_luck))) # Adds the adjusted chance for each outcome to the adjusted chances dictionary.
    if None not in outcomes and add_None:
        outcomes.append(None) # Adds a None outcome to the dictionary.
        adjusted_chances.update({None : 1.0 - sum(chances)}) # Calculates the chance of no outcome happening and adds it to the chances dictionary.
    if len(adjusted_chances) == 2: # Checks if there are only two outcomes.
        culmulative_chances : dict = adjusted_chances
    
    else:
        culmulative_chances : dict = {}
        _ : float = 0.0
        for outcome in outcomes:
            _ += adjusted_chances[outcome]
            culmulative_chances[outcome] = _
    random_num : float = random.uniform(0, 1)
    for outcome in outcomes:
        if random_num < culmulative_chances[outcome]: # Runs if the random number is less than culmulative chance for the current outcome 
            
            return outcome # Returns the current outcome in the iteration.

def create_room(map, room : Room):
    for x in range(room.x1, room.x2):
        for y in range(room.y1, room.y2):
            map[x][y] = EMPTY

def create_corridor(map, start : int, end : int, location : int, axis : str):
    for i in range(min(start, end), max(start, end) + 1): # Iterates through a range of values between the start and end points.
        match axis.lower():
            case "v":
                map[location][i] = EMPTY
            
            case "h":
                map[i][location] = EMPTY
            
            case _:
                raise ValueError(f"Axis must be either h or v, got {axis}") # Raises an error if the axis is neither horizontal or vertical.

def create_map(start_point : tuple = (1, 1)):
    map = [[BORDER for _ in range(MAP_LENGTH)] for _ in range(MAP_HEIGHT)] # Initializes the map with every coordinate having a "#."
    rooms = []
    num_rooms = min(15, max(3, int(round(player_data["depth"] / 20))))
    min_room_size, max_room_size = max(4, int(round(15 / num_rooms))), max(6, int(round(20 / num_rooms)))
    while len(rooms) < num_rooms: # Runs while there are less than 11 rooms generated.
        if not rooms: # Creates a 3x3 room around the starting point if no rooms have been generated.
            width = 3
            height = 3
            x, y = start_point[0] - 1, start_point[1] - 1
            new_room = Room(x, y, width, height)
            create_room(map, new_room)
        
        else: # Creates a randomly sized room if there is at least one room generated.
            width = random.randint(min_room_size, max_room_size)
            height = random.randint(min_room_size, max_room_size)
            x = random.randint(0, MAP_HEIGHT - width - 1)
            y = random.randint(0, MAP_LENGTH - height - 1)
            new_room = Room(x, y, width, height)
            if any([new_room.is_intersecting(_) for _ in rooms]): # Skips the generation of the current room if it intersects any currently generated rooms.
                continue
            create_room(map, new_room)
            if rooms: # Creates a corridor between the current room and the previous one if there has been one room generated.
                previous_room_center = rooms[-1].center
                new_room_center = new_room.center
                if random.randint(0, 1): # Randomly chooses the orientation of the corridor.
                    create_corridor(map, previous_room_center[0], new_room_center[0], previous_room_center[1], "h")
                    create_corridor(map, previous_room_center[1], new_room_center[1], new_room_center[0], "v")
                else:
                    create_corridor(map, previous_room_center[1], new_room_center[1], previous_room_center[0], "v")
                    create_corridor(map, previous_room_center[0], new_room_center[0], new_room_center[1], "h")
        rooms.append(new_room) # Adds the current room object to the rooms list.
    for x in range(4):
        points_to_remove = []
        for i in range(MAP_HEIGHT):
            for j in range(MAP_LENGTH):
                if len(get_valid_neighbors(map, (i, j))) >= 2:
                    points_to_remove.append((i, j))
        for _ in points_to_remove:
            map[_[0]][_[1]] = EMPTY
    end_point = rooms[-1].center
    map[end_point[0]][end_point[1]] = LADDER_DOWN # Places a "LADDER_DOWN" tile at the center of the last room generated.
    if len(map_data["maps"]) > 0:
        map[start_point[0]][start_point[1]] = LADDER_UP # Places a "LADDER_UP" tile at the center of the first room generated if there is another map.
    spawned_objects = {}
    for _ in range(max(2, int(2 * (player_data["luck"] / 20)))):
        spawned_objects.update(spawn_resource_nodes(map, start_point, "O", (max(1, player_data["depth"] / 2.5) * max(1, player_data["luck"] / 2.5)), 10, 5, 15))
        spawned_objects.update(spawn_resource_nodes(map, start_point, "G", (max(1, player_data["depth"] / 2.5) * max(1, player_data["luck"] / 2.5)), 10, 5, 15))
        spawned_objects.update(spawn_resource_nodes(map, start_point, "P", (max(1, player_data["depth"] / 2.5) * max(1, player_data["luck"] / 2.5)), 10, 5, 15))
    map_data["maps"].update({f"Map_{len(map_data["maps"]) + 1}" : (Map_Layout(map, [_.to_dict() for _ in rooms], start_point, end_point, spawned_objects)).to_dict()}) # Creates a new Map_Layout object, converts it into a dictionary, and adds it to data. 
    save_data()

def adjust_probabilities(outcomes : dict, factor : int):
    adjusted_chances = {}
    for outcome, (base_chance, reference_value) in outcomes.items():
        if factor <= reference_value:
            scale = 0.01
        
        elif factor >= reference_value * 2:
            scale = 2
        
        else:
            scale = (factor - reference_value) - 1
        adjusted_chances[outcome] = base_chance * scale
    total = sum(adjusted_chances.values()) if sum(adjusted_chances.values()) else sum([_[0] for _ in outcomes.values()])
    if not sum(adjusted_chances.values()):
        return {ore: base_prob for ore, (base_prob, _) in outcomes.items()}
    return {ore: prob / total for ore, prob in adjusted_chances.items()}

def spawn_resource_nodes(map, invalid_points : list, resource_type : str, richness : int | float, max_cluster_size : int, minimum: int, maximum: int):
    match resource_type:
        case "O":
            data_accessed = ORE_DATA
        
        case "G":
            data_accessed = GEM_DATA
        
        case "P":
            data_accessed = PLANT_DATA
        
        case _:
            raise ValueError("Resource type must be either O, G, or P.")
    type_chances = adjust_probabilities(data_accessed["Generation Data"], player_data["depth"])
    if any([minimum > maximum, minimum < 0, maximum < 0]):
        raise ValueError(f"minimum property must be a non-zero positive integer and maximum property must be a non-zero positive integer greater than or equal to minimum parameter.")
    clusters_to_spawn = random.randint(minimum, maximum)
    nodes_spawned = {}
    possible_origins = []
    for i in range(MAP_HEIGHT):
        for j in range(MAP_LENGTH):
            if get_tile(map, (i, j)) != EMPTY:
                continue
            possible_origins.append((i, j))
    for _ in range(clusters_to_spawn):
        cluster_origin = random.choice(possible_origins)
        cluster_size = random.randint(3, 3 * max_cluster_size)
        type_spawned = random_event(type_chances, add_None = False)
        while not type_spawned:
            type_spawned = random_event(type_chances, add_None = False)
        nodes_in_cluster = {}
        possible_tiles = [_ for _ in raycast_circle(map, cluster_origin, 2, True) if ((get_tile(map, _) == EMPTY) and (_ not in invalid_points))]
        for j in range(cluster_size):
            if len(possible_tiles) == 0:
                break
            node_pos = possible_tiles.pop(random.randint(0, len(possible_tiles) - 1))
            node_amount = data_accessed["Other Data"][type_spawned][1] + int(round(random.uniform(0.5, 0.75) * richness * (data_accessed["Other Data"][type_spawned][1])))
            node_tier = data_accessed["Other Data"][type_spawned][2]
            node_health = int(round((node_amount / 3) * round(node_tier * 1.25) * data_accessed["Other Data"][type_spawned][0]))
            nodes_in_cluster.update({f"{type_spawned}_{len([_ for _ in nodes_spawned.keys() if f"{type_spawned}" in _])}" : (Resource_Node(len(nodes_spawned) + 1, type_spawned, node_tier, node_amount, node_pos, node_health)).to_dict()})
        nodes_spawned.update(nodes_in_cluster)
    return nodes_spawned

def get_layout_property(layout_id : int, property : str):
    if property not in ["layout", "rooms", "entrance", "exit"]:
        raise ValueError(f"property parameter must be either layout, rooms, entrance, or exit; got {property}")
    else:
        return map_data["maps"][f"Map_{layout_id}"][property]

def apply_tier_penalty(damage : int, tier_req: int):
    if player_data["harvester_tier"] < tier_req:
        repel_chance = 1 - 1 / (3 * (tier_req - player_data["harvester_tier"]))
        if ((random_event({"repel" : repel_chance, None : 1 - repel_chance}, False, False, False) == "repel") and (not random_event({True : 1/3 * player_data["skills"]["Surefire"], False : 1 - (1/3 * player_data["skills"]["Surefire"])}, add_None = False, luck_affected = False)) or variables.debug_toggles["omniscience"]):
            return "Deflected"
        
        else:
            return damage * (0.6 * (1 / (tier_req - player_data["harvester_tier"])))
    
    else:
        return damage

def BFS(map, start : tuple, goal : str, iteration : int = 0, PID : tuple = (None, None)):
    """
    Performs a Breadth-first search and returns the number of iterations needed to reach the goal.
    \n(I"m not sure if I"ll even use this.)
    """
    if not iteration:
        queue = [start]
        visited = []
    
    else:
        queue, visited = PID
    iteration += 1
    pending_queue = []
    while queue:
        current_pos = queue.pop(0)
        if map[current_pos[0]][current_pos[1]] == goal:
            return iteration
        pending_queue.extend([_ for _ in get_valid_neighbors(current_pos) if _ not in visited])
    BFS(map, start, goal, iteration, (pending_queue, visited))

def damage_node(node_pos):
    damage_dealt = 0
    targetted_node = [_ for _ in [_ for _ in map_data["maps"][variables.current_map]["nodes"]] if tuple(map_data["maps"][variables.current_map]["nodes"][_]["position"]) == node_pos]
    if not targetted_node:
        return 0, (0, 0)
    
    else:
        targetted_node : dict = targetted_node[0]
        if variables.debug_toggles["omniscience"]:
            damage_dealt = random.randint(3,6) * (0.9 * player_data["harvester_tier"]) * (1 + (SKILLS["Hard Hitting"] * 0.5) + (player_data["skills"]["Mastery"] * 0.25)) * (0.9 * player_data["harvester_tier"])
        
        else:
            damage_dealt = random.randint(3,6) * (0.9 * player_data["harvester_tier"]) * (1 + (player_data["skills"]["Hard Hitting"] * 0.5) + (player_data["skills"]["Mastery"] * 0.25)) 
        if not variables.debug_toggles["instant_break"]:
            damage_dealt = apply_tier_penalty(damage_dealt, map_data["maps"][variables.current_map]["nodes"][targetted_node]["tier"])
        if damage_dealt == "Deflected":
            return "Deflected", (0, 0)
        
        else:
            damage_dealt = int(damage_dealt)
        if variables.debug_toggles["instant_break"]:
            map_data["maps"][variables.current_map]["nodes"][targetted_node]["health"] = 0
            damage_dealt = "∞"
        
        else:
            map_data["maps"][variables.current_map]["nodes"][targetted_node]["health"] -= damage_dealt
        if map_data["maps"][variables.current_map]["nodes"][targetted_node]["health"] <= 0:
            experience_factor : dict = {
                # Ores
                "Stone" : 1,
                "Raw Copper" : 2,
                "Raw Iron" : 3,
                "Raw Silver" : 5,
                "Raw Gold" : 7,
                "Raw Platinum" : 10,
                "Raw Bismuth" : 15,
                "Raw Titanium" : 20,
                "Raw Abyssite" : 30,
                # Gems
                "Amethyst" : 1,
                "Topaz" : 2,
                "Sapphire" : 3,
                "Emerald" : 4,
                "Ruby" : 5,
                "Diamond" : 6,
                "Painite" : 8,
                "Onyx" : 10,
                "Tourmaline" : 15,
                "Kyanite" : 20,
                "Vantalite" : 30,
                # Plants
                "Grass" : 1,
                "Small Roots" : 3,
                "Large Roots" : 5,
                "Deep Algae" : 10,
                "Luminous Moss" : 15,
                "Dark Fungus" : 30
            }
            R = collect_resources(targetted_node)
            X = gain_xp(experience_factor[map_data["maps"][variables.current_map]["nodes"][targetted_node]["item"]] * int(0.5 * map_data["maps"][variables.current_map]["nodes"][targetted_node]["amount"]))
            map_data["maps"][variables.current_map]["nodes"].pop(targetted_node)
            
            return damage_dealt, (R, X)
        
        return damage_dealt, (0, 0)

def gain_xp(experience):
    if variables.debug_toggles["omniscience"]:
        experience *= 1 + (SKILLS["Quick Learner"] * 0.2) * 1 + (player_data["skills"]["Mastery"] * 0.1)
    
    else:
        experience *= 1 + (player_data["skills"]["Quick Learner"] * 0.2) * 1 + (player_data["skills"]["Mastery"] * 0.1)
    player_data["experience"] += int(experience)
    if player_data["experience"] >= (((2 * XP_SCALING_FACTOR) * (player_data["level"] ^ 2)) + (XP_SCALING_FACTOR * player_data["level"]) + 100):
        player_data["experience"] -= (((2 * XP_SCALING_FACTOR) * (player_data["level"] ^ 2)) + (XP_SCALING_FACTOR * player_data["level"]) + 100)
        player_data["level"] += 1
        player_data["skill_points"] += 1
    save_data()
    
    return int(experience)

def darkness_creep():
    if variables.debug_toggles["omniscience"]:
        darkness_modifier = 0 - SKILLS["Darkvision"] - int(round(player_data["skills"]["Mastery"] / 2))
    
    else:
        darkness_modifier = 0 - player_data["skills"]["Darkvision"] - int(round(player_data["skills"]["Mastery"] / 2))
    darkness_modifier += ((player_data["depth"] - (player_data["depth"] % 50)) / 50)
    
    return int(darkness_modifier)

def collect_resources(node):
    node_resource = map_data["maps"][variables.current_map]["nodes"][node]["item"]
    node_amount = map_data["maps"][variables.current_map]["nodes"][node]["amount"]
    if variables.debug_toggles["omniscience"]:
        resources_gained = int(round(node_amount * (1 + SKILLS["Fortunate"] * 0.5) * (1 + player_data["skills"]["Mastery"] * 0.15))) + random_event({-1 : 1/3, 0 : 1.3, 1 : 1/3})
    
    else:
        resources_gained = int(round(node_amount * (1 + player_data["skills"]["Fortunate"] * 0.5) * (1 + player_data["skills"]["Mastery"] * 0.15))) + random_event({-1 : 1/3, 0 : 1.3, 1 : 1/3})
    if node_resource not in player_data["inventory"]["raw_materials"]:
        player_data["inventory"]["raw_materials"].update({node_resource : resources_gained})
    
    else:
        player_data["inventory"]["raw_materials"][node_resource] += resources_gained
    player_data["inventory"]["raw_materials"] = dict(sorted(player_data["inventory"]["raw_materials"].items()))
    save_data()
    
    return str(node_resource), int(resources_gained)