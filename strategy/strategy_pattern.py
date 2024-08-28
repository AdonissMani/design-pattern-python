from abc import ABC, abstractmethod

# Interfaces
class EngineInterface(ABC):
    @abstractmethod
    def engine(self):
        pass

class BreakingInterface(ABC):
    @abstractmethod
    def breaking(self):
        pass

# Implementations of interfaces
class HighEngine(EngineInterface):
    def engine(self):
        print("High engine")

class HighBreaking(BreakingInterface):
    def breaking(self):
        print("High break")

class NormalEngine(EngineInterface):
    def engine(self):
        print("Normal engine")

class NormalBreaking(BreakingInterface):
    def breaking(self):
        print("Normal break")

class LowEngine(EngineInterface):
    def engine(self):
        print("Low engine")

class LowBreaking(BreakingInterface):
    def breaking(self):
        print("Low break")

# Vehicle class using constructor injection
class Vehicle(ABC):
    def __init__(self, engine: EngineInterface, breaking: BreakingInterface):
        self._engine = engine   # Store the engine object itself
        self._breaking = breaking  # Store the breaking object itself

    
    def start_engine(self):
        self._engine.engine()  # Call the engine method on the engine object

    def apply_break(self):
        self._breaking.breaking()  # Call the breaking method on the breaking object

# Subclasses of Vehicle
class SportsVehicle(Vehicle):
    def __init__(self):
        super().__init__(HighEngine(), HighBreaking())

class OffRoadVehicle(Vehicle):
    def __init__(self):
        super().__init__(NormalEngine(), HighBreaking())

class PassengerVehicle(Vehicle):
    def __init__(self):
        super().__init__(LowEngine(), LowBreaking())

# Main class to execute the code
class Main:
    def main(self):
        sportsVehicle = SportsVehicle()
        sportsVehicle.start_engine()  
        sportsVehicle.apply_break()   

        offRoadVehicle = OffRoadVehicle()
        offRoadVehicle.start_engine()
        offRoadVehicle.apply_break()

        passengerVehicle = PassengerVehicle()
        passengerVehicle.start_engine()
        passengerVehicle.apply_break()

if __name__ == "__main__":
    main = Main()
    main.main()
