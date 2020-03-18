import pygame as pg
from pygame import sprite


class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return "Vector ({}, {})".format(self.x, self.y)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __rmul__(self, k: float):
        return Vector(k * self.x, k * self.y)

    def __mul__(self, k: float):
        return self.__rmul__(k)

    def __truediv__(self, k: float):
        div = 1/k
        return Vector(div * self.x, div * self.y)

    def __neg__(self):
        return Vector(-1 * self.x, -1 * self.y)

    def __eq__(self, other):
        self.x = other.x
        self.y = other.y
        return self

    @staticmethod
    def test():  # feel free to change the test code
        v = Vector(x=5, y=5)
        u = Vector(x=4, y=4)
        print('v is {}'.format(v))
        print('u is {}'.format(u))
        print('uplusv is {}'.format(u + v))
        print('uminusv is {}'.format(u - v))
        print('ku is {}'.format(3 * u))
        print('-u is {}'.format(-1 * u))


class Ship(sprite):
    def __init__(self, game, vector=Vector()):
        # Pass Params to Properties
        self.game = game
        self.vector = vector
        # Load in Ship's Sprite
        self.image = pg.image.load("Ship.png")
        # Ship starts at midbottom of the display, which access from game object
        self.rect = self.game.screen.midbottom
        self.lasers = []

    # Sets ship to screen center
    def center_ship(self):
        self.rect = self.game.screen.midbottom

    # Creates a laser at its current position, and tracks it in its laser list
    def fire(self):
        # Create laser rect with ship's rect center
        laser = Laser(rect=self.rect.center)
        self.lasers.append(laser)

    # Removes all lasers from it's list
    def remove_lasers(self):
        self.lasers.clear()

    # Changes position based on its vector
    def move(self):
        # If vector is (0,0), no movement
        if self.vector == Vector():
            return

        # Incrementing rect based on vector
        self.rect.left += self.vector.x
        self.rect.top += self.vector.y

    def draw(self): self.game.screen.blit(self.image, self.rect)

    def update(self):
        self.move()
        self.draw()

        # Since Ship is handling Lasers, call their update method
        for laser in self.lasers:
            laser.update()


def main():
    Vector.test()


if __name__ == '__main__':
    main()
