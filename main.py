import matplotlib.pyplot as plt
import numpy as np


class PIDController:

  def __init__(self, kp, ki, kd, setpoint):
    self.kp = kp
    self.ki = ki
    self.kd = kd
    self.setpoint = setpoint

    self.integral = 0.0
    self.previous_error = 0.0

  def update(self, current_value, dt):
    error = self.setpoint - current_value

    p = self.kp * error

    self.integral += error * dt
    i = self.ki * self.integral

    derivative = (error - self.previous_error) / dt if dt > 0 else 0.0
    d = self.kd * derivative

    self.previous_error = error

    return p + i + d



total_time = 10.0 
dt = 0.05 
time = np.arange(0, total_time, dt)

setpoint = 10.0 
current_value = 0
Kp = 1.0
Ki = 0.0
Kd = 0.5

pid = PIDController(Kp, Ki, Kd, setpoint)


response_values = []
setpoint_values = []

system_time_constant = 0.6

for t in time:
  control_effort = pid.update(current_value, dt)

  rate_of_change = (control_effort - current_value) / system_time_constant
  current_value += rate_of_change * dt

  response_values.append(current_value)
  setpoint_values.append(setpoint)

plt.figure(figsize=(10, 5))
plt.plot(
    time, response_values, label="System Response", color="#1f77b4", linewidth=2
)
plt.plot(
    time,
    setpoint_values,
    label="Target Threshold",
    color="#d62728",
    linestyle="--",
    linewidth=2,
)

plt.title(
    f"PID Control System Response (Kp={Kp}, Ki={Ki}, Kd={Kd})", fontsize=13
)
plt.xlabel("Time (seconds)", fontsize=11)
plt.ylabel("System Value", fontsize=11)
plt.grid(True, linestyle=":", alpha=0.6)
plt.legend(fontsize=11)
plt.tight_layout()
plt.ylim(setpoint -5, setpoint + 5)
plt.show()
