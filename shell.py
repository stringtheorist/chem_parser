__author__ = 'aftab'

class Shell:
    no_primitives = 0
    angular_momentum = -1
    exponents = []
    coefficients = []
    center = [0.0, 0.0, 0.0]

    def get_no_primitives(self):
        return self.no_primitives
    def get_center_coordinates(self):
        return self.center
    def get_angular_momentum(self):
        return self.angular_momentum


