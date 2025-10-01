from swap_meet.item import Item

class Electronics(Item):
    def __init__(self, id=None, type="Unknown", condition=0):
        super().__init__(id=id, condition=condition)
        self.type = type

    def get_category(self):
        return "Electronics"

    def __str__(self):
        return f"An object of type Electronics with id {self.id}. This is a {self.type} device."

    def condition_description(self): # We can omit this method in the subclass—since its behavior isn’t overridden, the parent’s condition_description() is inherited as-is.
        return super().condition_description()