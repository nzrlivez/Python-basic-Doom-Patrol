# hw_4

# 1
#  class Vehicle :
#      def __init__(self, max_speed, mileage) :
#          self.speed = max_speed
#          self.mileage = mileage

# 2
# class Bus(Vehicle) :
#     def __init__(self, max_speed, mileage, capacity) :
#         self.max_speed = max_speed
#         self.mileage = mileage
#         self.capacity = seating_capacity
#
#     def seating_capacity(self):
#         print(f'Bus contains {self.capacity} seats')
#
# School_bus = Bus(50, 60, 70)


# 2.2
# class Bus(Vehicle):
#     def __init__(self, max_speed, mileage, capacity):
#         super().__init__(max_speed, mileage)
#         self.capacity = capacity
#
#     def seating_capacity(self):
#         print(f'Bus contains {self.capacity} seats')
#
#
# bus = Bus(50, 60, 70)
# bus.seating_capacity()



# 3
# print(type(School_bus))

# 4
# print(instance(school_bus, Vehicle))

# 5. Create a new class School with get_school_id and number_of_students instance attributes

# 5
# class School :
#     def __int__(self, get_school_id, numer_of_student) :
#         self.get_school_id = get_school_id
#         self.numer_of_student = numer_of_student

# 6
# class SchoolBus :
#     def __int__(self, max_speed, mileage, capacity, get_school_id, numer_of_student, bus_school_color) :
#         super().__init__(bus_school_color)
#         self.bus_school_color = bus_school_color
#
#     def bus_school_color(self):
#          print(f'Bus color is {self.bus_school_color}.')

# 7
# class Bear :
#     def __init__(self, sound) :
#         self.sound = sound
#
#     def make_sound(self) :
#         print (f'Bear make sound like {self.sound}!')
#
#
# class Wolf :
#     def __init__(self, sound) :
#         self.sound = sound
#
#     def make_sound(self) :
#         print (f'Wolf make sound like {self.sound}!')
#
# Big_Bear = Bear('Rrrrrrrr')
# Gray_Wolf = Wolf('Uuuuuuuuu')
#
# animals = (Big_Bear, Gray_Wolf)
#
# for animal_sound in animals :
#     print(animal_sound.make_sound())

# 8
# class City:
#     def __init__(self, name, population):
#         self.name = name
#         self.population = population
#
#         def check_population(self):
#             if self.population > 1500:
#                 return self.population
#             else:
#                 return(f'Your city {self.name} is too small')
#
#
# Lviv = City('Lviv', 10000)
# IF = City('IF', 5000)
# all_cites = (Lviv, IF)
#
# for i in all_cites:
#     print(i.check_population())
