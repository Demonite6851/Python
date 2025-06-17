"""
Main Program for The Chasm
"""

# 1,697 lines of code

import colorama, json # Importing libraries/files
from functions import * # Getting everything from 'functions.py'
from variables import * # Getting everything from 'variables.py'
colorama.init(autoreset = True)

if not map_data["maps"]:
    create_map()
variables.current_map = list(map_data["maps"].keys())[0]
if not is_valid_move(map_data["maps"][variables.current_map]["layout"], player_data["position"]):
    player_data["position"] = tuple(map_data["maps"][variables.current_map]["entrance"])

pressed_key : str = None
actions_done = []
reset_page : bool = False
page : str = None

while True: # Runs continuously until the program is stopped.
    match current_screen.lower():
        case "title": # DONE
            print("\033c"+"\n".join([f"{auto_format(_.center(len(_) + 6), ("lightmagenta", "bright", "black"))}" for _ in program_banner]))
            print(auto_format("Press Space to continue, press Escape to close.".center(len(program_banner[0]) + 6), ("lightmagenta", "bright", "black")))
            if wait_for_keys("space", "esc") == "space":
                current_screen = "map"
            
            else:
                print(auto_format(("\033c"+"Are you sure you want to close the program?"), ("lightmagenta", "bright", "black")))
                if wait_for_keys("space", "esc") == "space":
                    print(auto_format(("\033c"+"Closing Program..."), ("lightmagenta", "bright", "black")))
                    save_data()
                    exit()
        
        case "pause": # DONE
            screen_to_print : list = []
            screen_to_print.extend([f"{auto_format(_.center(len(_) + 6), ("lightmagenta", "bright", "black"))}" for _ in menu_banner])
            screen_to_print.extend([f"{auto_format((" " + _).ljust(len(menu_banner[0]) + 6), ("lightmagenta", "bright", "black"))}" for _ in [_ if _ != selected_option else f"> {_}" for _ in current_menu_options]])
            print("\033c"+"\n".join(screen_to_print))
            pressed_key = wait_for_keys("w", "s", "esc", "space") # Waiting for specific keys.
            match pressed_key:
                case "w": # 'w' selects the previous option.
                    selected_option = current_menu_options[current_menu_options.index(selected_option) - 1]
                
                case "s": # 's' selects the next option.
                    selected_option = current_menu_options[current_menu_options.index(selected_option) + 1] if current_menu_options.index(selected_option) < len(current_menu_options) - 1 else current_menu_options[0]
                
                case "esc": # 'esc' returns you to the map screen.
                    current_screen = "map"
                
                case "space": # 'space' sends you to the selected menu.
                    match selected_option.lower():
                        case "back to title":
                            current_screen = "title"
                        
                        case "skills":
                            difference_detected = False
                            for _ in player_data["skills"]:
                                if player_data["skills"][_] != SKILLS[_]:
                                    difference_detected = True
                                    break
                            if difference_detected and not variables.debug_toggles["omniscience"]:
                                current_menu_options = [_ for _ in player_data["skills"] if _ != "Mastery"]
                            else:
                                current_menu_options = [_ for _ in player_data["skills"]]
                            selected_option = current_menu_options[0]
                            current_screen = "skills"
                        
                        case "stats":
                            current_screen = "stats"
                        
                        case "inventory":
                            if not player_data["inventory"]["raw_materials"] and not player_data["inventory"]["crafted_items"]:
                                continue
                            else:
                                if player_data["inventory"]["raw_materials"]:
                                    page = "R"
                                else:
                                    page = "C"
                            reset_page = True
                            current_screen = "inventory"
                        
                        case "crafting":
                            reset_page = True
                            current_screen = "crafting"
                            
        case "inventory": # DONE
            screen_to_print : list = []
            if reset_page:
                reset_page = False
                match page:
                    case "R":
                        current_menu_options = [(_[0], _[1]) for _ in player_data["inventory"]["raw_materials"].items()]
                        selected_option = current_menu_options[0]
                    
                    case "C":
                        current_menu_options = [(_[0], _[1]) for _ in player_data["inventory"]["crafted_items"].items()]
                        selected_option = current_menu_options[0]
            screen_to_print.extend([f"{auto_format(_.center(len(_) + 6), ("lightmagenta", "bright", "black"))}" for _ in inventory_banner])
            screen_to_print.append(f"{auto_format((" CRAFTED ITEMS " if page == "C" else " RAW MATERIALS ").center(len(inventory_banner[0]) + 6, "="), ("lightmagenta", "bright", "black"))}")
            items_display = [f"{("     " if _ != selected_option else "   > ")}{_[0]}:{" " * (15 - len(_[0]))}x{_[1]}" for _ in current_menu_options]
            screen_to_print.extend([f"{auto_format(_.ljust(len(inventory_banner[0]) + 6), ("lightmagenta", "bright", "black"))}" for _ in items_display])
            screen_to_print.append("=".center(len(inventory_banner[0]) + 6, "="))
            print("\033c" + "\n".join(screen_to_print))
            pressed_key = wait_for_keys("w", "s", "space", "esc", "tab")
            match pressed_key:
                case "w": # 'w' selects the previous option.
                    selected_option = current_menu_options[current_menu_options.index(selected_option) - 1]
                
                case "s": # 's' selects the next option.
                    selected_option = current_menu_options[current_menu_options.index(selected_option) + 1] if current_menu_options.index(selected_option) < len(current_menu_options) - 1 else current_menu_options[0]
                
                case "space": # 'space' gives you the details of the selected item.
                    screen_to_print = [f"{auto_format(_.center(len(_) + 6), ("lightmagenta", "bright", "black"))}" for _ in inventory_banner]
                    screen_to_print.append(auto_format(f" {selected_option[0]}".ljust(len(inventory_banner[0]) + 6), ("lightmagenta", "bright", "black")))
                    screen_to_print.append(auto_format(f"     {DESCRIPTIONS[selected_option[0]]}".ljust(len(inventory_banner[0]) + 6), ("lightmagenta", "bright", "black")))
                    print("\033c" + "\n".join(screen_to_print))
                    wait_for_keys("space")
                
                case "esc": # 'esc' sends you to the pause menu.
                    page = None
                    current_screen = "pause"
                    current_menu_options = ["Back to Title", "Inventory", "Crafting", "Skills", "Stats"]
                    selected_option = current_menu_options[0]
                
                case "tab":
                    if page == "R":
                        if player_data["inventory"]["crafted_items"]:
                            page = "C"
                            reset_page = True
                    
                    else:
                        if player_data["inventory"]["raw_materials"]:
                            page = "R"
                            reset_page = True
        case "crafting": # DONE
            if reset_page:
                reset_page = False
                if player_data["harvester_tier"] < 15:
                    current_menu_options = [list(HARVESTER_REQUIREMENTS.keys())[player_data["harvester_tier"] - 1]]
                
                else:
                    current_menu_options = []
                current_menu_options.extend(RECIPES.keys())
                selected_option = current_menu_options[0]
                actions_done = []
            screen_to_print : list = []
            screen_to_print.extend([f"{auto_format(_.center(len(_) + 6), ("lightmagenta", "bright", "black"))}" for _ in crafting_banner])
            upper_bound, lower_bound = len(current_menu_options) - 3, 3
            if current_menu_options.index(selected_option) >= upper_bound:
                items_to_display = list(range(len(current_menu_options) - 8, len(current_menu_options)))
            
            elif current_menu_options.index(selected_option) <= lower_bound:
                items_to_display = list(range(0, 8))
            
            else:
                items_to_display = [(current_menu_options.index(selected_option) + _) for _ in range(-4, 4)]
            screen_to_print.append(f"{auto_format("‾".center(len(crafting_banner[0]) + 6, "‾"), ("lightmagenta", "bright", "black"))}")
            for _ in items_to_display:
                if current_menu_options[_] not in list(RECIPES.keys()):
                    screen_to_print.append(f"{auto_format((("    > " + current_menu_options[_].replace("_", " ")) if current_menu_options[_] == selected_option else ("      " + current_menu_options[_].replace("_", " "))).ljust(len(crafting_banner[0]) + 6), (("lightgreen", "bright", "black") if HARVESTER_REQUIREMENTS[current_menu_options[_]].can_craft(player_data) else ("lightred", "bright", "black")))}")
                
                else:
                    screen_to_print.append(f"{auto_format((("    > " + current_menu_options[_].replace("_", " ") + (("  (" + str(RECIPES[current_menu_options[_]].calc_max_amount(player_data)) + ")") if RECIPES[current_menu_options[_]].calc_max_amount(player_data) else "")) if current_menu_options[_] == selected_option else ("      " + current_menu_options[_].replace("_", " ") + (("  (" + str(RECIPES[current_menu_options[_]].calc_max_amount(player_data)) + ")") if RECIPES[current_menu_options[_]].calc_max_amount(player_data) else ""))).ljust(len(crafting_banner[0]) + 6), (("lightgreen", "bright", "black") if RECIPES[current_menu_options[_]].can_craft(player_data) else ("lightred", "bright", "black")))}")
            screen_to_print.append(f"{auto_format("_".center(len(crafting_banner[0]) + 6, "_"), ("lightmagenta", "bright", "black"))}")
            if actions_done:
                if actions_done == ["Can't Craft"]:
                    screen_to_print.append(f"{auto_format(f"You can't craft that.".ljust(len(crafting_banner[0]) + 6), ("lightred", "bright", "black"))}")
                
                else:
                    if actions_done[0].replace("_", " ") not in player_data["inventory"]["crafted_items"]:
                        screen_to_print.append(f"{auto_format(f"Crafted {actions_done[0].replace("_", " ")}".ljust(len(crafting_banner[0]) + 6), ("lightmagenta", "bright", "black"))}")
                    
                    else:
                        screen_to_print.append(f"{auto_format(f"Crafted {actions_done[0].replace("_", " ")}".ljust(len(crafting_banner[0]) + 6), ("lightmagenta", "bright", "black"))}")
                        screen_to_print.append(f"{auto_format(f"You now have {player_data["inventory"]["crafted_items"][actions_done[0].replace("_", " ")]} {actions_done[0].replace("_", " ")}(s)".ljust(len(crafting_banner[0]) + 6), ("lightmagenta", "bright", "black"))}")
            screen_to_print.append(auto_format(f"  MATERIALS NEEDED:".ljust(len(crafting_banner[0]) + 6), ("lightmagenta", "bright", "black")))
            for material, amount in (HARVESTER_REQUIREMENTS[selected_option] if selected_option not in list(RECIPES.keys()) else RECIPES[selected_option]).materials.items():
                if material in player_data["inventory"]["raw_materials"]:
                    amount_held = player_data["inventory"]["raw_materials"][material]
                
                elif material in player_data["inventory"]["crafted_items"]:
                    amount_held = player_data["inventory"]["crafted_items"][material]
                
                else:
                    amount_held = 0
                screen_to_print.append(f"{auto_format(f"    ● {material} x{amount}{" " * (30 - len(f"    ● {material} x{amount}"))}({amount_held})".ljust(len(crafting_banner[0]) + 6), ("magenta", "bright", "black"))}")
            
            for _ in range(25 - len(screen_to_print)):
                screen_to_print.append(auto_format("".ljust(len(crafting_banner[0]) + 6), ("white", "bright", "black")))
            actions_done = []
            print("\033c" + "\n".join(screen_to_print))
            pressed_key = wait_for_keys("w", "s", "esc", "space")
            match pressed_key:
                case "w":
                    selected_option = current_menu_options[current_menu_options.index(selected_option) - 1]
                
                case "s":
                    selected_option = current_menu_options[current_menu_options.index(selected_option) + 1] if current_menu_options.index(selected_option) < len(current_menu_options) - 1 else current_menu_options[0]
                
                case "esc":
                    current_screen = "pause"
                    current_menu_options = ["Back to Title", "Inventory", "Crafting", "Skills", "Stats"]
                    selected_option = current_menu_options[0]
                
                case "space":
                    if selected_option not in list(RECIPES.keys()):
                        if HARVESTER_REQUIREMENTS[selected_option].can_craft(player_data):
                            HARVESTER_REQUIREMENTS[selected_option].craft_item(player_data)
                            player_data["harvester_tier"] += 1
                            actions_done = [selected_option]
                            reset_page = True
                            save_data()
                        
                        else:
                            actions_done = ["Can't Craft"]
                    else:
                        if RECIPES[selected_option].can_craft(player_data):
                            RECIPES[selected_option].craft_item(player_data)
                            actions_done = [selected_option]
                            save_data()
                        
                        else:
                            actions_done = ["Can't Craft"]
        case "skills": # DONE
            screen_to_print : list = []
            screen_to_print.extend([f"{auto_format(_.center(len(_) + 6), ("lightmagenta", "bright", "black"))}" for _ in skills_banner])
            print("\033c" + "\n".join(screen_to_print))
            screen_to_print = []
            for skill in SKILLS:
                if skill != "Mastery":
                    
                    if variables.debug_toggles["omniscience"]:
                        screen_to_print.append(auto_format(((f"  {skill}" if selected_option != skill else f"> {skill}") + f":{" " * (15 - len(skill))}{"● " * SKILLS[skill]}").ljust(len(skills_banner[0]) + 6), ("lightmagenta", "bright", "black")))
                    
                    else:
                        screen_to_print.append(auto_format(((f"  {skill}" if selected_option != skill else f"> {skill}") + f":{" " * (15 - len(skill))}{"● " * player_data["skills"][skill]}{"○ " * (SKILLS[skill] - player_data["skills"][skill])}").ljust(len(skills_banner[0]) + 6), ("lightmagenta", "bright", "black")))
                else:
                    difference_detected = False
                    for _ in player_data["skills"]:
                        if player_data["skills"][_] != SKILLS[_]:
                            difference_detected = True
                    
                    if difference_detected and not variables.debug_toggles["omniscience"]:
                        screen_to_print.append(auto_format(" ???".ljust(len(skills_banner[0]) + 6), ("magenta", "dim", "black")))
                    
                    else:
                        screen_to_print.append(auto_format((("  Mastery" if selected_option != skill else f"> Mastery") + f":     {player_data["skills"]["Mastery"]}").ljust(len(skills_banner[0]) + 6), ("lightmagenta", "bright", "black")))
            print("\n".join(screen_to_print))
            pressed_key = wait_for_keys("w", "s", "shift", "esc", "space") # Waiting for specific keys.
            match pressed_key:
                case "w": # 'w' selects the previous option.
                    selected_option = current_menu_options[current_menu_options.index(selected_option) - 1]
                
                case "s": # 's' selects the next option.
                    selected_option = current_menu_options[current_menu_options.index(selected_option) + 1] if current_menu_options.index(selected_option) < len(current_menu_options) - 1 else current_menu_options[0]
                
                case "shift": # 'shift' gives you info on the selected skill.
                    screen_to_print = []
                    screen_to_print.extend([f"{auto_format(_.center(len(_) + 6), ("lightmagenta", "bright", "black"))}" for _ in skills_banner])
                    screen_to_print.append(auto_format(f" {selected_option}".ljust(len(skills_banner[0]) + 6), ("lightmagenta", "bright", "black")))
                    screen_to_print.append(auto_format(f" {SKILL_DESCRIPTIONS[selected_option]}".ljust(len(skills_banner[0]) + 6), ("lightmagenta", "bright", "black")))
                    print("\033c" + "\n".join(screen_to_print) + auto_format(f"{"\n (Press 'esc' to go back.)"}".ljust(len(skills_banner[0]) + 6), ("lightmagenta", "bright", "black")))
                    wait_for_keys("esc")
                
                case "esc": # 'esc' sends you back to the pause menu.
                    current_screen = "pause"
                    current_menu_options = ["Back to Title", "Inventory", "Crafting", "Skills", "Stats"]
                    selected_option = current_menu_options[0]
                
                case "space": # 'space' upgrades the skill if you have at least one skill point.
                    if player_data["skill_points"] and player_data["skills"][selected_option] < SKILLS[selected_option]:
                        player_data["skill_points"] -= 1
                        player_data["skills"][selected_option] += 1
                        save_data()
        case "stats": # DONE
            screen_to_print : list = []
            screen_to_print.extend([f"{auto_format(_.center(len(_) + 6), ("lightmagenta", "bright", "black"))}" for _ in stats_banner])
            xp_to_lvlup = ((2 * XP_SCALING_FACTOR) * (player_data["level"] ^ 2)) + (XP_SCALING_FACTOR * player_data["level"]) + 100
            experience_percent = round(player_data["experience"] / xp_to_lvlup, 2)
            screen_to_print.append(auto_format(f"{" Level: " + str(player_data["level"])}".ljust(len(stats_banner[0]) + 6), ("lightmagenta", "bright", "black")))
            screen_to_print.append(auto_format(f"{" XP: ▌" + ("█" * int(experience_percent * 10)) + ("░" * (10 - int(experience_percent * 10))) + "▐"} ({experience_percent:.0%})".ljust(len(stats_banner[0]) + 6), ("lightmagenta", "bright", "black")))
            screen_to_print.append(auto_format(f"{" Luck: " + str(player_data["luck"])}".ljust(len(stats_banner[0]) + 6), ("lightmagenta", "bright", "black")))
            print("\033c" + "\n".join(screen_to_print) + auto_format(f"{"\n (Press 'esc' to go back.)"}".ljust(len(stats_banner[0]) + 7), ("lightmagenta", "bright", "black")))
            wait_for_keys("esc")
            current_screen = "pause"
            current_menu_options = ["Back to Title", "Inventory", "Crafting", "Skills", "Stats"]
            selected_option = current_menu_options[0]
        case "map": # DONE
            display_map()
            screen_to_print = []
            if actions_done != [True]:
                for action in actions_done:
                    match action[0]:
                        case "Damage":
                            if type(action[1]) == int or action[1] == "∞":
                                screen_to_print.append(f"{auto_format(f" Dealt {action[1]} damage.".ljust(MAP_LENGTH + 2), ("magenta", "bright", "black"))}")
                                if action[2][0] != 0:
                                    screen_to_print.append(f"{auto_format(f" Gained x{action[2][0][1]} {action[2][0][0]}.".ljust(MAP_LENGTH + 2), ("magenta", "bright", "black"))}")
                                    screen_to_print.append(f"{auto_format(f" Gained {action[2][1]} XP.".ljust(MAP_LENGTH + 2), ("magenta", "bright", "black"))}")
                            
                            else:
                                screen_to_print.append(f"{auto_format(f" Dealt 0 damage. (DEFLECTED)".ljust(MAP_LENGTH + 2), ("magenta", "bright", "black"))}")
                        
                        case "Level Up":
                            screen_to_print.append(f"{auto_format(f" LEVEL UP! You are now level {player_data["level"]}".ljust(MAP_LENGTH + 2), ("magenta", "bright", "black"))}")
                            screen_to_print.append(f"{auto_format(f" You have {player_data["skill_points"]} unspent skill points".ljust(MAP_LENGTH + 2), ("magenta", "bright", "black"))}")
                        
                        case "Toggle":
                            screen_to_print.append(f"{auto_format(f" {action[1].upper()}: {variables.debug_toggles[action[1].replace(" ", "_")]}".ljust(MAP_LENGTH + 2), ("magenta", "bright", "black"))}")
                        
                        case _:
                            pass
            print("\n".join(screen_to_print))
            time.sleep(0)
            actions_done = []
            while not actions_done:
                pressed_key = wait_for_keys("w", "a", "s", "d", "esc", "l", "o", "p", "=", "m", "space") # Waiting for specific keys.
                match pressed_key:
                    
                    case "w": # 'w' moves you up.
                        new_pos : tuple = (player_data["position"][0] - 1, player_data["position"][1])
                        if is_valid_move(map_data["maps"][variables.current_map]["layout"], new_pos):
                            player_data["position"] = new_pos
                            actions_done = [True]
                    
                    case "a": # 'a' moves you left.
                        new_pos : tuple = (player_data["position"][0], player_data["position"][1] - 1)
                        if is_valid_move(map_data["maps"][variables.current_map]["layout"], new_pos):
                            player_data["position"] = new_pos
                            actions_done = [True]
                    
                    case "s": # 's' moves you down.
                        new_pos : tuple = (player_data["position"][0] + 1, player_data["position"][1])
                        if is_valid_move(map_data["maps"][variables.current_map]["layout"], new_pos):
                            player_data["position"] = new_pos
                            actions_done = [True]
                    
                    case "d": # 'd' moves you right.
                        new_pos : tuple = (player_data["position"][0], player_data["position"][1] + 1)
                        if is_valid_move(map_data["maps"][variables.current_map]["layout"], new_pos):
                            player_data["position"] = new_pos
                            actions_done = [True]
                    
                    case "space": # 'space' interacts with the tile you're standing on.
                        match get_tile(map_data["maps"][variables.current_map]["layout"], player_data["position"]):
                            
                            case variables.LADDER_DOWN:
                                if player_data["depth"] == len(map_data["maps"]):
                                    create_map(player_data["position"])
                                player_data["depth"] += 1
                                variables.current_map = f"Map_{min(len(map_data["maps"]), player_data["depth"])}"
                                actions_done = [True]
                            
                            case variables.LADDER_UP:
                                if player_data["depth"] > 1:
                                    player_data["depth"] -= 1
                                    variables.current_map = f"Map_{min(len(map_data["maps"]), player_data["depth"])}"
                                    if not map_data["maps"][variables.current_map]["nodes"]:
                                        spawned_objects : dict = {}
                                        for _ in range(max(2, int(2 * (player_data["luck"] / 20)))):
                                            spawned_objects.update(spawn_resource_nodes(map, [tuple(map_data["maps"][variables.current_map]["entrance"]), tuple(map_data["maps"][variables.current_map]["exit"])], "O", (max(1, player_data["depth"] / 2.5) * max(1, player_data["luck"] / 25)), 10, 5, 15))
                                            spawned_objects.update(spawn_resource_nodes(map, [tuple(map_data["maps"][variables.current_map]["entrance"]), tuple(map_data["maps"][variables.current_map]["exit"])], "G", (max(1, player_data["depth"] / 2.5) * max(1, player_data["luck"] / 25)), 10, 5, 15))
                                            spawned_objects.update(spawn_resource_nodes(map, [tuple(map_data["maps"][variables.current_map]["entrance"]), tuple(map_data["maps"][variables.current_map]["exit"])], "P", (max(1, player_data["depth"] / 2.5) * max(1, player_data["luck"] / 25)), 10, 5, 15))
                                        map_data["maps"][variables.current_map]["nodes"]
                                    actions_done = [True]
                            
                            case _:
                                level = player_data["level"]
                                damage, spoils = damage_node(tuple(player_data["position"]))
                                if damage != 0:
                                    if level != player_data["level"]:
                                        actions_done = [("Damage", damage, spoils), ("Level Up")]
                                    else:
                                        actions_done = [("Damage", damage, spoils)]
                                else:
                                    actions_done = [True]
                    
                    case "l": # 'l' toggles True Sight (See everywhere, even behind walls) [DEBUG]
                        variables.debug_toggles["true_sight"] = not variables.debug_toggles["true_sight"]
                        actions_done = [("Toggle", "true sight")]
                    
                    case "o": # 'o' toggles Omniscience (Gives the max effect of skills.) [DEBUG]
                        variables.debug_toggles["omniscience"] = not variables.debug_toggles["omniscience"]
                        actions_done = [("Toggle", "omniscience")]
                    
                    case "p": # 'p' toggles Instant Break (Deal infinite damage.) [DEBUG]
                        variables.debug_toggles["instant_break"] = not variables.debug_toggles["instant_break"]
                        actions_done = [("Toggle", "instant break")]
                    
                    case "=": # '=' runs the reset command and closes the program.
                        temp_map_data : dict = {}
                        temp_player_data : dict = {}
                        reset_data(True)
                        with open("The Chasm/player_data.json", "r") as file: # Loading data from "player_data.json".
                            temp_player_data = json.load(file)
                        with open("The Chasm/map_data.json", "r") as file: # Loading data from "map_data.json".
                            temp_map_data = json.load(file)
                        if map_data != temp_map_data or player_data != temp_player_data:
                            exit()
                        actions_done = [True]
                    
                    case "m": # 'm' automatically levels you up. [DEBUG]
                        gain_xp((((2 * XP_SCALING_FACTOR) * (player_data["level"] ^ 2)) + (XP_SCALING_FACTOR * player_data["level"]) + 100))
                        actions_done = ("Level Up")
                    
                    case "esc": # 'esc' sends you to the pause menu.
                        current_screen = "pause"
                        current_menu_options = ["Back to Title", "Inventory", "Crafting", "Skills", "Stats"]
                        selected_option = current_menu_options[0]
                        actions_done = [True]