import machine
import pyb
import st7789 as display
import time
import math

class Element:
    """
    Element class

    The element class contains the basis of an element,
    each element is a building block of the program and the
    lowest level of the framework.

    Arguemtns:
    - pos (x, y): the top left corner position of the element relative to the screen
    - size (w, h): the width and height of the element
    - func: a callback for interaction objects
    - children: a list of sub elements
    - base: a boolean defining if the element is a base or not

    """
    def __init__(self, **kwargs):
        self.pos = kwargs['pos']
        self.size = kwargs['size']
        self.func = kwargs.get('func')
        self.children = kwargs.get('children', list())
        self.base = True


class Box(Element):
    """
    Box element

    The box element is a solid box of color based
    on the element class
    """
    def __init__(self, **kwargs):
        super().__init__(self)
        self.color = kwargs['color']

    def draw(self) -> None:
        display.fill_rect(*self.pos, *self.size, display.color565(self.color))


class Row(Element):
    """
    Row elment

    The row element is a structural non-base
    element used to horizontally arrange elements.
    Each element is resized horizontally to ensure
    a fit
    
    """
    def __init__(self, **kwargs):
        super().__init__(self)
        self.base = False

    def draw(self) -> None:
        base = self.pos[0]
        modifier = self.size[0]/len(self.children if self.children else 1)
        for i, child in enumerate(self.children):
            child.pos[0] = self.pos[0] + base + (modifier * i)
            child.size[0] = modifier
            child.draw()


class Col(Element):
    """
    Col elment

    The col element is a structural non-base
    element used to vertically arrange elements.
    Each element is resized vertically to ensure
    a fit
    
    """
    def __init__(self, **kwargs):
        super().__init__(self)
        self.base = False

    def draw(self) -> None:
        base = self.pos[1]
        modifier = self.size[1]/len(self.children if self.children else 1)
        for child in self.children:
            child.pos[1] = self.pos[1] + base + modifier
            child.size[1] = modifier
            child.draw()

class Clock(Element):
    """
    Clock element

    The clock element shows what a fully flashed
    out element can be. This element renders into
    an analogue clock within the pos of the element
    and is totally resuable.
    
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def draw(self) -> None:
        """
        Clock
        This function takes a time object and
        draws an analogue clock onto the screen
        in UTC time.
        Arg:
            t: The time object from the utime lib
        Returns: 
            None
        """
        display.fill(display.color565((255, 255, 255)))
        # tft.circle(Center, 63, TFT.GRAY)
        h, m, s = self.convTime(time.localtime())
        self.hand(h, 40, (64, 64), display.color565((0, 0, 0)))
        self.hand(m, 20, (64, 64), display.color565((150, 150, 150)))
        self.hand(s, 50, (64, 64), display.color565((0, 255, 0)))

    def convTime(self, t) -> (int, int, int):
        """ Conv time
            This function takes Time object and returns 3 normalised
            integers to alow for the clock hand function to be reused
            Args:
                t: The time object from the utime lib
            
            Returns:
                (H, M, S): set of three integers in range(60)
        """
        return (t[3] % 12) * 5, t[4], t[5]

    def hand(self, sec: float, radius: float, center: (int, int), color: (int, int, int)) -> None:
        """
        hand function
        This function takes a number form 0 to 60
        and prints it as an analogue hand.
        Args:
            secs: number between 0 and 60 of the time
            radius: the length of the hand
            center: the center point in (x, y)
            color: rgb value of the line (R, G, B) in ints
        Returns:
            None
        """
        if sec == 0 or sec == 60:
            display.vline(center, -(radius), color)
        else:
            if 0 < sec <= 15:  # First sector
                A = math.tan(
                    math.radians(90 - (sec * 6))
                )
                y = center[0] - math.sqrt((math.pow(radius, 2) * A) / (A + 1))
                x = center[1] + (y / A)
            elif 15 < sec <= 30:  # Second sector
                A = math.tan(
                    math.radians((sec - 15) * 6)
                )
                y = center[0] + math.sqrt((math.pow(radius, 2) * A) / (A + 1))
                x = center[1] + (y / A)
            elif 30 < sec <= 45:  # Thrid sector
                A = math.tan(
                    math.radians(90 - ((sec - 30) * 6))
                )
                y = center[0] + math.sqrt((math.pow(radius, 2) * A) / (A + 1))
                x = center[1] - (y / A)
            elif 45 < sec < 60:  # Forth sector
                A = math.tan(
                    math.radians((sec - 45) * 6)
                )
                y = center[0] - math.sqrt((math.pow(radius, 2) * A) / (A + 1))
                x = center[1] - (y / A)

            display.line(center, (int(x), int(y)), color)
