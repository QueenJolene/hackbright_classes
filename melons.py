"""This file should have our melon-type classes in it."""


#left off with Casaba Melons, need to figure out why it is still muliplying original price and not 
# rebound price.

class AbstractMelon(object):

    def __init__(self):
        try:
            raise TypeError("You can not make an instance from this class. Please use a specific melon type.")
        except TypeError,e:
            print e

    def get_base_price(self):
        return 5.00

    def get_price(self, qty, is_imported, shape, add_on = False):
        base_price = self.get_base_price()
        if add_on == True:
            base_price = base_price + 1

        if is_imported == True:
            base_price = base_price * 1.5

            if shape not in "natural":
                base_price = base_price * 2

        else:
            base_price = self.get_base_price()

            if shape not in "natural":
                base_price = base_price * 2

        return base_price * qty


class Watermelon(AbstractMelon):
    name = "Watermelon"
    color = "green"
    is_imported = False
    shape = "natural"
    seasons = ["Fall", "Summer"]

    def __init__(self):
        pass

    def get_price(self, qty):
        base_price = super(Watermelon, self).get_price(qty, self.is_imported, self.shape)
        if qty >= 3:
            return base_price * 0.75
        else:        
            return base_price


class Cantaloupe(AbstractMelon):
    name = "Cantaloupe"
    color = "tan"
    is_imported = False
    shape = "natural"
    seasons = ["Summer", "Spring"]

    def __init__(self):
        pass

    def get_price(self, qty):
        base_price = super(Cataloupe, self).get_price(qty, self.is_imported, self.shape)
        if qty >= 5:
            return base_price * 0.5
        else:
            return base_price
        

class Casaba(AbstractMelon):
    name = "Casaba"
    color = "green"
    is_imported = True
    shape = "natural"
    seasons = ["Spring", "Fall", "Summer", "Winter"]
    add_on = True
    
    def __init__(self):
        pass

    def get_price(self, qty):
        base_price = super(Casaba, self).get_price(qty, self.is_imported, self.shape)
        return base_price

class Sharlyn(AbstractMelon):
    name = "Sharlyn"
    color = "tan"
    is_imported = True
    shape = "natural"
    seasons = ["Summer"]

    def __init__(self):
        pass

    def get_price(self, qty):
        return self.get_base_price() * 1.5 * qty


class SantaClaus(AbstractMelon):
    name = "Santa Claus"
    color = "green"
    is_imported = True
    shape = "natural"
    seasons = ["Spring","Winter"]

    def __init__(self):
        pass

    def get_price(self, qty):
        return self.get_base_price() * qty * 1.5


class Christmas(AbstractMelon):
    name = "Christmas"
    color = "green"
    is_imported = False
    shape = "natural"
    seasons = ["Winter"]

    def __init__(self):
        pass

    def get_price(self, qty):
        return self.get_base_price() * qty


class HornedMelon(AbstractMelon):
    name = "Horned AbstractMelon"
    color = "yellow"
    is_imported = True
    shape = "natural"
    seasons = ["Summer"]

    def __init__(self):
        pass

    def get_price(self, qty):
        return self.get_base_price() * 1.5 * qty

class Xigua(AbstractMelon):
    name = "Xigua"
    color = "black"
    is_imported = True
    shape = "square"
    seasons = ["Summer"]

    def __init__(self):
        pass

    def get_price(self, qty):
        return 1.5 * self.base_price() * 2 * qty

class Ogens(AbstractMelon):

    name = "Ogen"
    color = "tan"
    is_imported = False
    shape = "natural"
    seasons = ["Spring", "Summer"]

    def __init__(self):
        pass

    def get_price(self, qty):
        return (self.get_base_price() + 1) * qty
