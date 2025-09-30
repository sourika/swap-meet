class Vendor:
    def __init__(self, inventory = None):
        if inventory is None:
            self.inventory = []
        else:
            self.inventory = inventory


    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:
            return False
    
    def get_by_id(self, id):
        for item in self.inventory:
            if item.id == id:
                return item
        return None

    def swap_items(self, other_vendor, my_item, their_item):
        if my_item in self.inventory and their_item in other_vendor.inventory:
            other_vendor.inventory.append(my_item)
            self.inventory.remove(my_item)
            other_vendor.inventory.remove(their_item)
            self.inventory.append(their_item)
            return True
        return False

    def swap_first_item(self, other_vendor):
        if self.inventory and other_vendor.inventory:
            self.inventory[0], other_vendor.inventory[0] = other_vendor.inventory[0], self.inventory[0]
            return True
        return False






        