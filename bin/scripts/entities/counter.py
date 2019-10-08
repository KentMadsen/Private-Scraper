zero = 0
movement_size = 1


class Counter:
    global zero, movement_size
    """ """
    def __init__(self):
        self.value = zero
        self.movement = movement_size

    def increase(self, variable_value):
        self.value = self.value + variable_value

    def increment(self):
        self.increase(self.movement)

    def decrease(self, variable_value):
        self.value = self.value - variable_value

    def decrement(self):
        self.decrease(self.movement)

    def reset(self):
        self.set_value(zero)

    def is_zero(self):
        return self.get_value() == zero

    def get_value(self):
        return self.value

    def set_value(self, variable_value):
        self.value = variable_value
        return self.value



