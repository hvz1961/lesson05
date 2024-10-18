class Store():
    def __init__(self, name_store, address):
        self.name_store = name_store
        self.address = address
    class Product():
    def add_product(self, name, price):
        self.name = name
        self.price = price
    def __repr__(self):
        return f'Товар(name={self.name}, prace={self.price})'
        if name.lower() == name.lower():
            return price
        else:
            return None
    def add_items(self, name, price):
        self.items[name] = price

    def delete_items(self, name, price):
        self.items[name] = price

stor1 = Store('Продмаг', 'Санкт-Петербург, ул.Милионная, д.3')
stor2 = Store('Строймаг', 'Санкт-Петербург, ул.Войнова, д.15')
stor3 = Store('Проммаг', 'Санкт-Петербург, ул.Халтурина, д.27')

stor1.name_store()
stor1.address()




