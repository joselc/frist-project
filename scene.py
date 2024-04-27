from manim import *

class Visual2ndDegree(Scene):

    origin_x = 0
    origin_y = 0

    def construct(self):
        equation = MathTex(
            r"x^2+10x=39",
            substrings_to_isolate="x^2+10x"
            )
        equation.set_color_by_tex("", WHITE)
        equation.set_color_by_tex("x^2+10x", YELLOW)
        square = Square(5)
        equation.next_to(square,UP)

        square_left_x = square.get_x() - square.side_length/2
        square_right_x = square.get_x() + square.side_length/2
        square_bottom_y = square.get_y() - square.side_length/2
        square_top_y = square.get_y() + square.side_length/2

        self.origin_x = square_left_x
        self.origin_y = square_bottom_y

        dashed_vertical = DashedLine([self.X(square.side_length*2/7), self.Y(0),  0.],
                                     [self.X(square.side_length*2/7), self.Y(square.side_length), 0.],
                                     dash_length=0.1)
        
        dashed_horizontal = DashedLine([self.X(0), self.Y(square.side_length*5/7),  0.],
                                       [self.X(square.side_length), self.Y(square.side_length*5/7), 0.],
                                       dash_length=0.1)
        
        polygon = Polygon([self.X(0), self.Y(0), 0.],
                           [self.X(square.side_length*2/7), self.Y(0), 0.],
                           [self.X(square.side_length*2/7), self.Y(square.side_length*5/7), 0.],
                           [self.X(square.side_length), self.Y(square.side_length*5/7), 0.],
                           [self.X(square.side_length), self.Y(square.side_length), 0.],
                           [self.X(0), self.Y(square.side_length), 0.],
                           [self.X(0), self.Y(0), 0.])
        polygon.set_opacity(0)
    
        self.add(equation)
        self.play(Create(square))
        self.play(Create(dashed_vertical),Create(dashed_horizontal))
        self.play(Create(polygon))
        self.play(polygon.animate.set_fill(YELLOW, opacity = 0.5))

    def X(self, x):
        return self.origin_x + x
    
    def Y(self, y):
        return self.origin_y + y
