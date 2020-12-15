class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def print_info(self):
        return "{} {} {}".format(self.year, self.make, self.model)
    
    def __str__(self):
        return "%d %s %s" % (self.year, self.make, self.model)