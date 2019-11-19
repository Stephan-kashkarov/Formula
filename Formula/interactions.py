class Touch:
    """
    Touch object
    
    The touch object contains the x, y and id of a
    touch event.
    """
    def __init__(self, **kwargs):
        self.type = 'Touch'
        self.x = kwargs['x']
        self.y = kwargs['y']
        self.id = kwargs['id']


class Gesture:
    """
    Gesture object

    The Gesture object contains the x, y and z of a
    Gesture event.
    """
    def __init__(self, **kwargs):
        self.type = 'Gesture'
        self.x = kwargs['x']
        self.y = kwargs['y']
        self.z = kwargs['z']

    def total(self):
        return sum([abs(x) for x in [self.x, self.y, self.z]])
