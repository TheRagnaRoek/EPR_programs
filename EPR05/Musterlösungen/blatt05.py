"""
"""
__author__ = "7592047, Khauto"
__email__ = "khauto@em.uni-frankfurt.de"

import copy
from datetime import datetime
import json

def print_nested_dict(data):
    """
    Diese Funktion hat nichts mit der Aufgabe zu tun.
    """
    print(json.dumps(data, indent=4, ensure_ascii=False))


def add_items(inventory, **items):
    """
    Adds items to the inventory at specified locations. If a location already exists,
    it updates the content; otherwise, it creates a new location.

    Parameters:
        inventory (dict): The current inventory dictionary.
        **items: Key-value pairs representing the location (key) and its items (value).

    Returns:
        None
    """
    for location, content in items.items():  
        if location in inventory:
            inventory[location].update(content) 
        else:
            inventory[location] = content


def list_all_items(inventory):
    """
    Lists all items in the inventory, sorted alphabetically.

    Parameters:
        inventory (dict): The current inventory dictionary.

    Returns:
        list: A sorted list of all item names across all locations.
    """
    sorted_items = []
    for location in inventory.values():
        for item in location:
            sorted_items.append(item)
    sorted_items.sort()
    return sorted_items


def search_item(inventory, item_name):
    """
    Searches for an item by name in the inventory.

    Parameters:
        inventory (dict): The current inventory dictionary.
        item_name (str): The name of the item to search for.

    Returns:
        tuple:
            - bool: True if the item is found, False otherwise.
            - dict/str: A dictionary containing the item's location and details if found, 
              or an error message if not found.
    """
    for location, items in inventory.items():
        if item_name in items:
            return True, {location: items[item_name]}
    return False, f"Item '{item_name}' not found."


def summarize_items_by_location(inventory, *locations):
    """
    Summarizes the items stored at specific locations.

    Parameters:
        inventory (dict): The current inventory dictionary.
        *locations (str): Variable number of location names to summarize.

    Returns:
        dict: A dictionary where keys are location names and values are lists of item names
              or an error message if the location is not found.
    """
    summary = {}
    for location in locations:
        if location in inventory:
            summary[location] = list(inventory[location].keys())
        else:
            summary[location] = "Location not found in inventory"
    return summary


def update_inventory_with_shallow_copy(inventory, item_name, **updates):
    """
    Updates the details of an item in the inventory using a shallow copy. This demonstrates
    that modifications to nested objects affect the original inventory.

    Parameters:
        inventory (dict): The current inventory dictionary.
        item_name (str): The name of the item to update.
        **updates: Key-value pairs representing the updates to apply to the item.

    Returns:
        None
    """
    shallow_copy = inventory.copy()
    found, info = search_item(shallow_copy, item_name)

    if found:
        location = next(iter(info)) 
        shallow_copy[location][item_name].update(updates)
        return True
    else:
        return False


def create_inventory_backup(inventory):
    """
    Creates a deep copy of the inventory and timestamps it. This ensures that
    the backup remains unaffected by future changes to the inventory.

    Parameters:
        inventory (dict): The current inventory dictionary.

    Returns:
        tuple:
            - str: A formatted timestamp of when the backup was created.
            - dict: A deep copy of the inventory.
    """
    deep_copy = copy.deepcopy(inventory)
    current_time = datetime.now()
    formatted_datetime = current_time.strftime("%Y-%m-%d %H:%M:%S")
    return formatted_datetime, deep_copy


if __name__ == "__main__":
    inventory = {}
    items_to_keller = {
        "Hammer": {"Anzahl": 5, "Zustand": "neu"},
        "Bett": {"Anzahl": 2, "Zustand": "alt"}
    }
    items_to_garage = {
        "Auto": {"Anzahl":1, "Zustand": "neu", "Model": "Porsche"},
        "garageitem": {"something":"value1"}
    }
    
    # print("Ursprünglich:")
    # print_nested_dict(inventory)
    add_items(inventory, keller=items_to_keller, garage=items_to_garage)
    # print("Nach dem Aufruf der Funktion:")
    # print_nested_dict(inventory)
    # print()
    # print(summarize_items_by_location(inventory, "keller", "garage", "bedroom"))
    # print()
    print(list_all_items(inventory))

    time, backup = create_inventory_backup(inventory)

    update_inventory_with_shallow_copy(inventory, "Auto", Model="Merzedes", Farbe="Gelb")  
    print_nested_dict(inventory)
    print()
    
    print(f"Backup: {time}")
    print_nested_dict(backup)
    print()

    # print("Alles:", list_all_items(inventory))

    # item = {"test": {"Anzahl": 123, "sts": "rr"}}
    # add_items(inventory, keller=item)
    # print("aktual. Inventar:", inventory)

    # print(create_item(name="car", status="neu", farbe="rot"))