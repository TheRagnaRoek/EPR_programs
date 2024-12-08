"""Inventory system implemented using nested dictionaries"""

__author__ = "7003725, van Reem"
__email__ = "drvanreem@stud.uni-frankfurt.de"

import copy
from datetime import datetime


def create_inventory(*locations: str) -> dict:
    """Creates an inventory with specified locations.

    :param locations: Location strings for keywords
    :return: Inventory dictionary"""
    inventory = dict()
    for location in locations:
        inventory[location] = None

    return inventory


def add_locations(inventory: dict, *locations: str) -> None:
    """Adds locations to a given inventory.

    :param inventory: Inventory dictionary
    :param locations: Location strings to be added

    :return: None"""
    for location in locations:
        if location in inventory:
            pass
        else:
            inventory[location] = None


def add_items_to_location(inventory: dict, location: str, **items: dict) -> None:
    """Adds items as dictionaries into specified location in the inventory.

    :param inventory: Inventory dictionary
    :param location: Location in the inventory (str)
    :param items: Item dicts to be added to the location in the inventory.
    Format: Itemname (kw): dict(attribute: value, etc.)

    :return: None"""

    if location in inventory:
        if inventory[location] is None:
            inventory[location] = {}  # create empty dictionary to enable dict functions
        for item_name, attributes in items.items():
            if not isinstance(items[item_name], dict):  # prohibit wrong item formats from being added
                print(f"Error: Item {item_name} has wrong datatype (must be dict)")
            else:
                inventory[location][item_name] = attributes
    else:
        print("Error: Location not in dictionary")


def show_all_items(inventory: dict) -> list:
    """Returns an alphabetically sorted list of all items at all locations

    :param inventory: Inventory-Dictionary
    """
    sorted_inventory: list = []
    for location in inventory:  # .values only accesses values, not keywords
        # print(location)  # debug
        if inventory[location] is None:
            continue
        else:
            for item in inventory[location]:
                # print(item)  # debug
                if item not in sorted_inventory:
                    sorted_inventory.append(item)
    sorted_inventory.sort()

    return sorted_inventory


def search_inventory(inventory: dict, item: str) -> tuple[bool, list]:
    """Searches for an item's locations in the dictionary.

    :param inventory: Inventory-Dictionary
    :param item: Item to be searched in the inventory (str)

    :return: True, location  if item is in the inventory, False if not
    """
    item_found = False
    locations = []

    print(f"Searching for {item}...")
    for location in inventory:
        if inventory[location] is None:
            continue
        if item in inventory[location]:
            item_found = True
            print(f"Item {item} found at {location}")
            locations.append(location)

    if item_found is True:
        return True, locations

    print(f"Item {item} was not found in the inventory.")
    return False, []


def get_location_inventory(inventory: dict, *locations: str) -> dict:
    """Gets the inventory of the specified location(s) as a dictionary

    :param inventory: Inventory dictionary
    :param locations: Locations for which to generate inventory overviews

    :return: Dictionary containing the summaries for each specified location."""
    summaries = {}
    for location in locations:
        if location in inventory:
            if inventory[location] is None:
                summaries[location] = None
            else:
                summaries[location] = list(inventory[location].items())
        else:
            summaries[location] = "Location not found"

    return summaries


def update_item(inventory: dict, item: str, location: str, **updates) -> bool:
    """Updates item attributes at specified location using the shallow copy function

    Demonstrates that changes to nested data structures carry over to the original top-level structure

    :param inventory: Inventory dictionary
    :param item: Item to be updated (str)
    :param location: Location at which the item should be updated
    :updates: Attributes to be added to the specified item (kwarg)
    :return: True if item was updated, False if not (either wrong location or non-existent"""
    inv_copy = inventory.copy()
    is_in_inv, locations = search_inventory(inv_copy, item)

    if is_in_inv and location in locations:
        inv_copy[location][item].update(updates)
        return True
    else:
        print("Error: Item not at specified location")
        return False


def backup_inventory(inventory: dict) -> tuple:
    """Backs up the inventory and saves the timestamp of the copy.

    :param inventory: Inventory dictionary

    :return: formatted timestamp (str), inventory backup (deepcopy)"""

    inv_copy = copy.deepcopy(inventory)
    curr_time = datetime.now()
    timestamp = curr_time.strftime("%Y-%m-%d %H:%M:%S")

    print(f"Backup done at: {timestamp}")

    return timestamp, inv_copy


if __name__ == "__main__":
    inventory = create_inventory("cellar", "attic", "garage")
    print(inventory)
    add_locations(inventory, "living_room", "attic")
    print(inventory)
    add_items_to_location(inventory, "attic", Hammer=dict(Amount=2, Type="wood"), Bed=dict(Amount=2),
                          wrong_item="error")
    print(inventory)
    add_items_to_location(inventory, "living_room", Hammer=dict(Amount=4))

    print(show_all_items(inventory))

    print(search_inventory(inventory, "Hammer"))
    search_inventory(inventory, "Boat")

    print(get_location_inventory(inventory, "attic", "living_room", "cellar", "flat"))

    backup = backup_inventory(inventory)

    add_items_to_location(inventory, "cellar", Painting=dict(Year=1665))
    print(get_location_inventory(inventory, "cellar"))

    update_item(inventory, "Painting", "cellar", Painter="Rembrandt", Medium="Oil")
    print(get_location_inventory(inventory, "cellar"))
