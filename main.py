class Warrior():

    def __init__(self, name, power, endurance, hair_color):
        self.name = name
        self.power = power
        self.endurance = endurance
        self.hair_color = hair_color

    def sleep(self):
        print(f'{self.name} лег спать')
        self.endurance += 2

    def eat(self):
        print(f'{self.name} сел кушать')
        self.power += 1

    def hit(self):
        print(f'{self.name} бьет кого-то')
        self.endurance -= 6

    def walk(self):
        print(f'{self.name} гуляет')

    def info(self):
        print(f'имя воина - {self.name}')
        print(f'цвет волос воина - {self.hair_color}')
        print(f'сила воина - {self.power}')
        print(f'выносливость воина - {self.endurance}')

war1 = Warrior('Степан', 75, 40, 'брюнет')
war2 = Warrior('Николай', 90, 50, 'блондин')

print(f'{war1.name}, сила: {war1.power}, выносливость: {war1.endurance}, {war1.hair_color}')

print(war2.name)
print(f'сила: {war2.power}')
print(f'выносливость: {war2.endurance}')
print(war2.hair_color)

war1.sleep()
war1.eat()
war1.hit()
war1.walk()
war1.info()

war2.sleep()
war2.eat()
war2.hit()
war2.walk()
war2.info()