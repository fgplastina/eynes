PI = 3.14

class Circle():

    def __init__(self, radio):
        self._validate_radio(radio)
        self.__radio = radio
        super().__init__()

    def __str__(self):
        return f"{self.__class__.__name__ } with radio: {self.__radio}"

    @property
    def radio(self):
        return self.__radio

    @radio.setter
    def radio(self, radio):
        self._validate_radio(radio)
        self.__radio = radio


    def _validate_radio(self, radio):
        if radio <= 0:
            raise Exception(f"Lo lamentamos, no es posible construir un circulo con radio {radio}. Por favor, introduzca un numero mayor a 0")

    def area(self):
        return PI * self.__radio**2

    def perimeter(self):
        return 2 * PI * self.__radio

    def __mul__(self, value):
        self._validate_radio(value)
        new_radio  = self.__radio * value
        return Circle(new_radio)


def _show_circle_area_and_perimeter(circle):
    print(circle)
    print(circle.area())
    print(circle.perimeter())
    print("\n")


def show_circle():
    circle = Circle(10)
    _show_circle_area_and_perimeter(circle)

    circle.radio = 11
    _show_circle_area_and_perimeter(circle)

    new_circle = circle * 5

    print(f"Nuevo circulo: {new_circle}")
    _show_circle_area_and_perimeter(new_circle)

    # Mostrar que no se puede instanciar a un radio igual o menor a 0
    try:
        new_circle = Circle(0)
    except Exception as e:
        print(e)

    # Mostrar que no se puede cambiar a un radio igual o menor a 0
    try:
        circle.radio = -10
    except Exception as e:
        print(e)

    # Mostrar que no se puede cambiar a un radio igual o menor a 0
    try:
        circle.radio = 10
        new_circle = circle * -21283100
    except Exception as e:
        print(e)


def main():
    show_circle()

if __name__=="__main__":
    main()
