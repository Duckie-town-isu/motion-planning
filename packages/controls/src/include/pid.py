class PID:
    def __init__(self,kP,kI,kD,kF):
        self.kP = kP
        self.kI = kI
        self.kD = kD
        self.kF = kF

        self.setpoint = 0
        self.prevError = 0
        self.integral = 0

    def set(self,setpoint):
        self.setpoint = setpoint

    def update(self,current,dt):
        error = self.setpoint - current
        dervative = (error - self.prevError)/dt
        self.integral += error*dt
        power = self.kP * error + self.kI * self.integral + self.kD * derivative
        self.prevError = error

        return power


