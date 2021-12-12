# hw 5

# 1.
# class Laptop :
#     def __init__(self):
#         batery1 = Batery('This is configuration for batery 1 ')
#         batery2 = Batery('This is configuration for batery 2')
#         self.batery = [batery1, batery2]
#
# class Batery :
#     def __init__(self, configuration):
#         self.configuration = configuration
#
# laptop = Laptop()
# print(laptop.batery[0].configuration)
# print(laptop.batery[1].configuration)

# 2.
# class Guitar :
#     def __init__(self, accord):
#         self.accord = accord
#
# class GuitarString
#     def __init__(self,note):
#         self.note = note
#
# accord = accord()
# guitar = guitar(accord)


# 3

# class Calc:
#     @staticmethod
#     def add_nums(a, b, c):
#         return a + b + c
#
#
# m = Calc()
# print(m.add_nums(5, 6, 7))


# 4

# class Pasta :
#     def __init__(self, ingredients):
#         self.ingredients = [ingredients]
#
#     def __repr__(self):
#         return f'It consists of {self.ingredients}'
#
#     @classmethod
#     def carbonara(cls):
#         return cls(['forcemeat', 'tomatoes'])
#
#
#     @classmethod
#     def bolognaise(cls):
#         return cls(['bacon', 'parmesan', 'eggs'])
#
# pasta_1 = Pasta.carbonara()
# pasta_2 = Pasta.bolognaise()
# print(pasta_1)
# print(pasta_2)

 # 5.

# class Concert :
#     max_visitors_num = 0
#
#     def __init__(self):
#         self._visitors_count = 0
#
#     @property
#     def visitors_count(self):
#         return self._visitors_count
#
#     @visitors_count.setter
#     def visitors_count(self, num):
#         if num < self.max_visitors_num:
#             self._visitors_count = num
#         else:
#             self._visitors_count = self.max_visitors_num
#
#
# Concert.max_visitors_num = 50
# concert = Concert()
# concert.visitors_count = 1000
# print(concert.visitors_count)

# 6.
# import dataclasses
#
# @dataclasses.dataclass
# class AddressBookDataClass :
#     key : int
#     name : str
#     phone_number : str
#     address : str
#     email : str
#     birthday : str
#     age : int
#
# my_address = AddressBookDataClass (key=55,
#                                name= 'Nazar',
#                                phone_number= '998-889-999',
#                                address= 'centralna',
#                                email= 'nazar@gmail.com',
#                                birthday= '15th March',
#                                age=23)
# print(my_address)


# 7.
# from collections import namedtuple
#
#
# AddressBookDataClass_1 = namedtuple('AddressBookDataClass',
#                                     ['key', 'name',
#                                      'phone_number',
#                                      'address', 'email',
#                                      'birthday', 'age'])
#
# me_add = AddressBookDataClass_1(33, 'Nazar',
#                                     '998-889-999',
#                                     'centralna',
#                                     'nazar@gmail.com',
#                                     '15th March', 23)

# 8.







