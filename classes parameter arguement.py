class MyCar:
    def __init__ (self, name, model, color, date):
        self.name = name
        self.model = model
        self.color = color
        self.date = date

toyota = MyCar("Toyota,", "Model-y,", "White,", "2015")
benz = MyCar("Benz,", "C-class,", "black,", "2020",)
lexus = MyCar("Lexus,", "Lexus-360,", " Brown,", "2024",)

print(toyota.name, toyota.model, toyota.color, toyota.date)
print(lexus.name, lexus.model, lexus.color, lexus.date)
print(benz.name, benz.model, benz.color, benz.date)
        