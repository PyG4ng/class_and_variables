class Animal:
  def __init__(self, name, weight):
    self.name = name
    self.weight = weight
  
  def __str__(self):
    return f"{self.name} весит {self.weight}кг"
  
  def feed(self):
    print(f"{self.name} был накормлен")
  pass

  def farm_job(self):
    print(f"Для {self.name} нужна следующая процедура: ")

# Птицы с яйцами
class Bird(Animal):
  def __init__(self, name, weight):
    super().__init__(name, weight)

  def farm_job(self):
    super().farm_job()
    print("Сбор яйц")

# Гусы
class Goose(Bird):
  voice = "Голос гуся"
  def __init__(self, name, weight):
    super().__init__(name, weight)

# Курицы
class Chicken(Bird):
  voice = "Голос Курицы"
  def __init__(self, name, weight):
    super().__init__(name, weight)

# Утки
class Duck(Bird):
  voice = "Голос Утки"
  def __init__(self, name, weight):
    super().__init__(name, weight)

# Животные которых надо доить
class VivipariousWithMilk(Animal):
  def __init__(self, name, weight):
    super().__init__(name, weight)

  def farm_job(self):
    super().farm_job()
    print("Дойка")

# Коровы
class Cow(VivipariousWithMilk):
  voice = "Голос Коровы"
  def __init__(self, name, weight):
    super().__init__(name, weight)

# Козы
class Goat(VivipariousWithMilk):
  voice = "Голос Козы"
  def __init__(self, name, weight):
    super().__init__(name, weight)

# Овцы
class Sheep(Animal):
  voice = "Голос Овцы"
  def __init__(self, name, weight):
    super().__init__(name, weight)

  def farm_job(self):
    super().farm_job()
    print("Стричь")

gouss_01 = Goose("Серый", 3.4)
gouss_02 = Goose("Белый", 4.1)
korova = Cow("Маньку", 154.2)
ovets_01 = Sheep("Барашек", 84.4)
ovets_02 = Sheep("Кудрявый", 74.2)
kouritssa_01 = Chicken("Ко-Ко", 5.19)
kouritssa_02 = Chicken("Кукареку", 3.81)
koza_01 = Goat("Рога", 44.61)
koza_02 = Goat("Копыта", 53.15)
utka = Duck("Кряква", 3.8)

animals_list = [
  gouss_01,
  gouss_02,
  korova,
  ovets_01,
  ovets_02,
  kouritssa_01,
  kouritssa_02,
  koza_01,
  koza_02,
  utka
  ]

total_weight = 0
max_weight = 0
for animal in animals_list:
  print(animal)
  animal.feed()
  print(animal.voice)
  animal.farm_job()
  print()

  total_weight += animal.weight

  if animal.weight > max_weight:
    max_weight = animal.weight
    boss = animal.name

print(f"""Oбщий вес всех животных: {total_weight}кг
Название самого тяжелого животного: {boss} с весом {max_weight}кг""")

