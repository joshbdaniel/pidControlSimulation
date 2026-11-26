# PID Control System Simulation

A lightweight Python simulation of a **Proportional-Integral-Derivative (PID)** controller driving a first-order dynamic system, complete with discrete-time numerical safeguards and Matplotlib plotting centered around the target threshold.

## Features

* **Discrete PID Controller (`PIDController`)**: Computes proportional (`P`), integral (`I`), and derivative (`D`) control effort each time step.
* **First-Order Plant Model**: Simulates system dynamics via forward Euler integration (`dt`) governed by `system_time_constant`.
* **Centered Threshold Visualization**: Automatically sets symmetric y-axis limits around `THRESHOLD` so the target line sits in the middle of the plot.
* **Config-Driven Gains & Initial State**: Reads setpoint, initial value, and PID gains from `configs.py`.

## Project Structure

```text
.
├── configs.py      # Simulation constants and PID gain parameters (required)
└── simulate.py     # PIDController class, simulation loop, and plot output
