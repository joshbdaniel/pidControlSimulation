# PID Control System Simulation

A lightweight Python simulation of a **Proportional-Integral-Derivative (PID)** controller driving a first-order dynamic system, complete with discrete-time numerical safeguards and Matplotlib plotting centered around the target threshold. 

Graphs how a system responds to each of the control gains to match a pre-set threshold value. 

$P = K_p \cdot e(t)$
$I = K_i \int e\,dt$
$D = K_d \frac{de}{dt}$

## Features

* **Discrete PID Controller (`PIDController`)**: Computes proportional (`P`), integral (`I`), and derivative (`D`) control effort each time step.
* **First-Order Plant Model**: Simulates system dynamics via forward Euler integration (`dt`) governed by `system_time_constant`.
* **Centered Threshold Visualization**: Automatically sets symmetric y-axis limits around `THRESHOLD` so the target line sits in the middle of the plot.
* **Config-Driven Gains & Initial State**: Reads setpoint, initial value, and PID gains from `configs.py`.

<img width="748" height="418" alt="image" src="https://github.com/user-attachments/assets/5d8a5d13-8c88-42b8-ade1-cfe3c9365027" />

<img width="748" height="419" alt="image" src="https://github.com/user-attachments/assets/6d7af5cb-425e-4a8e-b7ce-54e57c4a0e47" />

