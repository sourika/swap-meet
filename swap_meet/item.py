import uuid


class Item:
    def __init__(self, id = None, condition = 0):
        if id is None:
            self.id = uuid.uuid4().int
        else:
            self.id = id
        self.condition = condition        

    
    def get_category(self):
        return "Item"
    
    def __str__(self):
        return f"An object of type Item with id {self.id}."

    def condition_description(self):
        if self.condition == 0:
            return "heavily used"
        elif 0 < self.condition < 4:
            return "mint"
        elif 4 <= self.condition <= 5:
            return "excellent"

    