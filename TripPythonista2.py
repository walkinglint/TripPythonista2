from scene import *
from random import random, randrange
import colorsys

cn = 0
shapes = ['ellipse', 'rect', 'line']

class MyScene(Scene):
    def setup(self):
        background('black')
        self.init()
        background('white')
    
    def init(self):
        global cn
        cn = 0
        self.shapes = []
    
    def update(self):
        global cn
        cn += 1
        if cn % 10 == 0:
            self.init()
        
        translate(int(self.size.w // 2), int(self.size.h // 2))
        background('black')
        
        if cn % 1 == 0:  # Add a new shape every frame (increased frequency)
            for _ in range(5):  # Add 5 shapes at a time
                shape = shapes[randrange(len(shapes))]
                color = colorsys.hsv_to_rgb(random(), 1, 1)
                size = randrange(20, 50)
                x = randrange(-self.size.w // 2, self.size.w // 2)
                y = randrange(-self.size.h // 2, self.size.h // 2)
                angle = random() * 360
                self.shapes.append({'shape': shape, 'color': color, 'size': size, 'x': x, 'y': y, 'angle': angle})
        
        for shape_info in self.shapes:
            shape_info['size'] += 1  # Increase size to create the effect of coming closer
            self.draw_shape(shape_info)
    
    def draw_shape(self, shape_info):
        shape = shape_info['shape']
        color = shape_info['color']
        size = shape_info['size']
        x = shape_info['x']
        y = shape_info['y']
        angle = shape_info['angle']
        
        push_matrix()
        translate(x, y)
        rotate(angle)
        stroke(*color)
        stroke_weight(randrange(1, 5))
        fill(*color)
        
        if shape == 'ellipse':
            ellipse(0, 0, size, size)
        elif shape == 'rect':
            rect(-size / 2, -size / 2, size, size)
        elif shape == 'line':
            self.draw_line(0, 0, size)
        
        pop_matrix()
    
    def draw_line(self, x, y, size):
        length = randrange(20, 100)
        line(x, y, x + length, y)
    
    def touch_began(self, touch):
        self.init()

if __name__ == '__main__':
    run(MyScene(), PORTRAIT, 2)
