"""
Classes for The Chasm
"""

class Room():
    """
    Room Class for Map Generation Function
    """
    def __init__(self, x, y, width, height):
        self.x1 = x # Top Corner X
        self.y1 = y # Top Corner Y
        self.x2 = x + width # Bottom Corner X
        self.y2 = y + height # Bottom Corner Y
        self.center = (int(round(self.x1 + self.x2) / 2), int(round(self.y1 + self.y2) / 2))
    
    def is_intersecting(self, room2): # Returns whether or not that this room is intersecting another room.
        
        return ((self.x1 <= room2.x2) and (self.x2 >= room2.x1) and (self.y1 <= room2.y2) and (self.y2 >= room2.y1))
    
    def to_dict(self):
        
        return self.__dict__

class Resource_Node():
    """
    Resource Node Class for Node Generation Function
    """
    def __init__(self, id, item, tier, amount, pos, health):
        self.id = id # Node ID
        self.item = item # Resource Type
        self.tier = tier # Tier Required to Harvest Effectively
        self.amount = amount # Amount of Resources in Node
        self.position = pos # Node Position
        self.health = health # Node Health
    
    def to_dict(self):
        
        return self.__dict__

class Map_Layout():
    """
    Layout Class for Map Storage and Generation Function
    """
    def __init__(self, layout, rooms, start, end, objects : dict):
        self.layout = layout # Map Layout
        self.rooms = rooms # Rooms in Map Layout
        self.entrance = start # Entrance Point (LADDER_UP)
        self.exit = end # Exit Point (LADDER_DOWN)
        self.nodes = objects # Resource Nodes
    
    def to_dict(self):
        
        return self.__dict__

class Recipe():
    """
    Class for Recipe comprehension
    """
    def __init__(self, item, amount : int, materials : dict, xp : int):
        self.item = item
        self.amount_crafted = amount
        self.materials = materials
        self.xp_granted = xp
    
    def __str__(self):
        
        return f"{self.item}"

    def can_craft(self, player_data : dict):
        for material, amount in self.materials.items():
            if not material in player_data["inventory"]["raw_materials"] and not material in player_data["inventory"]["crafted_items"]:
                
                return False
            
            else:
                if material in player_data["inventory"]["raw_materials"]:
                    if amount > player_data["inventory"]["raw_materials"][material]:
                        
                        return False
                
                else:
                    if amount > player_data["inventory"]["crafted_items"][material]:
                        
                        return False
        
        return True
    
    def calc_max_amount(self, player_data : dict):
        values = []
        for material, amount in self.materials.items():
            if material not in player_data["inventory"]["raw_materials"]:
                if material not in player_data["inventory"]["crafted_items"]:
                    values.append(0)
                
                else:
                    values.append(int((player_data["inventory"]["crafted_items"][material] - player_data["inventory"]["crafted_items"][material] % amount) / amount))
            
            else:
                if material not in player_data["inventory"]["raw_materials"]:
                    values.append(0)
                
                else:
                    values.append(int((player_data["inventory"]["raw_materials"][material] - player_data["inventory"]["raw_materials"][material] % amount) / amount))
        return min(values)

    def craft_item(self, player_data : dict):
        for material, amount in self.materials.items():
            if material not in player_data["inventory"]["raw_materials"]:
                player_data["inventory"]["crafted_items"][material] -= amount
                if player_data["inventory"]["crafted_items"][material] == 0:
                    player_data["inventory"]["crafted_items"].pop(material)
            
            else:
                player_data["inventory"]["raw_materials"][material] -= amount
                if player_data["inventory"]["raw_materials"][material] == 0:
                    player_data["inventory"]["raw_materials"].pop(material)
            
        if str(self) in player_data["inventory"]["crafted_items"]:
            player_data["inventory"]["crafted_items"][str(self)] += self.amount_crafted
        
        else:
            player_data["inventory"]["crafted_items"][str(self)] = self.amount_crafted
        player_data["inventory"]["crafted_items"] = dict(sorted(player_data["inventory"]["crafted_items"].items()))
        player_data["inventory"]["raw_materials"] = dict(sorted(player_data["inventory"]["raw_materials"].items()))
        player_data["experience"] += self.xp_granted

class Harvester_Recipe():
    def __init__(self, item, materials : dict):
        self.item = item
        self.materials = materials
    
    def can_craft(self, player_data : dict):
        for material, amount in self.materials.items():
            if not material in player_data["inventory"]["raw_materials"] and not material in player_data["inventory"]["crafted_items"]:
                
                return False
            
            else:
                if material in player_data["inventory"]["raw_materials"]:
                    if amount > player_data["inventory"]["raw_materials"][material]:
                        
                        return False
                
                else:
                    if amount > player_data["inventory"]["crafted_items"][material]:
                        
                        return False
        
        return True
    
    def craft_item(self, player_data : dict):
        for material, amount in self.materials.items():
            if material not in player_data["inventory"]["raw_materials"]:
                player_data["inventory"]["crafted_items"][material] -= amount
                if player_data["inventory"]["crafted_items"][material] == 0:
                    player_data["inventory"]["crafted_items"].pop(material)
            
            else:
                player_data["inventory"]["raw_materials"][material] -= amount
                if player_data["inventory"]["raw_materials"][material] == 0:
                    player_data["inventory"]["raw_materials"].pop(material)