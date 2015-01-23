"""This file should have our melon-type classes in it."""

class AbstractMelon(object):

    def __init__(self):
        try:
            raise TypeError("You can not make an instance from this class. Please use a specific melon type.")
        except TypeError,e:
            print e

    def get_base_price(self):
        return 5.00

    def get_price(self, qty, is_imported, shape):
        base_price = self.get_base_price()
        if is_imported == True:
            base_price = self.get_base_price() * 1.5
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
        # if qty >= 3:
        #     base_price = self.get_base_price() * qty * 0.75
        #     return base_price
        # else:        
        #     return self.get_base_price() * qty
        print super(Watermelon, self).get_price(self, qty, self.is_imported, self.shape)


class Cantaloupe(AbstractMelon):
    name = "Cantaloupe"
    color = "tan"
    is_imported = False
    shape = "natural"
    seasons = ["Summer", "Spring"]

    def get_price(self, qty):
        if qty >= 5:
            return self.get_base_price() * 0.5 * qty
        else:
            return self.get_base_price() * qty
        

class Casaba(AbstractMelon):
    name = "Casaba"
    color = "green"
    is_imported = True
    shape = "natural"
    seasons = ["Spring", "Fall", "Summer", "Winter"]

    def get_price(self, qty):
        return (self.get_base_price() + 1) * 1.5 * qty

class Sharlyn(AbstractMelon):
    name = "Sharlyn"
    color = "tan"
    is_imported = True
    shape = "natural"
    seasons = ["Summer"]

    def get_price(self, qty):
        return self.get_base_price() * 1.5 * qty


class SantaClaus(AbstractMelon):
    name = "Santa Claus"
    color = "green"
    is_imported = True
    shape = "natural"
    seasons = ["Spring","Winter"]

    def get_price(self, qty):
        return self.get_base_price() * qty * 1.5


class Christmas(AbstractMelon):
    name = "Christmas"
    color = "green"
    is_imported = False
    shape = "natural"
    seasons = ["Winter"]

    def get_price(self, qty):
        return self.get_base_price() * qty


class HornedMelon(AbstractMelon):
    name = "Horned AbstractMelon"
    color = "yellow"
    is_imported = True
    shape = "natural"
    seasons = ["Summer"]

    def get_price(self, qty):
        return self.get_base_price() * 1.5 * qty

class Xigua(AbstractMelon):
    name = "Xigua"
    color = "black"
    is_imported = True
    shape = "square"
    seasons = ["Summer"]

    def get_price(self, qty):
        return 1.5 * self.base_price() * 2 * qty

class Ogens(AbstractMelon):

    name = "Ogen"
    color = "tan"
    is_imported = False
    shape = "natural"
    seasons = ["Spring", "Summer"]

    def get_price(self, qty):
        return (self.get_base_price() + 1) * qty
