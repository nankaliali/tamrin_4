class Ccy:
    currencies =  {'CHF': 1.0821202355817312,
                       'CAD': 1.488609845538393,
                       'GBP': 0.8916546282920325,
                       'JPY': 114.38826536281809,
                       'EUR': 1.0,
                       'USD': 1.11123458162018}
    def __init__(self, value, unit="EUR"):
        self.value = value
        self.unit = unit
    def __str__(self):
        return f'{self.value:.2f} {self.unit}'
    def __repr__(self):
        return f'Ccy({self.value}, "{self.unit}")'

    def changeTo(self, new_unit):
        """
            An Ccy object is transformed from the unit "self.unit" to "new_unit"
        """
        self.value = (self.value / Ccy.currencies[self.unit] * Ccy.currencies[new_unit])
        self.unit = new_unit
    def __add__(self, other):
        """
            Defines the '+' operator.
            If other is a CCy object the currency values
            are added and the result will be the unit of
            self. If other is an int or a float, other will
            be treated as a Euro value.
        """
        if type(other) == int or type(other) == float:
                x = (other * Ccy.currencies[self.unit])
        else:
                x = (other.value / Ccy.currencies[other.unit] * Ccy.currencies[self.unit])
        return Ccy(x + self.value, self.unit)
    def __iadd__(self, other):
        """
            Similar to __add__
        """
        if type(other) == int or type(other) == float:
            x = (other * Ccy.currencies[self.unit])
        else:
            x = (other.value / Ccy.currencies[other.unit] * Ccy.currencies[self.unit])
            self.value += x
        return self
    def __radd__(self, other):
        res = self + other
        if self.unit != "EUR":
            res.changeTo("EUR")
        return res
        # __sub__, __isub__ and __rsub__ can be defined analogue
    def __mul__(self, other):
        """
            Multiplication is only defined as a scalar multiplication,
            i.e. a money value can be multiplied by an int or a float.
            It is not possible to multiply to money values
        """
        if type(other)==int or type(other)==float:
            return Ccy(self.value * other, self.unit)
        else:
            raise TypeError("unsupported operand type(s) for *: 'Ccy' and " + type(other).__name__)
    def __rmul__(self, other):
        return self.__mul__(other)
    def __imul__(self, other):
        if type(other)==int or type(other)==float:
            self.value *= other
            return self
        else:
            raise TypeError("unsupported operand type(s) for *: 'Ccy' and " + type(other).__name__)

x = Ccy(10.00, "EUR")
y = Ccy(10.00, "GBP")
print(x + y)
print(x.__repr__())