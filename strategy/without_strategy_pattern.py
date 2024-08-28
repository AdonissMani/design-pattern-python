'''
Without pattern
'''

class Vehicle:
    '''
    Parent class
    '''
    
    def engine(self):
        print("low engine")
    
    def breaking(self):
        print("low break")

    
class SportsVehicle(Vehicle):
    '''
    Child class
    '''
    
    def engine(self):
        print("High engine")
    
    def breaking(self):
        print("High break")
    

class OffRoadVehicle(Vehicle):
    '''
    Child class
    '''

    def engine(self):
        print("Normal engine")
    
    def breaking(self):
        print("High break")    

class PassengerVehicle(Vehicle):
    '''
    Child class
    '''

    def engine(self):
        print("Normal engine")

    def breaking(self):
        print("Normal break")
