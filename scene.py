from manim import Scene,MathTex,Square,DashedLine,Polygon,Create,YELLOW,WHITE,UP

class Visual2ndDegree(Scene):

    origin_x = 0
    origin_y = 0

    def construct(self):
        equation = MathTex(
            r"{{x^2+10x}}={{39}}",
            )
        equation.set_color_by_tex("", WHITE)
        square = Square(5)
        equation.next_to(square,UP)

        square_left_x = square.get_x() - square.side_length/2
        square_bottom_y = square.get_y() - square.side_length/2

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
        self.play(polygon.animate.set_fill(YELLOW, opacity = 0.5),equation[0].animate.set_color(YELLOW))
        self.wait(duration=3.0,stop_condition=None,frozen_frame=None)

    def X(self, x):
        return self.origin_x + x
    
    def Y(self, y):
        return self.origin_y + y
    

class ColoredLatex(Scene):
    def construct(self):
        equation = MathTex(
            r"{{x^2+10x}}={{39}}",
            )
        equation.set_color_by_tex("", WHITE)
        equation[0].set_color(YELLOW)

        self.add(equation)
