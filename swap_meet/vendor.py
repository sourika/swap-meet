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

    def get_by_category(self, category):
        category_list = []
        for item in self.inventory:
            if item.get_category() == category:
                category_list.append(item)
        return category_list
    

    def get_best_by_category(self, category):
        best_item = None
        
        for item in self.inventory:
            if item.get_category() == category:
                if best_item is None or item.condition > best_item.condition:
                    best_item = item
            
        return best_item
    
    
    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        my_best_for_their = self.get_best_by_category(their_priority)
        their_best_for_me = other_vendor.get_best_by_category(my_priority)
        
        if not their_best_for_me or not my_best_for_their:
            return False
        else:
            temp = my_best_for_their
            my_best_for_their = their_best_for_me
            their_best_for_me = temp
        return True    



        