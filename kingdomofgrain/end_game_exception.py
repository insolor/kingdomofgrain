class EndGameException(Exception):
    def __init__(self, oi):
        self.oi = oi
