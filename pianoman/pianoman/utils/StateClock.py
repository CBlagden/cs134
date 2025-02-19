# Helper class to hold state time

def ros_to_float(t, rostime):
    if (rostime):
        converted_t = t.nanoseconds*1e-9
    else:
        converted_t = t
    return converted_t

class StateClock():
    def __init__(self, t0, rostime=False):
        self.t0 = ros_to_float(t0, rostime)
        self.paused = False

    # Get the delta time, including pauses
    def t_since_start(self, t, rostime=False):
        t = ros_to_float(t, rostime)
        if (self.paused):
            self.paused = False
            self.t0 = t - self.paused_dt
    
        return t - self.t0

    # Stop the clock
    def pause(self, t, rostime=False):
        t = ros_to_float(t, rostime)
        dt = self.t_since_start(t)

        self.paused = True
        self.paused_dt = dt
    
    # restart
    def restart(self, t0, rostime=False):
        self.t0 = ros_to_float(t0, rostime)
        self.paused = False
        
    def restart_with_deltat(self,t0,startdelta, rostime=False):
        self.t0 = ros_to_float(t0, rostime) - startdelta
        self.paused = False


    def __repr__(self):
        return f"{self.t0}"