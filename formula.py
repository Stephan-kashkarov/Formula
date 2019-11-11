import machine
import pyb
import st7789 as display
from helper import bitmap


class App:
    def __init__(self):
        self.active = True
        self.spi = machine.SPI(1)
        self.i2c = machine.I2C(freq=400000)
        self.interaction = list()
        self.view = list()
        self.timer = 0
        self.sleep_timer = pyb.Timer(1)
        self.sleep_timer.init(freq=1)
        self.sleep_timer.callback(self.incr_timer())

    def incr_timer(self) -> None:
        self.timer += 1
    
    def update(self) -> None:
        self.interaction.extend(*self.get_touch())
        while len(self.interaction) >= 1:
            self.timer = 0
            self.interact(self.view[-1], self.interaction.pop())

    def sleep(self) -> None:
        self.interaction.extend(*self.get_gesture())
        while len(self.interaction):
            if self.interaction.pop().g_force > 1:
                return True

class View:
    def __init__(self):
        pass

    def render(self):
        pass

    def interact(self, x, y, type):
        pass

class HomeView(View):
    def __init__(self, **kwargs):
        super().__init__()

    def render(self) -> list:
        return [
            Box(
                pos=(0, 0),
                size=(self.width/2, self.height),
                color=(255, 0, 0),
                func=lambda: self.stack.append(ClockView),
            ),
            Box(
                pos=(self.width/2, 0),
                size=(, self.height),
                color=(0, 255, 0),
                func=lambda: self.stack.append(DemoView),
            )
        ]

    def update(self) -> None:
        pass

class Element:
    def __init__(self, **kwargs) -> Element:
        self.bitmap = list()
        self.pos = kwargs['pos']
        self.size = kwargs['size']
        self.func = kwargs.get('func')
        self.children = kwargs.get('children', list())

class Box(Element):
    def __init__(self, **kwargs) -> Box:
        super().__init__(self)
        self.color = kwargs['color']
        
    def draw(self) -> None:
        display.fill_rect(*self.pos, *self.size, display.color565(self.color))

class Row(Element):
    def __init__(self, **kwargs) -> Row:
        super().__init__(self)

    def draw(self) -> None:




class ClockView(View):
    def __init__(self, **kwargs) -> ClockView:
        super().__init__(**kwargs)
        self.watch_timer = pyb.Timer(id=2)
    
    def draw()

    


