import math

class Operations:
    """
    Class containing all illegal operations of calculator.
    """


    @staticmethod
    def convert_to_int_or_float(val):
        if '.' in val:
            new_val = float(val)
        else:
            new_val = int(val)
        return new_val


    @ staticmethod
    def add(val1, val2):
        if isinstance(val1, str) and isinstance(val2, str):
            val1 = Operations.convert_to_int_or_float(val1)
            val2 = Operations.convert_to_int_or_float(val2)
            return val1 + val2

    @staticmethod
    def multiply(val1, val2):
        if isinstance(val1, str) and isinstance(val2, str):
            val1 = Operations.convert_to_int_or_float(val1)
            val2 = Operations.convert_to_int_or_float(val2)
            return val1 * val2

    @staticmethod
    def subtract(val1, val2):
        if isinstance(val1, str) and isinstance(val2, str):
            val1 = Operations.convert_to_int_or_float(val1)
            val2 = Operations.convert_to_int_or_float(val2)
            return val1 - val2

    @staticmethod
    def division(val1, val2):
        if isinstance(val1, str) and isinstance(val2, str):
            val1 = Operations.convert_to_int_or_float(val1)
            val2 = Operations.convert_to_int_or_float(val2)
            return val1/val2


    @staticmethod
    def squared(val):
        if isinstance(val, str):
            val = Operations.convert_to_int_or_float(val)
            return val ** 2

    @staticmethod
    def negate(val):
        if isinstance(val, str):
            val = Operations.convert_to_int_or_float(val)
            return -val


    @staticmethod
    def inverse(val):
        if isinstance(val ,str):
            val = Operations.convert_to_int_or_float(val)
            return 1/val

    @staticmethod
    def squareroot(val):
        if isinstance(val, str):
            val = Operations.convert_to_int_or_float(val)
            return math.sqrt(val)


    @staticmethod
    def percentage_raw(val):
        if isinstance(val, str):
            val = Operations.convert_to_int_or_float(val)
            return val * (val/100)


    @staticmethod
    def percentage_with_value(val1, val2):
        if isinstance(val1, str) and isinstance(val2, str):
            val1 = Operations.convert_to_int_or_float(val1)
            val2 = Operations.convert_to_int_or_float(val2)
            return val1 * (val2/100) 