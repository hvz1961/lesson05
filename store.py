class Store():
    def __init__(self, name_store, address):
        self.name_store = name_store
        self.address = address
        self.items = {}

    def add_items(self, name, price):
        self.items[name] = price
        print(f'товар {name} добавлен в {self.name_store}')

    def delete_items(self, name):
        if name in self.items:
            del self.items[name]
            print(f'товар {name} удален из {self.name_store}')

    def get_price(self, name):
        return self.items.get(name, None)

    def update_price(self, name, new_price):
        if name in self.items:
            self.items[name] = new_price
            print(f'цена на {name} изменена в {self.name_store}')
        else:
            print(f'товар {name} не найден')

stor1 = Store('"Дикси"','Санкт-Петербург ул.Милионная д.3')
print(stor1.name_store,stor1.address)
stor1.add_items('яблоки', 100)
stor1.add_items('бананы', 50)

print(stor1.get_price('яблоки'))
print(stor1.get_price('груши'))
print(stor1.get_price('бананы'))

stor1.update_price('яблоки', 120)
print(stor1.get_price('яблоки'))

stor2 = Store('"СтройДом"','Санкт-Петербург ул.Войнова д.15')
print(stor2.name_store,stor2.address)
stor2.add_items('гвозди', 20)
stor2.add_items('болты', 25)

print(stor2.get_price('гвозди'))
print(stor2.get_price('заклепки'))
print(stor2.get_price('болты'))

stor2.update_price('гвозди', 30)
print(stor2.get_price('гвозди'))

stor3 = Store('"Стиль"','Санкт-Петербург ул.Халтурина д.27')
print(stor3.name_store,stor3.address)
stor3.add_items('носки', 200)
stor3.add_items('шнурки', 70)

print(stor3.get_price('носки'))
print(stor3.get_price('платки'))
print(stor3.get_price('шнурки'))

stor3.update_price('носки', 230)
print(stor3.get_price('носки'))


