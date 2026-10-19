class PDController:
    """A simple discrete-time PD controller."""
    def __init__(self, kp=0.15, kd=0.6):
        self.kp = kp
        self.kd = kd
        self.previous_error = 0.0

    def compute(self, reference, observation):
        e = reference - observation
        u = self.kp * e + self.kd * (e - self.previous_error)
        self.previous_error = e
        return u
    
    def reset(self):
        self.previous_error = 0.0