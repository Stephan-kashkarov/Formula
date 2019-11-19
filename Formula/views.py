import pyb
from Formula.elements import (Box, Clock, Row)

class View:
    """
    View class

    an instance of a view is like a page
    on a website. It is made to keep content
    organised and to make multi page apps possible.
    
    All functions are to be expanded from in this class
    """
    def __init__(self, **kwargs):
        self.height = kwargs['height']
        self.width = kwargs['width']
        self.stack = []

    def render(self):
        pass

    def interact(self, x, y, type):
        pass


class HomeView(View):
    """
    HomeView View

    The homeview is the defualt view for the oage and is simply
    an example view with two boxes on the screen next to eachother
    the left box renders a clock and switches view and the right box
    renders a screen demo view which is yet to be implemented
    """
    def __init__(self, **kwargs):
        super().__init__()

    def render(self) -> list:
        return Row(
            pos=(0, 0),
            size=(self.width, self.height),
            children=[
                Box(
                    pos=(0, 0),
                    size=(None, self.height),
                    color=(255, 0, 0),
                    func=lambda: self.stack.append(ClockView),
                ),
                Box(
                    pos=(self.width/2, 0),
                    size=(None, self.height),
                    color=(0, 255, 0),
                ),
            ]
        )



class ClockView(View):
    """ClockView is an example view for the clock used in the example above"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def render(self):
        return Clock()
