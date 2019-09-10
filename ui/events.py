# Guesture codes to names
gestures = {
    0: "Up",
    1: "Right",
    2: "Down",
    3: "Left",
    4: "In",
    5: "Out",
    None: None
}

class Event:
    def __init__(self, **kwargs):
        self.position = kwargs['position'] # postition (y, x)
        self.event = gestures[kwargs.get('guesture_id')] # the direction of the interaction
        self.offset = kwargs.get('offset', None) # offset in position of action
