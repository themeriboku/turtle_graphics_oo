import turtle
import random

class Polygon:
    def __init__(self, num_sides, size, orientation, location, color, border_size):
        self.num_sides = num_sides
        self.size = size
        self.orientation = orientation
        self.location = location
        self.color = color
        self.border_size = border_size

    def draw(self):
        turtle.penup()
        turtle.goto(self.location[0], self.location[1])
        turtle.setheading(self.orientation)
        turtle.color(self.color)
        turtle.pensize(self.border_size)
        turtle.pendown()
        for _ in range(self.num_sides):
            turtle.forward(self.size)
            turtle.left(360 / self.num_sides)
        turtle.penup()

    def move(self, new_location):
        self.location = new_location


class PolygonArt:
    def __init__(self, shape_type, num_shapes):
        self.shape_type = shape_type
        self.num_shapes = num_shapes

    def get_new_color(self):
        return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def get_shape_details(self, shape_type):
        if shape_type == 1:
            return 3, False
        elif shape_type == 2:
            return 4, False
        elif shape_type == 3:
            return 5, False
        elif shape_type == 4:
            return random.randint(3, 5), False
        elif shape_type in [5, 6, 7]:
            return shape_type - 2, True
        elif shape_type == 8:
            return random.randint(3, 5), True

    def run(self):
        for _ in range(self.num_shapes):
            if self.shape_type == 9:
                shape_type = random.randint(1, 8)  # Randomly select shape type for each shape
            else:
                shape_type = self.shape_type

            num_sides, overlap = self.get_shape_details(shape_type)
            size = random.randint(60, 100)
            orientation = random.randint(0, 360)
            location = [random.randint(-100, 100), random.randint(-100, 100)]  # Smaller range for central position
            color = self.get_new_color()
            border_size = random.randint(1, 5)

            if overlap:
                polygon = EmbeddedPolygon(num_sides, size, orientation, location, color, border_size, 3, 0.618)
            else:
                polygon = Polygon(num_sides, size, orientation, location, color, border_size)
            polygon.draw()


class EmbeddedPolygon(Polygon):
    def __init__(self, num_sides, size, orientation, location, color, border_size, num_levels, reduction_ratio):
        super().__init__(num_sides, size, orientation, location, color, border_size)
        self.num_levels = num_levels
        self.reduction_ratio = reduction_ratio

    def draw(self):
        current_size = self.size
        current_location = self.location[:]
        for _ in range(self.num_levels):
            super().draw()
            turtle.penup()
            turtle.forward(current_size * (1 - self.reduction_ratio) / 2)
            turtle.left(90)
            turtle.forward(current_size * (1 - self.reduction_ratio) / 2)
            turtle.right(90)
            current_location[0] = turtle.pos()[0]
            current_location[1] = turtle.pos()[1]
            current_size *= self.reduction_ratio
            self.size = current_size
            self.location = current_location


def main():
    shape_type = int(input("Which art do you want to generate? Enter a number between 1 to 9 inclusive: "))

    turtle.speed(0)
    turtle.bgcolor('black')
    turtle.tracer(0)
    turtle.colormode(255)

    num_shapes = 20

    art_generator = PolygonArt(shape_type, num_shapes)
    art_generator.run()

    turtle.done()


if __name__ == "__main__":
    main()
