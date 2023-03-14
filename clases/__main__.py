class Circle():

    def __init__(self, radio):
        self._validate_radio(radio)
        self.radio = radio
        super().__init__()

    def __str__(self):
        return f"{self.__class__.__name__ } with radio: {self.radio}"

    def _validate_radio(self, radio):
        if radio <= 0:
            raise Exception("Lo lamentamos, no es posible construir un circulo con radio igual o inferior a 0. Por favor, introduzca un numero mayor")

    def area(self):
        ...
    def perimeter(self):
        ...

def main():
    circle = Circle(10)
    print(circle)
#    circle = Circle(0)
#    print(circle.__dict__)

if __name__=="__main__":
    main()
