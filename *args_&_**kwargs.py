""" '*args' : arguments; pass arguments as much as you want without defining them as parameters in a function """

# def add(*args):
#     print(type(args))
#     s=0
#     for i in args:
#         s+=i
#     print(s)
#
# add(3,4,6,8,3,2,1,7,0)


""" through *args we can fetch position of the argument """

# def position(*args):
#     print(args[0])
#     print(args[8])
#     print(args[4])
#     print(args[1])
#     print(args[3])
#
# position(3,4,6,8,3,2,1,7,0)



""" **kwargs : keyword arguments;  pass arguments as much as you want without defining them as parameters in a function """


# def calculate(n, **kwargs):
#     print(kwargs)
#
#     n+= kwargs['add']
#     n*= kwargs['multiply']
#     print(n)
#
# calculate(2, add=3, multiply=5)

""" or """

# class car:
#     def __init__(self, **kw):
#         self.name = kw['name']
#         self.color = kw['color']
#         self.model = kw['model']
#     def printing(self):
#         print(self.name, self.model, self.color)
# my_car = car(color = "Black",name = "Nissan", model = "GT-R")
# my_car.printing()


""" **kwargs with 'get' key ; its basically helpful when you forgot to assign an argument during creating an oject 
of the class ; in this scenerio 'get' method will return None instead of error (works with '()' round brackets) """


# class car:
#     def __init__(self, **kw):
#         self.name = kw.get('name')
#         self.color = kw.get('color')
#         self.model = kw.get('model')
#     def printing(self):
#         print(self.name, self.model, self.color)
# my_car = car(name = "Nissan", model = "GT-R")
# my_car.printing()