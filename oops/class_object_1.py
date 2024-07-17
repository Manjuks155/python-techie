class Triangle:
    area = 20
    def __init__(self, length):
        print("This is triangle")
        self.leng = length
    def get_area(self):
        print(self.area)


triangle_1 = Triangle(10)
print(triangle_1.leng)
print(triangle_1.area)
triangle_1.get_area()
