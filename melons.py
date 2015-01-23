"""This file should have our melon-type classes in it."""

class Watermelon(object):
    name = "Watermelon"
    color = "green"
    is_imported = False
    shape = "natural"
    seasons = ["Fall", "Summer"]

    def get_price(self, qty):
        base_price = 5.00
        if qty >= 3:
            base_price = base_price * qty * 0.75
        
        return base_price


class Cantaloupe(object):
    name = "Cantaloupe"
    color = "tan"
    is_imported = False
    shape = "natural"
    seasons = ["Summer", "Spring"]

    def get_price(self, qty):
        if qty >= 5:
            return 2.50 * qty
        else:
            return 5.00 * qty
        

class Casaba(object):
    name = "Casaba"
    color = "green"
    is_imported = True
    shape = "natural"
    seasons = ["Spring", "Fall", "Summer", "Winter"]

    def get_price(self, qty):
        base_price = 6.00
        price = base_price * 1.5 * qty
        
        return price

class Sharlyn(object):
    name = "Sharlyn"
    color = "tan"
    is_imported = True
    shape = "natural"
    seasons = ["Summer"]

    def get_price(self, qty):
        return 5.00 * 1.5 * qty


class SantaClaus(object):
    name = "Santa Claus"
    color = "green"
    is_imported = True
    shape = "natural"
    seasons = ["Spring","Winter"]

    def get_price(self, qty):
        base_price = 5.00
        price = base_price* qty * 1.5
        return price 


class Christmas(object):
    name = "Christmas"
    color = "green"
    is_imported = False
    shape = "natural"
    seasons = ["Winter"]

    def get_price(self, qty):
        return 5.00 * qty


class HornedMelon(object):
    name = "Horned Melon"
    color = "yellow"
    is_imported = True
    shape = "natural"
    seasons = ["Summer"]

    def get_price(self, qty):
        base_price = 5.00
        price = base_price * 1.5 * qty
        return price

class Xigua(object):
    name = "Xigua"
    color = "black"
    is_imported = True
    shape = "square"
    seasons = ["Summer"]

    def get_price(self, qty):
        return 1.5 * 5.00 * 2 * qty

class Ogens(object):

    name = "Ogen"
    color = "tan"
    is_imported = False
    shape = "natural"
    seasons = ["Spring", "Summer"]

    def get_price(self, qty):
        base_price = 6.00
        return base_price * qty


