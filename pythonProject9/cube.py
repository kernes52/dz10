class Rectangle:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def area(self):
        return self.__length * self.__width

    def perimeter(self):
        return 2 * (self.__length + self.__width)

if __name__ == "__main__":
    rect = Rectangle(30, 15)

    print(f"Площа прямокутника: {rect.area()}")

    print(f"периметр прямокутника: {rect.perimeter()}")
