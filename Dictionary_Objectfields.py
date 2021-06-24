import datetime

"""
The term object fields means to get all the object of a class or variable in the form
of a dictionary.
For this we have an inbuilt private method __dict__ and a function vars.
"""

# noinspection PyMethodMayBeStatic
class Aryan(object):
    def __init__(self):
        self.Name = 'Aryan'
        self.Class = 'BTech'
        self.Sec = 'A'
        self.Roll = 86
        self.Branch = 'CSE'
        self.dt = self.print_times()

    def print_times(self):
        st = str(datetime.datetime.now())
        return st

a = Aryan()
print(a.__dict__) # This is how we print all the objects fields using __dict__ method.
