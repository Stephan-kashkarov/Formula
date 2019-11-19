class Touch:
    def __init__(self, **kwargs):
        self.type = 'Touch'
        self.x = kwargs['x']
        self.y = kwargs['y']
        self.id = kwargs['id']


class Gesture:
    def __init__(self, **kwargs):
        self.type = 'Gesture'
        self.x = kwargs['x']
        self.y = kwargs['y']
        self.z = kwargs['z']

    def total(self):
        return sum([abs(x) for x in [self.x, self.y, self.z]])
