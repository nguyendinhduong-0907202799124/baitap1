class Toppings:
    def __init__(self,topping_type,weight):
        self.topping_type = topping_type
        self.weight = weight
    def get_topping_type(self):
        return self.__topping_type
    def set_topping_type(self, topping_type):
        self.__topping_type = topping_type
    def get_weight(self):
        return self.weight
    def set_weight(self, weight):
        self.weight = weight
class Dough:
    def __init__(self, flour_type, baking_technique, weight):
        self.flour_type = flour_type
        self.baking_technique = baking_technique
        self.weight = weight
    def get_flour_type(self):
        return self.flour_type
    def set_flour_type(self, flour_type):
        self.flour_type = flour_type
    def get_baking_technique(self):
        return self.baking_technique
    def set_baking_technique(self, baking_technique):
        self.baking_technique = baking_technique
    def get_weight(self):
        return self.weight
    def set_weight(self, weight):
        self.weight = weight
class Pizza:
    def __init__(self, name, dough, toppings_capacity):
        self.name = name
        self.dough = dough
        self.toppings = {}  
        self.toppings_capacity = toppings_capacity
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name
    def get_dough(self):
        return self.dough
    def set_dough(self, dough):
        self.dough = dough
    def get_toppings(self):
        return self.toppings
    def get_toppings_capacity(self):
        return self.toppings_capacity
    def set_toppings_capacity(self, toppings_capacity):
        self.toppings_capacity = toppings_capacity
    def add_topping(self, topping):
        if len(self.toppings) >= self.toppings_capacity:
            raise ValueError("Not enough space for another topping")
        topping_type = topping.get_topping_type()
        topping_weight = topping.get_weight()
        if topping_type in self.toppings:
            self.toppings[topping_type] =self.toppings[topping_type]+ topping_weight
        else:
            self.toppings[topping_type] = topping_weight
    def calculate_total_weight(self):
        total_weight = self.dough.get_weight() + sum(self.toppings.values())
        return total_weight