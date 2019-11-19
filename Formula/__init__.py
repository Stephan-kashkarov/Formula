import machine
import pyb
import ft6206 as touch
from lis2hh12 import accel
from Formula.views import HomeView
from Formula.interactions import Touch, Gesture



class App:
    """
    App class

    The app class is the central unit of the framework. The idea
    of an instance of app is to handle view structure and SPI/I2C
    Machine communication aswell as sleep state. 

    the app class contains the following useful arguments:
    - interaction: a stack of gestures and taps
    - view: a stack of views
    - sleep_timer: a timer callback to put the system into a sleep state

    The app class contains the following methods:
    - incr_timer: a method to increment the sleep timer called in the timer callback
    - sleep: the sleep state logic cycle
    - update: the live state logic cycle
    - get_touch: generate touch events
    - get_gesture: generate gesture events
    """
    def __init__(self, **kwargs):
        self.active = True
        self.spi = machine.SPI(1)
        self.i2c = machine.I2C(freq=400000)
        self.interaction = list()
        self.view = [*kwargs.get("view", HomeView())]
        self.timer = 0
        self.sleep_timer = pyb.Timer(1)
        self.sleep_timer.init(freq=1)
        self.sleep_timer.callback(self.incr_timer())

    def incr_timer(self) -> None:
        """
        incr_timer method
        
        timer incrementer for sleep_timer callback
        """
        self.timer += 1

    def update(self) -> None:
        """
        update method

        This method fills the interaction stack with touch events, 
        renders the top view off the view stack, passes interactions down
        and draws to the screen.
        
        """
        self.interaction.extend(*self.get_touch())
        while len(self.interaction) >= 1:
            self.timer = 0
            self.interact(self.view[-1], self.interaction.pop())
        if not self.screen:
            self.screen = self.view[-1].render()
        self.screen.interact(self.interaction.pop())
        self.screen.draw()
        

    def sleep(self) -> None:
        """
        sleep method

        the sleep method allows the device sleep when it is not
        in use. The device sits and waits on a gesture input before
        sending the device back into the update method
        """
        self.interaction.extend(*self.get_gesture())
        while len(self.interaction):
            if self.interaction.pop().total() > 256:
                return True

    def get_touch(self) -> [Touch]:
        """ get touch is a method to get touch inputs """
        for i in range(5):
            for event in touch.read():
                yield Touch(**event)

    def get_gesture(self) -> [Gesture]:
        """ get touch is a method to get gesture inputs """
        for i in range(5):
            yield Gesture(**accel.read())


    def run(self):
        """
        The run method

        The run method sets the entire program in motion
        in a while true loop. The method checks if the device is sleeping
        and if not runs the update method or the sleep method.
        """
        while True:
            if self.active:
                self.update()
            else:
                self.active = self.sleep()
