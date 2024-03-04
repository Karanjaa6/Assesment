class Rectangle():
    length = 45
    width = 30
    area = (length*width)
    print(area)


class Circle():
    radius = float(input('Enter cirle radius'))
    def area(self):
        return self.radius * self.radius * 22/7
    def perimeter(self):
        return self.radius * 2 * 22/7
print(Circle().area())
print(Circle().perimeter())



