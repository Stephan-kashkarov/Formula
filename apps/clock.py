from ui.app import App
from engine import text, line, pixel, box

# RED = (255, 0, 0)
# GREEN = (0, 255, 0)
# BLUE = (0, 0, 255)

class DigitalClock(App):
    def __init__(self, **kwargs):
        super().__init__()
        self.size = kwargs.get('size', (128, 128))
        self.center = (self.size[0]/2, self.size[1]/2)
    
    def interact(self):
        pass

    def draw(self) -> list:
        self.canvus = text(self.canvus, "hello", (x, y), 3)

