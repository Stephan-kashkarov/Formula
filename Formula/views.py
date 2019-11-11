import pyb
from Formula.elements import (Box, Clock)

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


class ClockView(View):
    def __init__(self, **kwargs) -> ClockView:
        super().__init__(**kwargs)
        self.watch_timer = pyb.Timer(id=2)

    def render(self):
        current_time = time.localtime()
        return Clock(current_time)
