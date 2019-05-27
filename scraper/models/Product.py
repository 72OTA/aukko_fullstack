## definición base de producto a nivel de busqueda.
class Product:
    def __init__(self, title, category, price, description):
        self.title = title
        self.category = category
        self.price = price
        self.description = description

    def toString(self):
        print(self.title)

    def __eq__(self, entity):
        if isinstance(entity, Product):
            return self.title == entity.title and self.category == entity.category
        return False